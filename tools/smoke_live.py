"""Live smoke test of the Alpaca data layer. Read-only; verifies every
endpoint the engine depends on and prints what came back.
    python tools/smoke_live.py   (needs ALPACA_API_KEY_ID / _SECRET_KEY env)
"""
import sys
from datetime import date, datetime, timedelta, timezone

sys.path.insert(0, ".")
from trader.data import AlpacaData  # noqa: E402

api = AlpacaData()
ok = True


def check(name, fn):
    global ok
    try:
        out = fn()
        print(f"[PASS] {name}: {out}")
    except Exception as e:
        ok = False
        print(f"[FAIL] {name}: {type(e).__name__}: {e}")


check("clock", lambda: api.clock())
today = date.today()
check("calendar", lambda: api.calendar((today - timedelta(days=5)).isoformat(),
                                       (today + timedelta(days=10)).isoformat())[:3])
check("latest_quotes", lambda: api.latest_quotes(["AAPL", "SPY", "BRK.B"]))
check("latest_trades", lambda: api.latest_trades(["AAPL", "SPY"]))


def _daily():
    start = (today - timedelta(days=40)).isoformat() + "T00:00:00Z"
    end = (today - timedelta(days=1)).isoformat() + "T23:59:59Z"
    bars = api.daily_bars(["AAPL", "MSFT"], start, end)
    return {s: (len(b), b[-1] if b else None) for s, b in bars.items()}


check("daily_bars", _daily)


def _minute():
    end = datetime.now(timezone.utc) - timedelta(minutes=16)
    start = end - timedelta(hours=26)
    bars = api.minute_bars(["AAPL"], start.isoformat().replace("+00:00", "Z"),
                           end.isoformat().replace("+00:00", "Z"))
    return {s: (len(b), b[-1] if b else None) for s, b in bars.items()}


check("minute_bars", _minute)


def _ca():
    rows = api.corporate_actions(["AAPL", "MSFT", "KO", "SPY", "NVDA"],
                                 (today - timedelta(days=90)).isoformat(),
                                 (today + timedelta(days=30)).isoformat())
    return f"{len(rows)} actions, e.g. {rows[:2]}"


check("corporate_actions", _ca)

print("SMOKE:", "ALL PASS" if ok else "FAILURES ABOVE")
sys.exit(0 if ok else 1)
