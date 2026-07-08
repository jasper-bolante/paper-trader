"""Cash ledger with T+1 settlement, and positions derived from tax lots.

Rules enforced here:
- Buys only ever spend SETTLED cash (stricter than a real cash account,
  which would merely forbid selling before the funding sale settles).
- Sale proceeds settle the next trading day (T+1).
- Dividends settle on their pay date.
"""


def deposit(conn, ts, trade_date, amount, memo="initial deposit"):
    conn.execute(
        "INSERT INTO cash_ledger(ts,trade_date,settle_date,type,amount,memo) "
        "VALUES(?,?,?,?,?,?)",
        (ts, trade_date, trade_date, "deposit", round(amount, 2), memo),
    )


def record_buy(conn, ts, trade_date, symbol, notional, trade_id=None):
    conn.execute(
        "INSERT INTO cash_ledger(ts,trade_date,settle_date,type,amount,symbol,related_id) "
        "VALUES(?,?,?,?,?,?,?)",
        (ts, trade_date, trade_date, "buy", -round(notional, 2), symbol, trade_id),
    )


def record_sell(conn, ts, trade_date, settle_date, symbol, proceeds, trade_id=None):
    """Sale proceeds credit the ledger but only settle at T+1 (settle_date)."""
    conn.execute(
        "INSERT INTO cash_ledger(ts,trade_date,settle_date,type,amount,symbol,related_id) "
        "VALUES(?,?,?,?,?,?,?)",
        (ts, trade_date, settle_date, "sell", round(proceeds, 2), symbol, trade_id),
    )


def record_dividend(conn, ts, trade_date, pay_date, symbol, amount, memo=None):
    conn.execute(
        "INSERT INTO cash_ledger(ts,trade_date,settle_date,type,amount,symbol,memo) "
        "VALUES(?,?,?,?,?,?,?)",
        (ts, trade_date, pay_date, "dividend", round(amount, 2), symbol, memo),
    )


def record_cash_in_lieu(conn, ts, trade_date, symbol, amount, memo=None):
    conn.execute(
        "INSERT INTO cash_ledger(ts,trade_date,settle_date,type,amount,symbol,memo) "
        "VALUES(?,?,?,?,?,?,?)",
        (ts, trade_date, trade_date, "cash_in_lieu", round(amount, 2), symbol, memo),
    )


def settled_cash(conn, as_of_date):
    row = conn.execute(
        "SELECT COALESCE(SUM(amount),0) AS s FROM cash_ledger WHERE settle_date <= ?",
        (as_of_date,),
    ).fetchone()
    return round(row["s"], 2)


def total_cash(conn):
    row = conn.execute("SELECT COALESCE(SUM(amount),0) AS s FROM cash_ledger").fetchone()
    return round(row["s"], 2)


def unsettled_cash(conn, as_of_date):
    return round(total_cash(conn) - settled_cash(conn, as_of_date), 2)


def open_lot(conn, ts, symbol, open_date, qty, basis_per_share, source="buy"):
    cur = conn.execute(
        "INSERT INTO lots(symbol,open_date,holding_period_start,qty_open,qty_orig,"
        "basis_per_share,source,created_ts) VALUES(?,?,?,?,?,?,?,?)",
        (symbol, open_date, open_date, qty, qty, basis_per_share, source, ts),
    )
    return cur.lastrowid


def open_lots(conn, symbol=None):
    q = "SELECT * FROM lots WHERE qty_open > 1e-9"
    args = ()
    if symbol:
        q += " AND symbol=?"
        args = (symbol,)
    q += " ORDER BY open_date, id"
    return conn.execute(q, args).fetchall()


def positions(conn):
    """{symbol: {qty, basis}} from open lots."""
    rows = conn.execute(
        "SELECT symbol, SUM(qty_open) AS qty, SUM(qty_open*basis_per_share) AS basis "
        "FROM lots WHERE qty_open > 1e-9 GROUP BY symbol"
    ).fetchall()
    return {
        r["symbol"]: {"qty": r["qty"], "basis": round(r["basis"], 2)} for r in rows
    }


def position_qty(conn, symbol):
    row = conn.execute(
        "SELECT COALESCE(SUM(qty_open),0) AS q FROM lots WHERE symbol=? AND qty_open > 1e-9",
        (symbol,),
    ).fetchone()
    return row["q"]
