"""Run orchestration. One invocation = one decision cycle.

Modes:
  auto   - decide from the market clock: hourly cycle while open, one EOD
           cycle after close, otherwise exit quietly. (What the scheduler runs.)
  hourly / eod - forced, for testing.
  report - regenerate REPORT.md from stored state only.
"""
import json
import os
import uuid
from datetime import datetime, timedelta, timezone

from . import (benchmark, config, corporate_actions, data, db, fills, ledger,
               market_calendar as mc, metrics, report, signals, strategy,
               tax, universe)


def _utcnow():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


class Ctx:
    """Everything one run needs."""

    def __init__(self, mode, api=None, db_file=None):
        self.cfg = config.load()
        self.conn = db.connect(db_file or config.db_path())
        self.api = api or data.AlpacaData()
        self.now = mc.now_et()
        self.today = self.now.date().isoformat()
        self.run_id = f"{self.now.strftime('%Y%m%dT%H%M%S')}-{uuid.uuid4().hex[:6]}"
        self.mode = mode
        self.quotes = {}
        self.trades_made = 0
        self.ballast = self.cfg["risk"]["ballast_symbol"]

    def log(self, kind, symbol, detail, action=None):
        payload = json.dumps(detail, default=str)
        self.conn.execute(
            "INSERT INTO decisions(ts,run_id,kind,symbol,action,detail) "
            "VALUES(?,?,?,?,?,?)",
            (_utcnow(), self.run_id, kind, symbol, action, payload),
        )
        line = json.dumps({"ts": _utcnow(), "run_id": self.run_id, "kind": kind,
                           "symbol": symbol, "action": action, "detail": detail},
                          default=str)
        with open(os.path.join(config.state_dir(), "decisions.jsonl"), "a",
                  encoding="utf-8") as f:
            f.write(line + "\n")

    def price(self, sym):
        return (self.quotes.get(sym) or {}).get("last")

    def fetch_quotes(self, symbols):
        symbols = [s for s in set(symbols) if s and s not in self.quotes]
        if not symbols:
            return
        qs = self.api.latest_quotes(symbols)
        ts = self.api.latest_trades(symbols)
        for s in symbols:
            q = qs.get(s, {})
            q["last"] = (ts.get(s) or {}).get("price") or q.get("ask") or q.get("bid")
            self.quotes[s] = q

    def sig_liquidity(self, sym):
        """(adv_dollar, ann_vol) from the latest signals row, if any."""
        d = signals.latest_date(self.conn)
        if not d:
            return None, None
        row = self.conn.execute(
            "SELECT adv_dollar, ann_vol FROM signals WHERE signal_date=? AND symbol=?",
            (d, sym),
        ).fetchone()
        return (row["adv_dollar"], row["ann_vol"]) if row else (None, None)


def run(mode="auto", api=None, db_file=None):
    ctx = Ctx(mode, api=api, db_file=db_file)
    conn = ctx.conn
    try:
        if mode == "report":
            _regenerate_report(ctx)
            return "report"
        mc.sync(conn, ctx.api, ctx.today)
        resolved = _resolve_mode(ctx) if mode == "auto" else mode
        if resolved is None:
            _finish(ctx, "skipped", "market closed / nothing due")
            return "skipped"
        _bootstrap(ctx)
        if resolved == "hourly":
            _run_hourly(ctx)
        else:
            _run_eod(ctx)
        _finish(ctx, resolved, "ok")
        return resolved
    except Exception as e:
        conn.execute(
            "INSERT INTO runs(run_id,ts,mode,ok,message) VALUES(?,?,?,0,?)",
            (ctx.run_id, _utcnow(), mode, f"{type(e).__name__}: {e}"),
        )
        conn.commit()
        raise
    finally:
        conn.close()


def _finish(ctx, mode, message):
    ctx.conn.execute(
        "INSERT INTO runs(run_id,ts,mode,ok,message) VALUES(?,?,?,1,?)",
        (ctx.run_id, _utcnow(), mode, message),
    )
    ctx.conn.commit()


