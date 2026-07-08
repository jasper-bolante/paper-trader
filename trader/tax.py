"""FIFO realization, wash-sale handling, and the tax reserve.

Model (documented in STRATEGY.md):
- Lots consumed strictly FIFO by (open_date, id).
- Term: long if held > 365 days measured from holding_period_start
  (which a wash-sale tack can push earlier than the purchase date).
- Wash sale, both directions:
    * At SALE time, a loss is matched against replacement shares bought in
      the prior 30 days that are still open and haven't absorbed a wash.
    * At BUY time, the new shares absorb any still-pending losses realized
      within the prior 30 days.
  A matched share's loss is disallowed, added to the replacement lot's
  basis, and the replacement lot's holding period is tacked back.
- Tax reserve: a standing liability (not a cash movement). Per calendar
  year, allowed ST and LT gains are netted per IRS ordering (net loss on
  one side offsets the other), taxed at the configured rates, with net
  losses carried forward. Dividends are taxed at the qualified rate.
  Equity and investable cash are both reduced by the reserve.
"""
from datetime import date, timedelta


def _d(s):
    return date.fromisoformat(s)


def _term(holding_start, sell_date):
    return "long" if (_d(sell_date) - _d(holding_start)).days > 365 else "short"


def realize_sale(conn, ts, trade_date, symbol, qty, total_proceeds, trade_id=None):
    """Consume lots FIFO for a sale. Returns list of realization dicts."""
    lots = conn.execute(
        "SELECT * FROM lots WHERE symbol=? AND qty_open > 1e-9 ORDER BY open_date, id",
        (symbol,),
    ).fetchall()
    available = sum(l["qty_open"] for l in lots)
    if qty > available + 1e-9:
        raise ValueError(f"sell {qty} {symbol} but only {available} held")

    per_share_proceeds = total_proceeds / qty
    remaining = qty
    events = []
    for lot in lots:
        if remaining <= 1e-9:
            break
        take = min(lot["qty_open"], remaining)
        remaining -= take
        conn.execute(
            "UPDATE lots SET qty_open = qty_open - ? WHERE id=?", (take, lot["id"])
        )
        basis = take * lot["basis_per_share"]
        proceeds = take * per_share_proceeds
        gain = proceeds - basis
        term = _term(lot["holding_period_start"], trade_date)

        wash_disallowed = 0.0
        wash_pending = 0.0
        if gain < -1e-9:
            per_share_loss = -gain / take
            matched = _match_replacements(
                conn, symbol, trade_date, take, per_share_loss,
                lot["holding_period_start"], exclude_lot_id=None,
            )
            wash_disallowed = round(matched * per_share_loss, 6)
            wash_pending = take - matched

        cur = conn.execute(
            "INSERT INTO realized(ts,trade_date,symbol,qty,open_date,"
            "holding_period_start,proceeds,basis,gain,wash_disallowed,"
            "wash_pending_qty,term,trade_id) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (ts, trade_date, symbol, take, lot["open_date"],
             lot["holding_period_start"], round(proceeds, 4), round(basis, 4),
             round(gain, 4), wash_disallowed, wash_pending, term, trade_id),
        )
        events.append({
            "realized_id": cur.lastrowid, "qty": take, "gain": round(gain, 2),
            "term": term, "wash_disallowed": round(wash_disallowed, 2),
        })
    return events


def _match_replacements(conn, symbol, sale_date, loss_qty, per_share_loss,
                        sold_holding_start, exclude_lot_id=None):
    """Match loss shares against replacement lots bought within the 30 days
    BEFORE the sale. Returns matched share count. Adjusts replacement lots."""
    window_start = (_d(sale_date) - timedelta(days=30)).isoformat()
    rows = conn.execute(
        "SELECT * FROM lots WHERE symbol=? AND source='buy' AND qty_open > 1e-9 "
        "AND open_date >= ? AND open_date <= ? ORDER BY open_date, id",
        (symbol, window_start, sale_date),
    ).fetchall()
    matched_total = 0.0
    remaining = loss_qty
    for lot in rows:
        if remaining <= 1e-9:
            break
        if exclude_lot_id is not None and lot["id"] == exclude_lot_id:
            continue
        capacity = lot["qty_open"] - lot["wash_absorbed_qty"]
        if capacity <= 1e-9:
            continue
        m = min(capacity, remaining)
        # Basis of replacement shares rises by the disallowed per-share loss.
        # Spread across the whole lot to keep one basis figure per lot.
        add_total = m * per_share_loss
        new_basis = lot["basis_per_share"] + add_total / lot["qty_open"]
        new_start = min(lot["holding_period_start"], sold_holding_start)
        conn.execute(
            "UPDATE lots SET basis_per_share=?, holding_period_start=?, "
            "wash_absorbed_qty = wash_absorbed_qty + ? WHERE id=?",
            (new_basis, new_start, m, lot["id"]),
        )
        matched_total += m
        remaining -= m
    return matched_total


