"""Trading decisions. Pure planning functions — the engine executes.

Risk framework (the confirmed "conservative-medium" definition):
- Permanent SPY ballast (~20%), stock sleeve of 10-15 momentum names.
- Max 10% of equity per position at purchase, max 25% per sector.
- 10% trailing stops off the highest close since entry.
- Drawdown brakes vs the equity high-water mark:
    >=7%  no new entries       >=12% halve the stock sleeve
    >=15% liquidate everything and halt until manual resume.
- Max 2 new positions/day, 3-trading-day minimum hold (stops exempt).
- Entries only spend settled cash net of the tax reserve and cash buffer.
"""
from . import ledger, market_calendar

MIN_ENTRY_NOTIONAL = 500.0  # skip entries too small to be meaningful

DD_ORDER = ["normal", "no_buys", "halve", "halted"]


def dd_state(prev_state, drawdown, cfg, hysteresis=0.02):
    """Drawdown state machine with hysteresis; 'halted' is sticky (manual)."""
    r = cfg["risk"]
    if prev_state == "halted" or drawdown >= r["drawdown_liquidate"]:
        return "halted"
    if drawdown >= r["drawdown_halve"]:
        return "halve"
    # De-escalation requires recovering `hysteresis` past the threshold,
    # so the state doesn't flap around a boundary.
    if prev_state == "halve" and drawdown >= r["drawdown_halve"] - hysteresis:
        return "halve"
    if drawdown >= r["drawdown_no_buys"]:
        return "no_buys"
    if prev_state in ("no_buys", "halve") and drawdown >= r["drawdown_no_buys"] - hysteresis:
        return "no_buys"
    return "normal"


def plan_exits(conn, cfg, sigs, positions, quotes, today, state, ballast_symbol):
    """Rank-decay and trend-break exits (stops are separate working orders).
    Returns (sells, holds) — every held name gets a logged decision."""
    r = cfg["risk"]
    scfg = cfg["signals"]
    sells, holds = [], []
    for sym, pos in positions.items():
        if sym == ballast_symbol:
            continue
        q = quotes.get(sym) or {}
        last = q.get("last")
        sig = sigs.get(sym)
        st = conn.execute("SELECT * FROM position_state WHERE symbol=?",
                          (sym,)).fetchone()
        entry_date = st["entry_date"] if st else today
        held_days = market_calendar.trading_days_between(conn, entry_date, today)
        detail = {
            "qty": pos["qty"], "last": last,
            "rank": sig["rank"] if sig else None,
            "ma_exit": sig["ma_exit"] if sig else None,
            "held_trading_days": held_days,
            "stop": st["stop_price"] if st else None,
        }
        reason = None
        if sig is None:
            detail["note"] = "no signal row (dropped from universe?) - holding"
        elif sig["rank"] is None or sig["rank"] > scfg["exit_rank_min"]:
            reason = f"momentum rank decayed ({sig['rank']} > {scfg['exit_rank_min']} or ineligible: {sig['veto_reason']})"
        elif last is not None and sig["ma_exit"] and last < sig["ma_exit"]:
            reason = f"trend break: {last} < 100DMA {sig['ma_exit']}"
        if reason and held_days < r["min_holding_days"]:
            detail["note"] = f"exit signal ({reason}) but min hold {r['min_holding_days']}d not met"
            reason = None
        if reason:
            sells.append({"symbol": sym, "qty": pos["qty"], "reason": reason,
                          "detail": detail})
        else:
            holds.append({"symbol": sym, "detail": detail})
    return sells, holds


def plan_halve_sells(cfg, sigs, positions, quotes, equity, ballast_symbol,
                     already_selling):
    """In 'halve' state: shed weakest-ranked names until the stock sleeve
    is at or below half its normal target."""
    r = cfg["risk"]
    sleeve_target = equity * (1 - r["ballast_target_pct"]) * 0.5
    holdings = []
    sleeve_value = 0.0
    for sym, pos in positions.items():
        if sym == ballast_symbol or sym in already_selling:
            continue
        last = (quotes.get(sym) or {}).get("last") or 0
        value = pos["qty"] * last
        sleeve_value += value
        rank = (sigs.get(sym) or {}).get("rank")
        holdings.append({"symbol": sym, "qty": pos["qty"], "value": value,
                         "rank": rank if rank is not None else 9999})
    sells = []
    holdings.sort(key=lambda h: -h["rank"])  # weakest first
    for h in holdings:
        if sleeve_value <= sleeve_target:
            break
        sells.append({"symbol": h["symbol"], "qty": h["qty"],
                      "reason": f"drawdown brake (halve): shedding weakest rank {h['rank']}",
                      "detail": {"sleeve_value": round(sleeve_value, 2),
                                 "sleeve_target": round(sleeve_target, 2)}})
        sleeve_value -= h["value"]
    return sells