def _resolve_mode(ctx):
    sess = mc.session(ctx.conn, ctx.today)
    if sess:
        open_dt, close_dt = sess
        if open_dt <= ctx.now < close_dt:
            return "hourly"
        if ctx.now >= close_dt and db.get_meta(ctx.conn, "eod_done") != ctx.today:
            return "eod"
    return None


def _bootstrap(ctx):
    conn = ctx.conn
    if db.get_meta(conn, "inception") is None:
        ledger.deposit(conn, _utcnow(), ctx.today,
                       ctx.cfg["account"]["starting_cash"])
        db.set_meta(conn, "inception", ctx.today)
        db.set_meta(conn, "dd_state", "normal")
        ctx.log("system", None, {
            "event": "inception",
            "deposit": ctx.cfg["account"]["starting_cash"],
            "note": "simulated cash account funded; T+1 settlement, no margin",
        })


# ---------------------------------------------------------------- hourly ---

def _run_hourly(ctx):
    conn, cfg, today = ctx.conn, ctx.cfg, ctx.today
    ts = _utcnow()
    tax.expire_pending_washes(conn, today)

    positions = ledger.positions(conn)
    order_syms = [o["symbol"] for o in _open_orders(conn)]
    ctx.fetch_quotes(list(positions) + order_syms + [ctx.ballast])

    # 1. Corporate actions due (splits first — they change quantities).
    corporate_actions.apply_due(conn, ts, today, ctx.price, ctx.log)
    positions = ledger.positions(conn)

    # 2. Working orders (stops) against minute bars since the last check.
    _process_working_orders(ctx)
    positions = ledger.positions(conn)

    # 3. Daily signals (computed once per day, cached).
    prev_td = mc.prev_trading_day(conn, today)
    sig_date = signals.ensure(conn, ctx.api, cfg, today, prev_td)
    sigs = signals.get_all(conn, sig_date)

    # 4. Candidate quotes, portfolio valuation, drawdown state.
    scfg = cfg["signals"]
    candidates = [s["symbol"] for s in sigs.values()
                  if s["eligible"] and s["rank"] and s["rank"] <= scfg["entry_rank_max"]]
    ctx.fetch_quotes(candidates)
    equity, settled, reserve, pos_value = _valuation(ctx, positions)
    hwm = float(db.get_meta(conn, "hwm") or equity)
    dd = max(0.0, 1 - equity / hwm) if hwm > 0 else 0.0
    prev_state = db.get_meta(conn, "dd_state") or "normal"
    state = _maybe_resume(ctx, prev_state, equity)
    state_new = strategy.dd_state(state, dd, cfg)
    if state_new != state:
        ctx.log("system", None, {"event": "drawdown_state", "from": state,
                                 "to": state_new, "drawdown": round(dd, 4),
                                 "equity": equity, "hwm": hwm})
    db.set_meta(conn, "dd_state", state_new)
    state = state_new

    # 5. Halt: liquidate everything once, then do nothing until manual resume.
    if state == "halted":
        _liquidate_all(ctx, positions, reason=f"drawdown {dd:.1%} breached "
                       f"{cfg['risk']['drawdown_liquidate']:.0%} liquidation brake")
        _snapshot(ctx, "intraday")
        db.set_meta(conn, "last_hourly_ts", ts)
        return

    sector_of = universe.sector_map()

    # 6. Exits: rank decay / trend break, then halve-state shedding, trims.
    sells, holds = strategy.plan_exits(conn, cfg, sigs, positions, ctx.quotes,
                                       today, state, ctx.ballast)
    for h in holds:
        ctx.log("hold", h["symbol"], h["detail"], action="hold")
    selling = {s["symbol"] for s in sells}
    if state == "halve":
        sells += strategy.plan_halve_sells(cfg, sigs, positions, ctx.quotes,
                                           equity, ctx.ballast, selling)
    sells += strategy.plan_trims(cfg, positions, ctx.quotes, equity, ctx.ballast)
    for s in sells:
        _execute_sell(ctx, s["symbol"], s["qty"], "market", s["reason"],
                      s.get("detail"))
    if sells:
        positions = ledger.positions(conn)
        equity, settled, reserve, pos_value = _valuation(ctx, positions)

    # 7. Entries (only in 'normal' state; settled cash net of reserve+buffer).
    investable = settled - reserve - cfg["risk"]["min_cash_buffer_pct"] * equity
    new_today = conn.execute(
        "SELECT COUNT(DISTINCT symbol) AS n FROM trades WHERE trade_date=? "
        "AND side='buy' AND reason LIKE 'momentum entry%'", (today,),
    ).fetchone()["n"]
    buys, skips = strategy.plan_entries(conn, cfg, sigs, positions, ctx.quotes,
                                        sector_of, equity, max(0.0, investable),
                                        today, state, new_today, ctx.ballast)
    for sk in skips[:8]:
        ctx.log("no_trade", sk.get("symbol"), sk, action="skip_entry")
    for b in buys:
        _execute_buy(ctx, b["symbol"], b["qty"], b["reason"], b.get("detail"))
    if buys:
        positions = ledger.positions(conn)
        equity, settled, reserve, pos_value = _valuation(ctx, positions)

    # 8. Ballast rebalance toward its band.
    investable = settled - reserve - cfg["risk"]["min_cash_buffer_pct"] * equity
    bp = strategy.plan_ballast(cfg, positions, ctx.quotes, equity,
                               max(0.0, investable), state, ctx.ballast)
    if bp:
        if bp["side"] == "buy":
            _execute_buy(ctx, bp["symbol"], bp["qty"], bp["reason"])
        else:
            _execute_sell(ctx, bp["symbol"], bp["qty"], "market", bp["reason"])
        positions = ledger.positions(conn)

    # 9. Keep exactly one trailing stop per held stock.
    strategy.ensure_stop_orders(conn, cfg, ts, today, positions, ctx.quotes,
                                ctx.ballast)

    # 10. Benchmark starts on the first market-open run.
    if benchmark.ensure_started(conn, cfg, ctx.quotes.get(ctx.ballast, {}), ts):
        ctx.log("system", ctx.ballast,
                {"event": "benchmark_started",
                 "note": "SPY buy-and-hold benchmark funded with same $"})

    if ctx.trades_made == 0:
        ctx.log("no_trade", None, {
            "reason": "no signals crossed action thresholds this hour",
            "drawdown_state": state, "equity": equity,
            "settled_cash": settled, "positions": len(positions),
        })
    _snapshot(ctx, "intraday")
    # Keep the report and dashboard fresh every hour, not just at EOD.
    positions = ledger.positions(conn)
    report.generate(conn, cfg, {s: ctx.price(s) for s in positions}, today)
    db.set_meta(conn, "last_hourly_ts", ts)
    conn.commit()


