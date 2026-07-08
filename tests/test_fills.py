"""Fill engine: spread, impact scaling, participation caps, limit/stop semantics."""
import unittest

from trader import fills

CFG = {"fills": {"impact_coefficient": 1.0, "max_participation": 0.10,
                 "fallback_half_spread_bps": 5.0, "max_half_spread_bps": 75.0,
                 "marketable_limit_buffer": 0.001}}

QUOTE = {"bid": 99.90, "ask": 100.10, "last": 100.00}


class TestMarket(unittest.TestCase):
    def test_buy_pays_ask_plus_impact(self):
        r = fills.fill_market("buy", 10, QUOTE, 50_000_000, 0.25, None, CFG)
        self.assertEqual(r.qty, 10)
        self.assertGreaterEqual(r.price, 100.10)
        self.assertGreater(r.spread_cost, 0)

    def test_sell_receives_bid_minus_impact(self):
        r = fills.fill_market("sell", 10, QUOTE, 50_000_000, 0.25, None, CFG)
        self.assertLessEqual(r.price, 99.90)

    def test_impact_scales_with_size(self):
        small = fills.fill_market("buy", 10, QUOTE, 5_000_000, 0.40, None, CFG)
        large = fills.fill_market("buy", 10000, QUOTE, 5_000_000, 0.40, None, CFG)
        self.assertGreater(large.price, small.price)

    def test_impact_scales_with_volatility(self):
        calm = fills.impact_fraction(10000, 5_000_000, 0.15, CFG)
        wild = fills.impact_fraction(10000, 5_000_000, 0.60, CFG)
        self.assertGreater(wild, calm)

    def test_participation_cap_partial_fill(self):
        r = fills.fill_market("buy", 1000, QUOTE, 50_000_000, 0.25, 500, CFG)
        self.assertEqual(r.qty, 50)  # 10% of 500 observed shares
        self.assertIn("partial", r.note)

    def test_fallback_spread_without_quote(self):
        r = fills.fill_market("buy", 10, {"last": 50.0}, None, None, None, CFG)
        self.assertAlmostEqual(r.price, 50.0 * 1.0005, places=4)

    def test_no_quote_no_fill(self):
        r = fills.fill_market("buy", 10, {}, None, None, None, CFG)
        self.assertEqual(r.qty, 0)


class TestLimit(unittest.TestCase):
    BARS = [{"o": 101, "h": 101.5, "l": 100.4, "c": 100.6, "v": 5000}]

    def test_not_reached_no_fill(self):
        r = fills.evaluate_limit("buy", 10, 100.0, {"bid": 100.4, "ask": 100.6},
                                 self.BARS, 1e7, 0.3, CFG)
        self.assertEqual(r.qty, 0)

    def test_touch_is_not_enough(self):
        bars = [{"o": 101, "h": 101, "l": 100.0, "c": 100.5, "v": 5000}]
        r = fills.evaluate_limit("buy", 10, 100.0, {"bid": 100.4, "ask": 100.6},
                                 bars, 1e7, 0.3, CFG)
        self.assertEqual(r.qty, 0)  # low == limit: queue position, no fill

    def test_trade_through_fills_at_limit(self):
        bars = [{"o": 101, "h": 101, "l": 99.7, "c": 100.5, "v": 5000}]
        r = fills.evaluate_limit("buy", 10, 100.0, {"bid": 100.4, "ask": 100.6},
                                 bars, 1e7, 0.3, CFG)
        self.assertEqual(r.qty, 10)
        self.assertEqual(r.price, 100.0)

    def test_marketable_now_fills_capped_at_limit(self):
        r = fills.evaluate_limit("buy", 10, 100.2, {"bid": 99.9, "ask": 100.1},
                                 [], 1e7, 0.3, CFG)
        self.assertEqual(r.qty, 10)
        self.assertLessEqual(r.price, 100.2)


class TestStop(unittest.TestCase):
    def test_not_triggered(self):
        bars = [{"o": 100, "h": 101, "l": 95.5, "c": 100, "v": 1000}]
        r = fills.evaluate_stop("sell", 10, 95.0, {"last": 100}, bars, 1e7, 0.3, CFG)
        self.assertEqual(r.qty, 0)

    def test_triggered_fills_near_stop(self):
        bars = [{"o": 96, "h": 96.5, "l": 94.8, "c": 95.2, "v": 1000}]
        r = fills.evaluate_stop("sell", 10, 95.0, {"last": 95.2}, bars, 1e7, 0.3, CFG)
        self.assertEqual(r.qty, 10)
        self.assertLess(r.price, 95.0)         # spread + impact below the stop
        self.assertGreater(r.price, 94.0)      # but not absurdly far

    def test_gap_through_stop_fills_at_open(self):
        bars = [{"o": 90.0, "h": 91, "l": 89.5, "c": 90.5, "v": 1000}]
        r = fills.evaluate_stop("sell", 10, 95.0, {"last": 90.5}, bars, 1e7, 0.3, CFG)
        self.assertEqual(r.qty, 10)
        self.assertLess(r.price, 90.1)          # fills off the gap open, not the stop
        self.assertIn("gap", r.note)

    def test_trigger_from_quote_without_bars(self):
        r = fills.evaluate_stop("sell", 10, 95.0, {"last": 94.0}, [], 1e7, 0.3, CFG)
        self.assertEqual(r.qty, 10)
        self.assertLess(r.price, 94.01)


if __name__ == "__main__":
    unittest.main()
