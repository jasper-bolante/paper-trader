"""SQLite persistence. One file, state/trader.db, committed to git each run.

Money convention: cash amounts are rounded to cents at ledger boundaries;
per-share basis keeps full float precision. Dates are ISO strings in
America/New_York market time; timestamps are ISO UTC.
"""
import sqlite3

SCHEMA = """
CREATE TABLE IF NOT EXISTS meta (
    key TEXT PRIMARY KEY,
    value TEXT
);

-- Every cash movement. Settled cash as-of date D = SUM(amount) over rows
-- with settle_date <= D. Buys debit with settle_date = trade date (we never
-- spend unsettled funds); sale proceeds credit with settle_date = T+1.
CREATE TABLE IF NOT EXISTS cash_ledger (
    id INTEGER PRIMARY KEY,
    ts TEXT NOT NULL,
    trade_date TEXT NOT NULL,
    settle_date TEXT NOT NULL,
    type TEXT NOT NULL,             -- deposit|buy|sell|dividend|cash_in_lieu|fee
    amount REAL NOT NULL,           -- signed, positive = cash in
    symbol TEXT,
    memo TEXT,
    related_id INTEGER
);

-- Tax lots. FIFO consumption keyed on (open_date, id). A wash-sale
-- adjustment raises basis_per_share and back-dates holding_period_start;
-- wash_absorbed_qty marks replacement shares already used by a wash match
-- so the same share can never absorb two disallowed losses.
CREATE TABLE IF NOT EXISTS lots (
    id INTEGER PRIMARY KEY,
    symbol TEXT NOT NULL,
    open_date TEXT NOT NULL,            -- actual purchase date (wash-sale window uses this)
    holding_period_start TEXT NOT NULL, -- may be earlier than open_date after a wash tack
    qty_open REAL NOT NULL,
    qty_orig REAL NOT NULL,
    basis_per_share REAL NOT NULL,
    wash_absorbed_qty REAL NOT NULL DEFAULT 0,
    source TEXT NOT NULL DEFAULT 'buy', -- buy|split
    created_ts TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS trades (
    id INTEGER PRIMARY KEY,
    ts TEXT NOT NULL,
    trade_date TEXT NOT NULL,
    symbol TEXT NOT NULL,
    side TEXT NOT NULL,             -- buy|sell
    qty REAL NOT NULL,
    order_type TEXT NOT NULL,       -- market|limit|stop
    fill_price REAL NOT NULL,
    notional REAL NOT NULL,
    spread_cost REAL NOT NULL DEFAULT 0,
    impact_cost REAL NOT NULL DEFAULT 0,
    order_id INTEGER,
    reason TEXT
);

-- Working orders that persist across hourly runs (resting limits, stops).
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY,
    created_ts TEXT NOT NULL,
    created_date TEXT NOT NULL,
    symbol TEXT NOT NULL,
    side TEXT NOT NULL,
    qty REAL NOT NULL,
    remaining_qty REAL NOT NULL,
    order_type TEXT NOT NULL,       -- limit|stop
    limit_price REAL,
    stop_price REAL,
    status TEXT NOT NULL DEFAULT 'open',  -- open|filled|cancelled|expired
    reason TEXT,
    last_checked_ts TEXT
);

-- Realization events (per consumed lot slice).
CREATE TABLE IF NOT EXISTS realized (
    id INTEGER PRIMARY KEY,
    ts TEXT NOT NULL,
    trade_date TEXT NOT NULL,
    symbol TEXT NOT NULL,
    qty REAL NOT NULL,
    open_date TEXT NOT NULL,
    holding_period_start TEXT NOT NULL,
    proceeds REAL NOT NULL,
    basis REAL NOT NULL,
    gain REAL NOT NULL,             -- economic gain before wash adjustment
    wash_disallowed REAL NOT NULL DEFAULT 0,  -- portion of loss disallowed (positive number)
    wash_pending_qty REAL NOT NULL DEFAULT 0, -- loss shares not yet matched to a replacement buy
    term TEXT NOT NULL,             -- short|long
    trade_id INTEGER
);

-- Per-position strategy state (trailing stop bookkeeping).
CREATE TABLE IF NOT EXISTS position_state (
    symbol TEXT PRIMARY KEY,
    entry_date TEXT NOT NULL,
    highest_close REAL NOT NULL,
    stop_price REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS equity_snapshots (
    id INTEGER PRIMARY KEY,
    ts TEXT NOT NULL,
    snap_date TEXT NOT NULL,
    kind TEXT NOT NULL,             -- intraday|eod
    settled_cash REAL NOT NULL,
    unsettled_cash REAL NOT NULL,
    tax_reserve REAL NOT NULL,
    positions_value REAL NOT NULL,
    equity REAL NOT NULL,           -- cash + positions - tax_reserve
    benchmark_value REAL,
    note TEXT
);

-- Full reasoning log for every evaluation, including no-trade decisions.
CREATE TABLE IF NOT EXISTS decisions (
    id INTEGER PRIMARY KEY,
    ts TEXT NOT NULL,
    run_id TEXT NOT NULL,
    kind TEXT NOT NULL,             -- entry|exit|hold|no_trade|halt|system
    symbol TEXT,
    action TEXT,
    detail TEXT NOT NULL            -- JSON blob with the full reasoning
);

CREATE TABLE IF NOT EXISTS corporate_actions (
    id INTEGER PRIMARY KEY,
    symbol TEXT NOT NULL,
    type TEXT NOT NULL,             -- cash_dividend|forward_split|reverse_split
    ex_date TEXT NOT NULL,
    pay_date TEXT,
    rate REAL NOT NULL,             -- $/share for dividends, new/old ratio for splits
    applied INTEGER NOT NULL DEFAULT 0,
    raw TEXT,
    UNIQUE(symbol, type, ex_date)
);

CREATE TABLE IF NOT EXISTS calendar (
    date TEXT PRIMARY KEY,          -- trading days only
    open_time TEXT NOT NULL,        -- HH:MM ET
    close_time TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS signals (
    signal_date TEXT NOT NULL,
    symbol TEXT NOT NULL,
    momentum REAL,
    rank INTEGER,
    price REAL,
    ma_trend REAL,
    ma_trend_rising INTEGER,
    ma_exit REAL,
    adv_dollar REAL,
    ann_vol REAL,
    eligible INTEGER NOT NULL,
    veto_reason TEXT,
    PRIMARY KEY (signal_date, symbol)
);

CREATE TABLE IF NOT EXISTS runs (
    id INTEGER PRIMARY KEY,
    run_id TEXT NOT NULL,
    ts TEXT NOT NULL,
    mode TEXT NOT NULL,
    ok INTEGER NOT NULL,
    message TEXT
);
"""


def connect(path):
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA foreign_keys=ON")
    conn.executescript(SCHEMA)
    return conn


def get_meta(conn, key, default=None):
    row = conn.execute("SELECT value FROM meta WHERE key=?", (key,)).fetchone()
    return row["value"] if row else default


def set_meta(conn, key, value):
    conn.execute(
        "INSERT INTO meta(key,value) VALUES(?,?) "
        "ON CONFLICT(key) DO UPDATE SET value=excluded.value",
        (key, str(value)),
    )