def _open_orders(conn):
    return conn.execute("SELECT * FROM orders WHERE status='open'").fetchall()


def _process_working_orders(ctx):
    conn, cfg = ctx.conn, ctx.cfg
    orders = _open_orders(conn)
    if not orders:
        return
    sess = mc.session(conn, ctx.today)
    if sess is None:
        # Forced run outside a session (testing): no bars to scan, but still
        # evaluate stops against the current quotes.
        _evaluate_orders(ctx, orders, {})
        return
    open_dt = sess[0]
    last_ts = db.get_meta(conn, "last_hourly_ts")
    start = open_dt.astimezone(timezone.utc)
    if last_ts:
        prev = datetime.fromisoformat(last_ts)
        if prev.tzinfo is None:
            prev = prev.replace(tzinfo=timezone.utc)
        start = max(start, prev)
    end = datetime.now(timezone.utc) - timedelta(minutes=1)
    if end <= start:
        return
    syms = sorted({o["symbol"] for o in orders})
    bars = ctx.api.minute_bars(syms, start.isoformat().replace("+00:00", "Z"),
                               end.isoformat().replace("+00:00", "Z"))
    _evaluate_orders(ctx, orders, bars)


def _evaluate_orders(ctx, orders, bars):
    conn, cfg = ctx.conn, ctx.cfg
    for o in orders:
        q = ctx.quotes.get(o["symbol"]) or {}
        adv, vol = ctx.sig_liquidity(o["symbol"])
        obars = bars.get(o["symbol"]) or []
        if o["order_type"] == "stop":
            res = fills.evaluate_stop(o["side"], o["remaining_qty"],
                                      o["stop_price"], q, obars, adv, vol, cfg)
        else:
            res = fills.evaluate_limit(o["side"], o["remaining_qty"],
                                       o["limit_price"], q, obars, adv, vol, cfg)
        conn.execute("UPDATE orders SET last_checked_ts=? WHERE id=?",
                     (_utcnow(), o["id"]))
        if res.qty <= 0:
            continue
        if o["side"] == "sell":
            _apply_sell_fill(ctx, o["symbol"], res, o["order_type"],
                             o["reason"] or "working order", order_id=o["id"],
                             exempt_min_hold=True)
        else:
            _apply_buy_fill(ctx, o["symbol"], res, o["order_type"],
                            o["reason"] or "working order", order_id=o["id"])
        remaining = o["remaining_qty"] - res.qty
        conn.execute(
            "UPDATE orders SET remaining_qty=?, status=? WHERE id=?",
            (remaining, "filled" if remaining <= 1e-9 else "open", o["id"]),
        )