def apply_wash_on_buy(conn, symbol, buy_date, lot_id):
    """After a purchase, absorb pending losses realized in the prior 30 days.
    Returns total newly disallowed loss (positive number)."""
    lot = conn.execute("SELECT * FROM lots WHERE id=?", (lot_id,)).fetchone()
    window_start = (_d(buy_date) - timedelta(days=30)).isoformat()
    pend = conn.execute(
        "SELECT * FROM realized WHERE symbol=? AND wash_pending_qty > 1e-9 "
        "AND trade_date >= ? AND trade_date <= ? ORDER BY trade_date, id",
        (symbol, window_start, buy_date),
    ).fetchall()
    capacity = lot["qty_open"] - lot["wash_absorbed_qty"]
    newly_disallowed = 0.0
    basis_add_total = 0.0
    holding_start = lot["holding_period_start"]
    absorbed = 0.0
    for r in pend:
        if capacity <= 1e-9:
            break
        per_share_loss = -r["gain"] / r["qty"]
        m = min(capacity, r["wash_pending_qty"])
        add = m * per_share_loss
        conn.execute(
            "UPDATE realized SET wash_pending_qty = wash_pending_qty - ?, "
            "wash_disallowed = wash_disallowed + ? WHERE id=?",
            (m, add, r["id"]),
        )
        holding_start = min(holding_start, r["holding_period_start"])
        basis_add_total += add
        newly_disallowed += add
        absorbed += m
        capacity -= m
    if absorbed > 0:
        conn.execute(
            "UPDATE lots SET basis_per_share = basis_per_share + ?/qty_open, "
            "holding_period_start=?, wash_absorbed_qty = wash_absorbed_qty + ? "
            "WHERE id=?",
            (basis_add_total, holding_start, absorbed, lot_id),
        )
    return round(newly_disallowed, 2)


def expire_pending_washes(conn, as_of_date):
    """Losses older than 30 days can no longer be washed; clear pending flags."""
    cutoff = (_d(as_of_date) - timedelta(days=31)).isoformat()
    conn.execute(
        "UPDATE realized SET wash_pending_qty = 0 "
        "WHERE wash_pending_qty > 0 AND trade_date < ?",
        (cutoff,),
    )


def realized_summary(conn):
    """Per-year allowed ST/LT nets. allowed = gain + wash_disallowed."""
    rows = conn.execute(
        "SELECT substr(trade_date,1,4) AS yr, term, "
        "SUM(gain + wash_disallowed) AS allowed, SUM(gain) AS economic "
        "FROM realized GROUP BY yr, term"
    ).fetchall()
    out = {}
    for r in rows:
        y = out.setdefault(r["yr"], {"short": 0.0, "long": 0.0,
                                     "economic_short": 0.0, "economic_long": 0.0})
        y[r["term"]] += r["allowed"]
        y["economic_" + r["term"]] += r["economic"]
    return out


def dividends_received(conn):
    row = conn.execute(
        "SELECT COALESCE(SUM(amount),0) AS s FROM cash_ledger WHERE type='dividend'"
    ).fetchone()
    return row["s"]


def tax_reserve(conn, cfg):
    """Standing tax liability across all sim years, with loss carryforward."""
    st_rate = cfg["tax"]["short_term_rate"]
    lt_rate = cfg["tax"]["long_term_rate"]
    div_rate = cfg["tax"]["dividend_rate"]
    summary = realized_summary(conn)
    st_carry = lt_carry = 0.0
    reserve = 0.0
    for yr in sorted(summary):
        st = summary[yr]["short"] + st_carry
        lt = summary[yr]["long"] + lt_carry
        # IRS ordering: a net loss on one side offsets the other side's gain.
        if st < 0 and lt > 0:
            offset = min(-st, lt)
            lt -= offset
            st += offset
        elif lt < 0 and st > 0:
            offset = min(-lt, st)
            st -= offset
            lt += offset
        reserve += st_rate * max(0.0, st) + lt_rate * max(0.0, lt)
        st_carry, lt_carry = min(0.0, st), min(0.0, lt)
    reserve += div_rate * max(0.0, dividends_received(conn))
    return round(max(0.0, reserve), 2)
