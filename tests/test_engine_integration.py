"""End-to-end engine test against a deterministic fake market: bootstrap,
ballast purchase, momentum entries, stop creation, snapshots, EOD report."""
import os
import shutil
import tempfile
import unittest
import zlib
from datetime import date, datetime, timedelta

from trader import config

config.load()  # cache config.yaml before ROOT is patched

from trader import db, engine, ledger  # noqa: E402

REAL_ROOT = config.ROOT


def _px(sym):
    return 30.0 + (zlib.crc32(sym.encode()) % 400)


def _uptrend(sym):
    return zlib.crc32(sym.encode()) % 5 == 0


class FakeApi:
    """Deterministic market: ~20% of symbols in smooth uptrends (momentum
    candidates), the rest flat. Tight spreads, deep liquidity."""

    def calendar(self, start, end):
        out = []
        d = date.fromisoformat(start)
        stop = date.fromisoformat(end)
        while d <= stop:
            if d.weekday() < 5:
                out.append({"date": d.isoformat(), "open": "09:30",
                            "close": "16:00"})
            d += timedelta(days=1)
        return out

    def latest_quotes(self, symbols):
        return {s: {"bid": round(_px(s) * 0.999, 2),
                    "ask": round(_px(s) * 1.001, 2),
                    "bid_size": 10, "ask_size": 10, "ts": "t"}
                for s in symbols}

    def latest_trades(self, symbols):
        return {s: {"price": _px(s), "ts": "t"} for s in symbols}

    def daily_bars(self, symbols, start, end):
        out = {}
        for s in symbols:
            base = _px(s)
            drift = 0.002 if _uptrend(s) else 0.0
            n = 260
            bars = []
            price = base / ((1 + drift) ** n)
            d = date.today() - timedelta(days=int(n * 1.5))
            i = 0
            while len(bars) < n:
                if d.weekday() < 5:
                    price *= (1 + drift)
                    wiggle = 1 + (0.001 if i % 2 == 0 else -0.001)
                    c = price * wiggle
                    bars.append({"t": d.isoformat(), "o": c, "h": c * 1.004,
                                 "l": c * 0.996, "c": round(c, 2),
                                 "v": 1_000_000})
                    i += 1
                d += timedelta(days=1)
            out[s] = bars
        return out

    def minute_bars(self, symbols, start, end):
        return {s: [] for s in symbols}

    def corporate_actions(self, symbols, start, end):
        today = date.today().isoformat()
        pay = (date.today() + timedelta(days=14)).isoformat()
        if "SPY" in symbols:
            return [{"symbol": "SPY", "type": "cash_dividend",
                     "ex_date": today, "pay_date": pay, "rate": 1.62,
                     "raw": {}}]
        return []

    def clock(self):
        return {}


class TestEngineIntegration(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        os.makedirs(os.path.join(self.tmp, "data"))
        shutil.copy(os.path.join(REAL_ROOT, "data", "universe.csv"),
                    os.path.join(self.tmp, "data", "universe.csv"))
        config.ROOT = self.tmp
        self.db_file = os.path.join(config.state_dir(), "trader.db")

    def tearDown(self):
        config.ROOT = REAL_ROOT
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_full_cycle(self):
        cfg = config.load()
        api = FakeApi()

        # --- first hourly run: bootstrap, ballast, entries, stops ---
        engine.run("hourly", api=api, db_file=self.db_file)
        conn = db.connect(self.db_file)
        today = date.today().isoformat()

        self.assertIsNotNone(db.get_meta(conn, "inception"))
        positions = ledger.positions(conn)
        self.assertIn("SPY", positions)
        spy_value = positions["SPY"]["qty"] * _px("SPY")
        self.assertGreater(spy_value, 0.14 * 20000)   # ballast near 20%
        self.assertLess(spy_value, 0.26 * 20000)

        stocks = [s for s in positions if s != "SPY"]
        self.assertGreaterEqual(len(stocks), 1)
        self.assertLessEqual(len(stocks), cfg["risk"]["max_new_positions_per_day"])
        for s in stocks:
            val = positions[s]["qty"] * _px(s)
            self.assertLessEqual(val, cfg["risk"]["max_position_pct"] * 20000 * 1.05)

        # One trailing stop per stock, none for the ballast.
        stops = conn.execute(
            "SELECT symbol FROM orders WHERE order_type='stop' AND status='open'"
        ).fetchall()
        self.assertEqual(sorted(r["symbol"] for r in stops), sorted(stocks))

        # Cash invariants: settled cash never negative, no margin used.
        self.assertGreaterEqual(ledger.settled_cash(conn, today), 0)

        # Decision log covers entries and the reasoning trail.
        n_dec = conn.execute("SELECT COUNT(*) AS n FROM decisions").fetchone()["n"]
        self.assertGreater(n_dec, 0)
        self.assertTrue(os.path.exists(
            os.path.join(self.tmp, "state", "decisions.jsonl")))

        # Benchmark funded with the same $20k.
        self.assertIsNotNone(db.get_meta(conn, "bench_shares"))

        snap = conn.execute(
            "SELECT * FROM equity_snapshots WHERE kind='intraday'"
        ).fetchone()
        self.assertIsNotNone(snap)
        # Equity ≈ starting cash minus trading costs (< 1% lost to costs).
        self.assertGreater(snap["equity"], 20000 * 0.99)
        self.assertLessEqual(snap["equity"], 20000)
        conn.close()

        # --- second hourly run: daily entry limit holds ---
        engine.run("hourly", api=api, db_file=self.db_file)
        conn = db.connect(self.db_file)
        stocks2 = [s for s in ledger.positions(conn) if s != "SPY"]
        self.assertLessEqual(len(stocks2),
                             cfg["risk"]["max_new_positions_per_day"])
        conn.close()

        # --- EOD run: snapshot, dividend capture, report ---
        engine.run("eod", api=api, db_file=self.db_file)
        conn = db.connect(self.db_file)
        self.assertEqual(db.get_meta(conn, "eod_done"), today)
        eod = conn.execute(
            "SELECT * FROM equity_snapshots WHERE kind='eod'"
        ).fetchone()
        self.assertIsNotNone(eod)
        self.assertIsNotNone(eod["benchmark_value"])
        # SPY dividend recorded, settling on the future pay date (unsettled now).
        div = conn.execute(
            "SELECT * FROM cash_ledger WHERE type='dividend'"
        ).fetchone()
        self.assertIsNotNone(div)
        self.assertGreater(div["settle_date"], today)
        self.assertTrue(os.path.exists(os.path.join(self.tmp, "REPORT.md")))
        self.assertTrue(os.path.exists(
            os.path.join(self.tmp, "docs", "equity_curve.svg")))
        self.assertIsNotNone(db.get_meta(conn, "hwm"))
        conn.close()


if __name__ == "__main__":
    unittest.main()
