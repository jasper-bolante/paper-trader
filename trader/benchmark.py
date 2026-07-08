"""Buy-and-hold S&P 500 benchmark: the same $20,000 put into SPY at
inception (paying the spread), dividends reinvested net of the 15%
dividend tax. Fractional shares allowed — it's a yardstick, not a
tradable account. Never sold, so no realization taxes apply."""
import json

from . import db


def ensure_started(conn, cfg, quote, ts):
    if db.get_meta(conn, "bench_shares") is not None:
        return False
    ask = quote.get("ask") or quote.get("last")
    if not ask or ask <= 0:
        return False
    cash = cfg["account"]["starting_cash"]
    shares = cash / ask
    db.set_meta(conn, "bench_shares", repr(shares))
    db.set_meta(conn, "bench_started", ts)
    db.set_meta(conn, "bench_ca_applied", "[]")
    return True


def process_dividends(conn, cfg, today, spy_price):
    """Reinvest benchmark-symbol dividends whose pay date has arrived."""
    shares_s = db.get_meta(conn, "bench_shares")
    if shares_s is None or not spy_price:
        return []
    shares = float(shares_s)
    applied = set(json.loads(db.get_meta(conn, "bench_ca_applied") or "[]"))
    sym = cfg["benchmark"]["symbol"]
    started = (db.get_meta(conn, "bench_started") or "")[:10]
    rows = conn.execute(
        "SELECT * FROM corporate_actions WHERE symbol=? AND type='cash_dividend' "
        "AND pay_date IS NOT NULL AND pay_date <= ? AND ex_date >= ? ORDER BY id",
        (sym, today, started),
    ).fetchall()
    events = []
    for r in rows:
        if r["id"] in applied:
            continue
        gross = shares * r["rate"]
        net = gross * (1 - cfg["tax"]["dividend_rate"])
        shares += net / spy_price
        applied.add(r["id"])
        events.append({"ex_date": r["ex_date"], "rate": r["rate"],
                       "net_reinvested": round(net, 2)})
    db.set_meta(conn, "bench_shares", repr(shares))
    db.set_meta(conn, "bench_ca_applied", json.dumps(sorted(applied)))
    return events


def value(conn, spy_price):
    shares_s = db.get_meta(conn, "bench_shares")
    if shares_s is None or not spy_price:
        return None
    return round(float(shares_s) * spy_price, 2)