def plan_entries(conn, cfg, sigs, positions, quotes, sector_of, equity,
                 investable, today, state, new_today, ballast_symbol):
    """Pick new entries. Returns (buys, skips) with reasons for both."""
    r, scfg = cfg["risk"], cfg["signals"]
    buys, skips = [], []
    if state != "normal":
        return buys, [{"symbol": None,
                       "reason": f"no entries: drawdown state '{state}'"}]
    held = {s for s in positions if s != ballast_symbol}
    slots = min(r["max_positions"] - len(held),
                r["max_new_positions_per_day"] - new_today)
    if slots <= 0:
        return buys, [{"symbol": None,
                       "reason": f"no entry slots (positions {len(held)}/{r['max_positions']}, "
                                 f"new today {new_today}/{r['max_new_positions_per_day']})"}]

    sector_value = {}
    for sym, pos in positions.items():
        if sym == ballast_symbol:
            continue
        last = (quotes.get(sym) or {}).get("last") or 0
        sec = sector_of.get(sym, "Unknown")
        sector_value[sec] = sector_value.get(sec, 0) + pos["qty"] * last

    candidates = sorted(
        (s for s in sigs.values()
         if s["eligible"] and s["rank"] and s["rank"] <= scfg["entry_rank_max"]
         and s["symbol"] not in held),
        key=lambda s: s["rank"],
    )
    base_size = equity * (1 - r["ballast_target_pct"]) / r["target_positions"]
    remaining = investable
    for sig in candidates:
        if len(buys) >= slots:
            break
        sym = sig["symbol"]
        q = quotes.get(sym) or {}
        ask = q.get("ask") or q.get("last")
        if not ask or ask <= 0:
            skips.append({"symbol": sym, "reason": "no quote available"})
            continue
        # Volatility-scaled sizing: shrink choppier names, modestly boost calm ones.
        vol_adj = max(0.6, min(1.2, 0.30 / sig["ann_vol"])) if sig["ann_vol"] else 1.0
        size = min(base_size * vol_adj, r["max_position_pct"] * equity, remaining)
        qty = int(size // ask)
        notional = qty * ask
        if qty < 1 or notional < MIN_ENTRY_NOTIONAL:
            skips.append({"symbol": sym, "rank": sig["rank"],
                          "reason": f"insufficient investable cash (size ${size:.0f}, "
                                    f"need >= ${MIN_ENTRY_NOTIONAL:.0f})"})
            continue
        sec = sector_of.get(sym, "Unknown")
        if sector_value.get(sec, 0) + notional > r["max_sector_pct"] * equity:
            skips.append({"symbol": sym, "rank": sig["rank"],
                          "reason": f"sector cap: {sec} would exceed "
                                    f"{r['max_sector_pct']:.0%} of equity"})
            continue
        buys.append({
            "symbol": sym, "qty": qty, "ask": ask,
            "reason": f"momentum entry: rank {sig['rank']}, "
                      f"mom {sig['momentum']:.3f}, vol {sig['ann_vol']:.0%}",
            "detail": {"rank": sig["rank"], "momentum": sig["momentum"],
                       "ann_vol": sig["ann_vol"], "vol_adj": round(vol_adj, 2),
                       "base_size": round(base_size, 2),
                       "notional": round(notional, 2), "sector": sec},
        })
        remaining -= notional
        sector_value[sec] = sector_value.get(sec, 0) + notional
    return buys, skips


def plan_ballast(cfg, positions, quotes, equity, investable, state, ballast_symbol):
    """Keep the permanent index ballast inside its band. Returns one order or None."""
    r = cfg["risk"]
    if state == "halted":
        return None
    q = quotes.get(ballast_symbol) or {}
    last, ask = q.get("last"), q.get("ask") or q.get("last")
    if not last or not ask:
        return None
    qty_held = positions.get(ballast_symbol, {}).get("qty", 0)
    value = qty_held * last
    frac = value / equity if equity > 0 else 0
    if frac < r["ballast_band_low"]:
        target = r["ballast_target_pct"] * equity
        buy_notional = min(target - value, investable)
        qty = int(buy_notional // ask)
        if qty >= 1 and qty * ask >= MIN_ENTRY_NOTIONAL:
            return {"side": "buy", "symbol": ballast_symbol, "qty": qty,
                    "reason": f"ballast rebalance: {frac:.1%} < band "
                              f"{r['ballast_band_low']:.0%}, buying toward "
                              f"{r['ballast_target_pct']:.0%}"}
    elif frac > r["ballast_band_high"]:
        target = r["ballast_target_pct"] * equity
        qty = int((value - target) // last)
        if qty >= 1:
            return {"side": "sell", "symbol": ballast_symbol, "qty": qty,
                    "reason": f"ballast rebalance: {frac:.1%} > band "
                              f"{r['ballast_band_high']:.0%}, trimming toward "
                              f"{r['ballast_target_pct']:.0%}"}
    return None


def plan_trims(cfg, positions, quotes, equity, ballast_symbol):
    """Trim any single position that has grown past the trim threshold."""
    r = cfg["risk"]
    trims = []
    for sym, pos in positions.items():
        if sym == ballast_symbol:
            continue
        last = (quotes.get(sym) or {}).get("last")
        if not last:
            continue
        value = pos["qty"] * last
        if value > r["trim_position_pct"] * equity:
            target = r["max_position_pct"] * equity
            qty = int((value - target) // last)
            if qty >= 1:
                trims.append({"symbol": sym, "qty": qty,
                              "reason": f"position {value/equity:.1%} of equity "
                                        f"exceeds trim threshold "
                                        f"{r['trim_position_pct']:.0%}; trimming "
                                        f"back to {r['max_position_pct']:.0%}"})
    return trims


def ensure_stop_orders(conn, cfg, ts, today, positions, quotes, ballast_symbol):
    """Every held stock keeps exactly one open stop-sell at its trailing
    stop. Creates/updates position_state and stop orders to match."""
    r = cfg["risk"]
    for sym, pos in positions.items():
        if sym == ballast_symbol:
            continue
        last = (quotes.get(sym) or {}).get("last")
        st = conn.execute("SELECT * FROM position_state WHERE symbol=?",
                          (sym,)).fetchone()
        if st is None:
            seed = last or (pos["basis"] / pos["qty"])
            stop = seed * (1 - r["trailing_stop_pct"])
            conn.execute(
                "INSERT INTO position_state(symbol,entry_date,highest_close,"
                "stop_price) VALUES(?,?,?,?)", (sym, today, seed, stop),
            )
        else:
            stop = st["stop_price"]
        order = conn.execute(
            "SELECT * FROM orders WHERE symbol=? AND order_type='stop' "
            "AND status='open'", (sym,),
        ).fetchone()
        if order is None:
            conn.execute(
                "INSERT INTO orders(created_ts,created_date,symbol,side,qty,"
                "remaining_qty,order_type,stop_price,reason) "
                "VALUES(?,?,?,?,?,?,?,?,?)",
                (ts, today, sym, "sell", pos["qty"], pos["qty"], "stop", stop,
                 f"trailing stop {r['trailing_stop_pct']:.0%}"),
            )
        elif abs(order["remaining_qty"] - pos["qty"]) > 1e-9 \
                or abs((order["stop_price"] or 0) - stop) > 1e-6:
            conn.execute(
                "UPDATE orders SET qty=?, remaining_qty=?, stop_price=? WHERE id=?",
                (pos["qty"], pos["qty"], stop, order["id"]),
            )
    # Cancel stops for symbols no longer held.
    for o in conn.execute(
        "SELECT * FROM orders WHERE order_type='stop' AND status='open'"
    ).fetchall():
        if o["symbol"] not in positions or positions[o["symbol"]]["qty"] <= 1e-9:
            conn.execute("UPDATE orders SET status='cancelled' WHERE id=?",
                         (o["id"],))
            conn.execute("DELETE FROM position_state WHERE symbol=?",
                         (o["symbol"],))


def update_trailing_stop(conn, cfg, symbol, close):
    st = conn.execute("SELECT * FROM position_state WHERE symbol=?",
                      (symbol,)).fetchone()
    if st is None or close is None:
        return
    hi = max(st["highest_close"], close)
    stop = hi * (1 - cfg["risk"]["trailing_stop_pct"])
    conn.execute(
        "UPDATE position_state SET highest_close=?, stop_price=? WHERE symbol=?",
        (hi, stop, symbol),
    )
    conn.execute(
        "UPDATE orders SET stop_price=? WHERE symbol=? AND order_type='stop' "
        "AND status='open'", (stop, symbol),
    )
