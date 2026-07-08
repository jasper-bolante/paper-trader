"""Trading calendar cached in the DB from Alpaca's /v2/calendar endpoint
(covers US market holidays and early closes). The engine refuses to trade
on dates the cache doesn't cover — better to skip a run than to guess."""
from datetime import date, datetime, timedelta
from zoneinfo import ZoneInfo

ET = ZoneInfo("America/New_York")


def now_et():
    return datetime.now(tz=ET)


def sync(conn, api, today_iso, horizon_days=45, backfill_days=10):
    """Ensure the calendar cache covers [today - backfill, today + horizon]."""
    start = (date.fromisoformat(today_iso) - timedelta(days=backfill_days)).isoformat()
    end = (date.fromisoformat(today_iso) + timedelta(days=horizon_days)).isoformat()
    have = conn.execute(
        "SELECT COUNT(*) AS n FROM calendar WHERE date >= ? AND date <= ?",
        (today_iso, end),
    ).fetchone()["n"]
    # ~2/3 of calendar days are trading days; refresh if the tail looks thin.
    if have >= horizon_days * 0.5:
        return
    for day in api.calendar(start, end):
        conn.execute(
            "INSERT INTO calendar(date, open_time, close_time) VALUES(?,?,?) "
            "ON CONFLICT(date) DO UPDATE SET open_time=excluded.open_time, "
            "close_time=excluded.close_time",
            (day["date"], day["open"], day["close"]),
        )
    conn.commit()


def session(conn, date_iso):
    """(open_dt, close_dt) as aware ET datetimes, or None if not a trading day."""
    row = conn.execute(
        "SELECT * FROM calendar WHERE date=?", (date_iso,)
    ).fetchone()
    if not row:
        return None
    d = date.fromisoformat(date_iso)
    oh, om = map(int, row["open_time"].split(":"))
    ch, cm = map(int, row["close_time"].split(":"))
    return (
        datetime(d.year, d.month, d.day, oh, om, tzinfo=ET),
        datetime(d.year, d.month, d.day, ch, cm, tzinfo=ET),
    )


def is_trading_day(conn, date_iso):
    return session(conn, date_iso) is not None


def covers(conn, date_iso):
    """True if the cache extends to/beyond this date (so a miss means
    'holiday/weekend', not 'never synced')."""
    row = conn.execute("SELECT MAX(date) AS m FROM calendar").fetchone()
    return row["m"] is not None and row["m"] >= date_iso


def next_trading_day(conn, date_iso):
    row = conn.execute(
        "SELECT MIN(date) AS d FROM calendar WHERE date > ?", (date_iso,)
    ).fetchone()
    if row["d"] is None:
        raise RuntimeError(f"calendar cache exhausted after {date_iso}")
    return row["d"]


def prev_trading_day(conn, date_iso):
    row = conn.execute(
        "SELECT MAX(date) AS d FROM calendar WHERE date < ?", (date_iso,)
    ).fetchone()
    return row["d"]


def trading_days_between(conn, start_iso, end_iso):
    """Count of trading days in (start, end] — used for min-holding checks."""
    row = conn.execute(
        "SELECT COUNT(*) AS n FROM calendar WHERE date > ? AND date <= ?",
        (start_iso, end_iso),
    ).fetchone()
    return row["n"]
