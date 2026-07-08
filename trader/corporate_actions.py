"""Dividends and splits on held positions.

- Splits apply on the ex-date: lot quantities scale by the ratio, per-share
  basis scales inversely (total basis unchanged), trailing-stop state and
  open stop orders are rescaled, and any fractional residue is paid out as
  cash-in-lieu at the post-split price.
- Cash dividends accrue when first seen on/after the ex-date for the
  quantity held at that moment, and the cash SETTLES on the pay date.
  (Approximation: intraday timing of ex-date holdings; positions turn over
  slowly enough that this is minor. Documented in STRATEGY.md.)
"""
import json
import math

from . import ledger


def fetch_and_store(conn, api, symbols, start, end):
    if not symbols:
        return 0
    rows = api.corporate_actions(sorted(symbols), start, end)
    n = 0
    for r in rows:
        cur = conn.execute(
            "INSERT OR IGNORE INTO corporate_actions"
            "(symbol,type,ex_date,pay_date,rate,raw) VALUES(?,?,?,?,?,?)",
            (r["symbol"], r["type"], r["ex_date"], r["pay_date"], r["rate"],
             json.dumps(r["raw"], default=str)),
        )
        n += cur.rowcount
    return n


def apply_due(conn, ts, today, get_price, log):
    """Apply unapplied actions with ex_date <= today for held symbols.
    get_price(symbol) -> last trade price (post-split market price).
    log(kind, symbol, detail_dict) records the decision trail."""
    applied = []
    rows = conn.execute(
        "SELECT * FROM corporate_actions WHERE applied=0 AND ex_date <= ? "
        "ORDER BY ex_date, id",
        (today,),
    ).fetchall()
    for ca in rows:
        sym = ca["symbol"]
        qty = ledger.position_qty(conn, sym)
        if qty <= 1e-9:
            # Not held (or no longer held): nothing to apply, retire the row.
            conn.execute("UPDATE corporate_actions SET applied=1 WHERE id=?",
                         (ca["id"],))
            continue
        if ca["type"] in ("forward_split", "reverse_split"):
            _apply_split(conn, ts, today, ca, get_price, log)
        elif ca["type"] == "cash_dividend":
            amount = round(qty * ca["rate"], 2)
            pay = ca["pay_date"] or today
            ledger.record_dividend(conn, ts, today, pay, sym, amount,
                                   memo=f"{ca['rate']}/sh x {qty}")
            log("system", sym, {
                "event": "dividend", "rate": ca["rate"], "qty": qty,
                "amount": amount, "ex_date": ca["ex_date"], "pay_date": pay,
                "note": "cash settles on pay date; 15% dividend tax reserved",
            })
            conn.execute("UPDATE corporate_actions SET applied=1 WHERE id=?",
                         (ca["id"],))
        applied.append((sym, ca["type"]))
    return applied


def _apply_split(conn, ts, today, ca, get_price, log):
    sym, ratio = ca["symbol"], ca["rate"]
    if not ratio or ratio <= 0:
        conn.execute("UPDATE corporate_actions SET applied=1 WHERE id=?", (ca["id"],))
        return
    lots = conn.execute(
        "SELECT * FROM lots WHERE symbol=? AND qty_open > 1e-9 ORDER BY open_date, id",
        (sym,),
    ).fetchall()
    for lot in lots:
        conn.execute(
            "UPDATE lots SET qty_open = qty_open * ?, qty_orig = qty_orig * ?, "
            "basis_per_share = basis_per_share / ?, "
            "wash_absorbed_qty = wash_absorbed_qty * ? WHERE id=?",
            (ratio, ratio, ratio, ratio, lot["id"]),
        )
    # Sell off any fractional residue as cash-in-lieu at the post-split price.
    total = ledger.position_qty(conn, sym)
    frac = total - math.floor(total)
    cil = 0.0
    if frac > 1e-9:
        px = get_price(sym) or 0.0
        cil = round(frac * px, 2)
        last_lot = conn.execute(
            "SELECT * FROM lots WHERE symbol=? AND qty_open > 1e-9 "
            "ORDER BY open_date DESC, id DESC LIMIT 1", (sym,),
        ).fetchone()
        conn.execute("UPDATE lots SET qty_open = qty_open - ? WHERE id=?",
                     (frac, last_lot["id"]))
        if cil > 0:
            ledger.record_cash_in_lieu(conn, ts, today, sym, cil,
                                       memo=f"split {ratio}: fractional {frac:.4f}")
    # Rescale trailing-stop state and open stop orders.
    conn.execute(
        "UPDATE position_state SET highest_close = highest_close / ?, "
        "stop_price = stop_price / ? WHERE symbol=?", (ratio, ratio, sym),
    )
    conn.execute(
        "UPDATE orders SET qty = qty * ?, remaining_qty = remaining_qty * ?, "
        "stop_price = CASE WHEN stop_price IS NULL THEN NULL ELSE stop_price / ? END, "
        "limit_price = CASE WHEN limit_price IS NULL THEN NULL ELSE limit_price / ? END "
        "WHERE symbol=? AND status='open'", (ratio, ratio, ratio, ratio, sym),
    )
    conn.execute("UPDATE corporate_actions SET applied=1 WHERE id=?", (ca["id"],))
    log("system", sym, {
        "event": ca["type"], "ratio": ratio, "new_qty": ledger.position_qty(conn, sym),
        "cash_in_lieu": cil, "ex_date": ca["ex_date"],
    })