def _valuation(ctx, positions):
    conn, cfg = ctx.conn, ctx.cfg
    ctx.fetch_quotes(list(positions))
    pos_value = sum(p["qty"] * (ctx.price(s) or 0) for s, p in positions.items())
    settled = ledger.settled_cash(conn, ctx.today)
    total = ledger.total_cash(conn)
    reserve = tax.tax_reserve(conn, cfg)
    equity = round(total + pos_value - reserve, 2)
    return equity, settled, reserve, round(pos_value, 2)


def _maybe_resume(ctx, state, equity):
    """A committed state/RESUME file acknowledges a liquidation halt and
    restarts the strategy with the high-water mark reset to current equity."""
    flag = os.path.join(config.state_dir(), "RESUME")
    if state == "halted" and os.path.exists(flag):
        os.remove(flag)
        db.set_meta(ctx.conn, "hwm", equity)
        db.set_meta(ctx.conn, "halt_liquidated", "0")
        ctx.log("system", None, {"event": "manual_resume",
                                 "note": "RESUME flag found; HWM reset",
                                 "equity": equity})
        return "normal"
    return state


def _liquidate_all(ctx, positions, reason):
    conn = ctx.conn
    if db.get_meta(conn, "halt_liquidated") == "1":
        ctx.log("halt", None, {"reason": "halted; awaiting state/RESUME file",
                               "note": "no trading until manual resume"})
        return
    ctx.log("halt", None, {"event": "liquidation_brake", "reason": reason})
    for sym, pos in sorted(positions.items()):
        _execute_sell(ctx, sym, pos["qty"], "market",
                      f"liquidation brake: {reason}")
    conn.execute("UPDATE orders SET status='cancelled' WHERE status='open'")
    conn.execute("DELETE FROM position_state")
    db.set_meta(conn, "halt_liquidated", "1")


