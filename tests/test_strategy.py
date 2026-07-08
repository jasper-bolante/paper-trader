"""Risk rules: drawdown state machine, entry constraints, exit gating."""
import unittest

from trader import config, db, ledger, strategy


def cfg():
    return config.load()


def mem():
    return db.connect(":memory:")


def add_calendar(conn, dates):
    for d in dates:
        conn.execute("INSERT OR IGNORE INTO calendar(date,open_time,close_time) "
                     "VALUES(?,?,?)", (d, "09:30", "16:00"))


def sig(sym, rank, mom=0.2, vol=0.30, price=100.0, ma_exit=90.0):
    return {"symbol": sym, "eligible": 1, "rank": rank, "momentum": mom,
            "ann_vol": vol, "price": price, "ma_trend": 95.0,
            "ma_trend_rising": 1, "ma_exit": ma_exit, "adv_dollar": 5e7,
            "veto_reason": None}


class TestDrawdownState(unittest.TestCase):
    def test_escalation_thresholds(self):
        c = cfg()
        self.assertEqual(strategy.dd_state("normal", 0.05, c), "normal")
        self.assertEqual(strategy.dd_state("normal", 0.08, c), "no_buys")
        self.assertEqual(strategy.dd_state("normal", 0.13, c), "halve")
        self.assertEqual(strategy.dd_state("normal", 0.16, c), "halted")

    def test_halted_is_sticky(self):
        c = cfg()
        self.assertEqual(strategy.dd_state("halted", 0.01, c), "halted")

    def test_hysteresis(self):
        c = cfg()
        # In no_buys at 7.5% dd; recovering to 6.5% is inside hysteresis.
        self.assertEqual(strategy.dd_state("no_buys", 0.065, c), "no_buys")
        self.assertEqual(strategy.dd_state("no_buys", 0.04, c), "normal")
        self.assertEqual(strategy.dd_state("halve", 0.11, c), "halve")
        self.assertEqual(strategy.dd_state("halve", 0.08, c), "no_buys")


class TestEntries(unittest.TestCase):
    def test_no_entries_outside_normal_state(self):
        conn = mem()
        sigs = {"AAA": sig("AAA", 1)}
        buys, skips = strategy.plan_entries(
            conn, cfg(), sigs, {}, {"AAA": {"ask": 100, "last": 100}},
            {"AAA": "Tech"}, 20000, 15000, "2026-07-06", "no_buys", 0, "SPY")
        self.assertEqual(buys, [])
        self.assertIn("no_buys", skips[0]["reason"])

    def test_entry_sizing_and_daily_limit(self):
        conn = mem()
        sigs = {s: sig(s, i + 1) for i, s in enumerate(["AAA", "BBB", "CCC"])}
        quotes = {s: {"ask": 100.0, "last": 100.0} for s in sigs}
        sectors = {"AAA": "Tech", "BBB": "Health", "CCC": "Energy"}
        buys, _ = strategy.plan_entries(conn, cfg(), sigs, {}, quotes, sectors,
                                        20000, 15000, "2026-07-06", "normal",
                                        0, "SPY")
        self.assertEqual(len(buys), 2)  # max_new_positions_per_day
        for b in buys:
            # base size = 20000*0.80/12 ≈ 1333; never above 10% of equity
            self.assertLessEqual(b["detail"]["notional"], 2000 + 100)

    def test_sector_cap_blocks(self):
        conn = mem()
        c = cfg()
        sigs = {"AAA": sig("AAA", 1)}
        quotes = {"AAA": {"ask": 100.0, "last": 100.0},
                  "TT1": {"last": 100.0}, "TT2": {"last": 100.0}}
        positions = {"TT1": {"qty": 25, "basis": 2400},
                     "TT2": {"qty": 25, "basis": 2400}}
        sectors = {"AAA": "Tech", "TT1": "Tech", "TT2": "Tech"}
        buys, skips = strategy.plan_entries(conn, c, sigs, positions, quotes,
                                            sectors, 20000, 15000, "2026-07-06",
                                            "normal", 0, "SPY")
        self.assertEqual(buys, [])
        self.assertTrue(any("sector cap" in s["reason"] for s in skips))

    def test_settled_cash_limits_size(self):
        conn = mem()
        sigs = {"AAA": sig("AAA", 1)}
        quotes = {"AAA": {"ask": 100.0, "last": 100.0}}
        buys, skips = strategy.plan_entries(conn, cfg(), sigs, {}, quotes,
                                            {"AAA": "Tech"}, 20000, 350.0,
                                            "2026-07-06", "normal", 0, "SPY")
        self.assertEqual(buys, [])  # investable $350 < $500 minimum entry
        self.assertTrue(any("insufficient investable cash" in s["reason"]
                            for s in skips))


