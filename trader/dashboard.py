"""Interactive dashboard: docs/index.html, generated from the ledger and
served by GitHub Pages. Self-contained — the template embeds all data as
JSON, so the page needs no server or external requests."""
import json
import os
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

from . import config, db, ledger, metrics, tax, universe

ET = ZoneInfo("America/New_York")


def _et(ts_iso):
    """ISO UTC timestamp -> short ET display string."""
    try:
        dt = datetime.fromisoformat(ts_iso)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.astimezone(ET).strftime("%b %d, %I:%M %p")
    except ValueError:
        return ts_iso


def build_data(conn, cfg, last_prices, today):
    positions = ledger.positions(conn)
    settled = ledger.settled_cash(conn, today)
    total_cash = ledger.total_cash(conn)
    reserve = tax.tax_reserve(conn, cfg)
    pos_value = sum(p["qty"] * (last_prices.get(s) or 0)
                    for s, p in positions.items())
    equity = round(total_cash + pos_value - reserve, 2)
    start = cfg["account"]["starting_cash"]
    ballast = cfg["risk"]["ballast_symbol"]
    sectors = universe.sector_map()

    snaps = conn.execute(
        "SELECT ts, kind, equity, benchmark_value FROM equity_snapshots "
        "ORDER BY ts"
    ).fetchall()
    series = [{"t": r["ts"], "kind": r["kind"], "equity": r["equity"],
               "bench": r["benchmark_value"]} for r in snaps]

    pos_rows = []
    for sym in sorted(positions):
        p = positions[sym]
        last = last_prices.get(sym)
        value = round(p["qty"] * last, 2) if last else None
        unreal = round(value - p["basis"], 2) if value is not None else None
        st = conn.execute("SELECT stop_price FROM position_state WHERE symbol=?",
                          (sym,)).fetchone()
        pos_rows.append({
            "symbol": sym, "qty": p["qty"],
            "avg_basis": round(p["basis"] / p["qty"], 2),
            "last": last, "value": value, "unreal": unreal,
            "unreal_pct": round(unreal / p["basis"], 6) if unreal is not None and p["basis"] else None,
            "stop": round(st["stop_price"], 2) if st else None,
            "sector": "S&P 500 index" if sym == ballast else sectors.get(sym),
            "is_ballast": sym == ballast,
        })

    trades = []
    for t in conn.execute("SELECT * FROM trades ORDER BY id DESC").fetchall():
        realized = None
        if t["side"] == "sell":
            rr = conn.execute(
                "SELECT SUM(gain) g, SUM(basis) b, SUM(wash_disallowed) w, "
                "MAX(CASE term WHEN 'long' THEN 'long' ELSE 'short' END) term, "
                "MIN(open_date) od FROM realized WHERE trade_id=?",
                (t["id"],),
            ).fetchone()
            if rr and rr["g"] is not None:
                held = None
                try:
                    held = (datetime.fromisoformat(t["trade_date"])
                            - datetime.fromisoformat(rr["od"])).days
                except (TypeError, ValueError):
                    pass
                realized = {
                    "gain": round(rr["g"], 2),
                    "pct": round(rr["g"] / rr["b"], 6) if rr["b"] else None,
                    "wash": bool(rr["w"] and rr["w"] > 0),
                    "term": rr["term"] + "-term" if rr["term"] else None,
                    "held": held,
                }
        trades.append({
            "when": _et(t["ts"]), "side": t["side"], "symbol": t["symbol"],
            "qty": t["qty"], "price": t["fill_price"], "notional": t["notional"],
            "spread_cost": round(t["spread_cost"], 2),
            "impact_cost": round(t["impact_cost"], 2),
            "costs": round(t["spread_cost"] + t["impact_cost"], 2),
            "reason": t["reason"], "realized": realized,
        })

    decisions = []
    for d in conn.execute(
        "SELECT * FROM decisions WHERE kind IN "
        "('entry','exit','no_trade','halt','system','hold') "
        "ORDER BY id DESC LIMIT 60"
    ).fetchall():
        try:
            detail = json.loads(d["detail"])
            reason = (detail.get("reason") or detail.get("note")
                      or detail.get("event") or "")
        except (ValueError, TypeError):
            reason = ""
        decisions.append({"when": _et(d["ts"]), "kind": d["kind"],
                          "symbol": d["symbol"], "reason": reason})

    summary = tax.realized_summary(conn)
    years = []
    for yr in sorted(summary):
        wash = conn.execute(
            "SELECT COALESCE(SUM(wash_disallowed),0) w FROM realized "
            "WHERE substr(trade_date,1,4)=?", (yr,),
        ).fetchone()["w"]
        years.append({"year": yr, "st": round(summary[yr]["short"], 2),
                      "lt": round(summary[yr]["long"], 2),
                      "wash": round(wash, 2)})

    bench_row = conn.execute(
        "SELECT benchmark_value FROM equity_snapshots "
        "WHERE benchmark_value IS NOT NULL ORDER BY ts DESC LIMIT 1"
    ).fetchone()

    return {
        "generated": datetime.now(ET).strftime("%b %d, %Y %I:%M %p ET"),
        "inception": db.get_meta(conn, "inception"),
        "dd_state": db.get_meta(conn, "dd_state") or "normal",
        "account": {
            "equity": equity, "starting_cash": start,
            "total_return": round(equity / start - 1, 6),
            "settled": settled, "unsettled": round(total_cash - settled, 2),
            "tax_reserve": reserve, "positions_value": round(pos_value, 2),
        },
        "series": series,
        "metrics": metrics.compute(conn, cfg),
        "positions": pos_rows,
        "trades": trades,
        "decisions": decisions,
        "tax": {"years": years,
                "dividends": round(tax.dividends_received(conn), 2),
                "rates": {"st": cfg["tax"]["short_term_rate"],
                          "lt": cfg["tax"]["long_term_rate"],
                          "div": cfg["tax"]["dividend_rate"]}},
        "benchmark": {"value": bench_row["benchmark_value"] if bench_row else None},
    }


def generate(conn, cfg, last_prices, today):
    data = build_data(conn, cfg, last_prices, today)
    tpl_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "dashboard_template.html")
    with open(tpl_path, "r", encoding="utf-8") as f:
        tpl = f.read()
    payload = json.dumps(data, default=str).replace("</", "<\\/")
    html = tpl.replace("__DATA__", payload)
    out_dir = os.path.join(config.ROOT, "docs")
    os.makedirs(out_dir, exist_ok=True)
    out = os.path.join(out_dir, "index.html")
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    return out