def _execute_buy(ctx, sym, qty, reason, detail=None):
    """Entry as a marketable limit: pays ask+impact but never above
    ask*(1+buffer) — bounds slippage on the way in."""
    cfg = ctx.cfg
    q = ctx.quotes.get(sym) or {}
    adv, vol = ctx.sig_liquidity(sym)
    res = fills.fill_market("buy", qty, q, adv, vol, None, cfg)
    if res.qty <= 0:
        ctx.log("no_trade", sym, {"reason": f"buy not filled: {res.note}"},
                action="entry_failed")
        return
    ask = q.get("ask") or q.get("last")
    limit = ask * (1 + cfg["fills"]["marketable_limit_buffer"])
    if res.price > limit:
        res.price = round(limit, 4)
    _apply_buy_fill(ctx, sym, res, "limit", reason, detail=detail)


def _apply_buy_fill(ctx, sym, res, order_type, reason, order_id=None, detail=None):
    conn, cfg, today = ctx.conn, ctx.cfg, ctx.today
    ts = _utcnow()
    # Hard invariant: never spend beyond settled cash net of the tax reserve.
    settled = ledger.settled_cash(conn, today)
    reserve = tax.tax_reserve(conn, cfg)
    max_notional = max(0.0, settled - reserve)
    if res.qty * res.price > max_notional:
        new_qty = int(max_notional // res.price)
        ctx.log("system", sym, {
            "event": "buy_downsized", "from_qty": res.qty, "to_qty": new_qty,
            "reason": "settled-cash constraint at execution time",
        })
        res.qty = new_qty
        if res.qty <= 0:
            return
    notional = round(res.qty * res.price, 2)
    cur = conn.execute(
        "INSERT INTO trades(ts,trade_date,symbol,side,qty,order_type,fill_price,"
        "notional,spread_cost,impact_cost,order_id,reason) "
        "VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",
        (ts, today, sym, "buy", res.qty, order_type, res.price, notional,
         res.spread_cost, res.impact_cost, order_id, reason),
    )
    trade_id = cur.lastrowid
    ledger.record_buy(conn, ts, today, sym, notional, trade_id)
    lot_id = ledger.open_lot(conn, ts, sym, today, res.qty, res.price)
    disallowed = tax.apply_wash_on_buy(conn, sym, today, lot_id)
    d = dict(detail or {})
    d.update({"reason": reason, "qty": res.qty, "price": res.price,
              "notional": notional, "spread_cost": res.spread_cost,
              "impact_cost": res.impact_cost, "fill_note": res.note})
    if disallowed:
        d["wash_sale"] = (f"${disallowed} of recent losses disallowed; "
                          f"added to this lot's basis")
    ctx.log("entry", sym, d, action="buy")
    ctx.trades_made += 1
    conn.commit()


def _execute_sell(ctx, sym, qty, order_type, reason, detail=None):
    cfg = ctx.cfg
    q = ctx.quotes.get(sym) or {}
    adv, vol = ctx.sig_liquidity(sym)
    res = fills.fill_market("sell", qty, q, adv, vol, None, cfg)
    if res.qty <= 0:
        ctx.log("no_trade", sym, {"reason": f"sell not filled: {res.note}"},
                action="exit_failed")
        return
    _apply_sell_fill(ctx, sym, res, order_type, reason, detail=detail)


def _apply_sell_fill(ctx, sym, res, order_type, reason, order_id=None,
                     detail=None, exempt_min_hold=False):
    conn, cfg, today = ctx.conn, ctx.cfg, ctx.today
    ts = _utcnow()
    held = ledger.position_qty(conn, sym)
    if res.qty > held:
        res.qty = held
    if res.qty <= 0:
        return
    proceeds = round(res.qty * res.price, 2)
    settle = mc.next_trading_day(conn, today)
    cur = conn.execute(
        "INSERT INTO trades(ts,trade_date,symbol,side,qty,order_type,fill_price,"
        "notional,spread_cost,impact_cost,order_id,reason) "
        "VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",
        (ts, today, sym, "sell", res.qty, order_type, res.price, proceeds,
         res.spread_cost, res.impact_cost, order_id, reason),
    )
    trade_id = cur.lastrowid
    ledger.record_sell(conn, ts, today, settle, sym, proceeds, trade_id)
    events = tax.realize_sale(conn, ts, today, sym, res.qty, proceeds, trade_id)
    if ledger.position_qty(conn, sym) <= 1e-9:
        conn.execute("DELETE FROM position_state WHERE symbol=?", (sym,))
        conn.execute(
            "UPDATE orders SET status='cancelled' WHERE symbol=? AND "
            "status='open' AND order_type='stop' AND id IS NOT ?",
            (sym, order_id),
        )
    d = dict(detail or {})
    d.update({"reason": reason, "qty": res.qty, "price": res.price,
              "proceeds": proceeds, "settles": settle,
              "spread_cost": res.spread_cost, "impact_cost": res.impact_cost,
              "fill_note": res.note,
              "realized": events})
    ctx.log("exit", sym, d, action="sell")
    ctx.trades_made += 1
    conn.commit()


def _snapshot(ctx, kind):
    conn = ctx.conn
    positions = ledger.positions(conn)
    equity, settled, reserve, pos_value = _valuation(ctx, positions)
    total = ledger.total_cash(conn)
    bench = benchmark.value(conn, ctx.price(ctx.ballast))
    conn.execute(
        "INSERT INTO equity_snapshots(ts,snap_date,kind,settled_cash,"
        "unsettled_cash,tax_reserve,positions_value,equity,benchmark_value) "
        "VALUES(?,?,?,?,?,?,?,?,?)",
        (_utcnow(), ctx.today, kind, settled, round(total - settled, 2),
         reserve, pos_value, equity, bench),
    )
    return equity


# ------------------------------------------------------------------- eod ---

def _run_eod(ctx):
    conn, cfg, today = ctx.conn, ctx.cfg, ctx.today
    ts = _utcnow()
    tax.expire_pending_washes(conn, today)
    positions = ledger.positions(conn)
    held = list(positions) + [ctx.ballast]
    ctx.fetch_quotes(held)

    # Corporate actions: refresh the forward window for held + benchmark.
    start = (datetime.now(timezone.utc) - timedelta(days=5)).date().isoformat()
    end = (datetime.now(timezone.utc) + timedelta(days=45)).date().isoformat()
    try:
        n = corporate_actions.fetch_and_store(conn, ctx.api, held, start, end)
        if n:
            ctx.log("system", None, {"event": "corporate_actions_synced",
                                     "new_rows": n})
    except data.AlpacaError as e:
        ctx.log("system", None, {"event": "corporate_actions_fetch_failed",
                                 "error": str(e),
                                 "note": "will retry next EOD run"})
    corporate_actions.apply_due(conn, ts, today, ctx.price, ctx.log)
    positions = ledger.positions(conn)

    # Trailing stops ratchet on closing prices (last trade after the bell).
    for sym in positions:
        if sym != ctx.ballast:
            strategy.update_trailing_stop(conn, cfg, sym, ctx.price(sym))

    # Benchmark dividends reinvest on pay date.
    events = benchmark.process_dividends(conn, cfg, today, ctx.price(ctx.ballast))
    for e in events:
        ctx.log("system", ctx.ballast, {"event": "benchmark_dividend", **e})

    equity = _snapshot(ctx, "eod")
    hwm = float(db.get_meta(conn, "hwm") or 0)
    if equity > hwm:
        db.set_meta(conn, "hwm", equity)

    last_prices = {s: ctx.price(s) for s in positions}
    report.generate(conn, cfg, last_prices, today)
    db.set_meta(conn, "eod_done", today)
    ctx.log("system", None, {"event": "eod_complete", "equity": equity,
                             "hwm": max(hwm, equity)})
    conn.commit()


def _regenerate_report(ctx):
    positions = ledger.positions(ctx.conn)
    ctx.fetch_quotes(list(positions) + [ctx.ballast])
    last_prices = {s: ctx.price(s) for s in positions}
    report.generate(ctx.conn, ctx.cfg, last_prices, ctx.today)