class TestExits(unittest.TestCase):
    def _setup(self, entry_date, today, dates):
        conn = mem()
        add_calendar(conn, dates)
        ledger.open_lot(conn, "t", "AAA", entry_date, 10, 100.0)
        conn.execute(
            "INSERT INTO position_state(symbol,entry_date,highest_close,stop_price) "
            "VALUES('AAA',?,110,99)", (entry_date,),
        )
        return conn

    def test_min_hold_blocks_signal_exit(self):
        dates = ["2026-07-06", "2026-07-07"]
        conn = self._setup("2026-07-06", "2026-07-07", dates)
        sigs = {"AAA": sig("AAA", None)}  # rank decayed to ineligible
        sigs["AAA"]["rank"] = None
        sells, holds = strategy.plan_exits(
            conn, cfg(), sigs, {"AAA": {"qty": 10, "basis": 1000}},
            {"AAA": {"last": 100}}, "2026-07-07", "normal", "SPY")
        self.assertEqual(sells, [])
        self.assertEqual(len(holds), 1)

    def test_rank_decay_exits_after_min_hold(self):
        dates = ["2026-07-01", "2026-07-02", "2026-07-03", "2026-07-06",
                 "2026-07-07"]
        conn = self._setup("2026-07-01", "2026-07-07", dates)
        sigs = {"AAA": sig("AAA", 200)}  # decayed past exit_rank_min=150
        sells, _ = strategy.plan_exits(
            conn, cfg(), sigs, {"AAA": {"qty": 10, "basis": 1000}},
            {"AAA": {"last": 100}}, "2026-07-07", "normal", "SPY")
        self.assertEqual(len(sells), 1)
        self.assertIn("rank decayed", sells[0]["reason"])

    def test_trend_break_exits(self):
        dates = ["2026-07-01", "2026-07-02", "2026-07-03", "2026-07-06",
                 "2026-07-07"]
        conn = self._setup("2026-07-01", "2026-07-07", dates)
        s = sig("AAA", 10, ma_exit=105.0)  # price 100 < 100DMA 105
        sells, _ = strategy.plan_exits(
            conn, cfg(), {"AAA": s}, {"AAA": {"qty": 10, "basis": 1000}},
            {"AAA": {"last": 100}}, "2026-07-07", "normal", "SPY")
        self.assertEqual(len(sells), 1)
        self.assertIn("trend break", sells[0]["reason"])


class TestBallastAndTrims(unittest.TestCase):
    def test_ballast_buys_toward_target_when_below_band(self):
        plan = strategy.plan_ballast(cfg(), {}, {"SPY": {"last": 500, "ask": 500.2}},
                                     20000, 15000, "normal", "SPY")
        self.assertEqual(plan["side"], "buy")
        self.assertGreaterEqual(plan["qty"], 7)  # toward 20% of 20k = $4k

    def test_trim_oversized_position(self):
        positions = {"AAA": {"qty": 40, "basis": 2000}}
        trims = strategy.plan_trims(cfg(), positions, {"AAA": {"last": 100}},
                                    20000, "SPY")
        self.assertEqual(len(trims), 1)   # $4000 = 20% > 14% trim threshold
        self.assertGreaterEqual(trims[0]["qty"], 19)  # back toward 10% = $2000


if __name__ == "__main__":
    unittest.main()
