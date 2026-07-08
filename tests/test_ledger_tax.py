"""Settlement, FIFO, wash-sale, and tax-reserve behavior."""
import unittest

from trader import db, ledger, tax

CFG = {"tax": {"short_term_rate": 0.24, "long_term_rate": 0.15,
               "dividend_rate": 0.15}}


def mem():
    return db.connect(":memory:")


class TestSettlement(unittest.TestCase):
    def test_deposit_settles_immediately(self):
        conn = mem()
        ledger.deposit(conn, "t", "2026-07-06", 20000)
        self.assertEqual(ledger.settled_cash(conn, "2026-07-06"), 20000)

    def test_sale_proceeds_settle_t_plus_1(self):
        conn = mem()
        ledger.deposit(conn, "t", "2026-07-06", 20000)
        ledger.record_buy(conn, "t", "2026-07-06", "AAPL", 5000)
        self.assertEqual(ledger.settled_cash(conn, "2026-07-06"), 15000)
        # Sell on 7/7; proceeds settle 7/8.
        ledger.record_sell(conn, "t", "2026-07-07", "2026-07-08", "AAPL", 5500)
        self.assertEqual(ledger.settled_cash(conn, "2026-07-07"), 15000)
        self.assertEqual(ledger.unsettled_cash(conn, "2026-07-07"), 5500)
        self.assertEqual(ledger.settled_cash(conn, "2026-07-08"), 20500)

    def test_dividend_settles_on_pay_date(self):
        conn = mem()
        ledger.record_dividend(conn, "t", "2026-07-06", "2026-07-20", "MSFT", 42)
        self.assertEqual(ledger.settled_cash(conn, "2026-07-06"), 0)
        self.assertEqual(ledger.settled_cash(conn, "2026-07-20"), 42)


class TestFifo(unittest.TestCase):
    def test_fifo_order_and_terms(self):
        conn = mem()
        ledger.open_lot(conn, "t", "X", "2025-01-10", 10, 100.0)  # old lot
        ledger.open_lot(conn, "t", "X", "2026-06-01", 10, 150.0)  # recent lot
        events = tax.realize_sale(conn, "t", "2026-07-06", "X", 15, 15 * 160.0)
        # First 10 shares from the 2025 lot (long), next 5 from 2026 (short).
        self.assertEqual(len(events), 2)
        self.assertEqual(events[0]["term"], "long")
        self.assertAlmostEqual(events[0]["gain"], 600.0)   # (160-100)*10
        self.assertEqual(events[1]["term"], "short")
        self.assertAlmostEqual(events[1]["gain"], 50.0)    # (160-150)*5
        self.assertAlmostEqual(ledger.position_qty(conn, "X"), 5)

    def test_cannot_sell_more_than_held(self):
        conn = mem()
        ledger.open_lot(conn, "t", "X", "2026-06-01", 10, 100.0)
        with self.assertRaises(ValueError):
            tax.realize_sale(conn, "t", "2026-07-06", "X", 11, 1100)


class TestWashSale(unittest.TestCase):
    def test_wash_against_prior_purchase(self):
        conn = mem()
        # Lot A bought long ago, lot B bought 5 days before the loss sale.
        ledger.open_lot(conn, "t", "X", "2026-03-01", 10, 100.0)
        lot_b = ledger.open_lot(conn, "t", "X", "2026-07-01", 10, 95.0)
        # Sell the FIFO (older) lot at a loss on 7/6: 10 sh @ 90 = -$100.
        events = tax.realize_sale(conn, "t", "2026-07-06", "X", 10, 900.0)
        self.assertAlmostEqual(events[0]["gain"], -100.0)
        self.assertAlmostEqual(events[0]["wash_disallowed"], 100.0)
        b = conn.execute("SELECT * FROM lots WHERE id=?", (lot_b,)).fetchone()
        # Disallowed $100 spread over B's 10 shares: basis 95 -> 105.
        self.assertAlmostEqual(b["basis_per_share"], 105.0)
        # Holding period tacked back to the sold lot's start.
        self.assertEqual(b["holding_period_start"], "2026-03-01")

    def test_wash_on_repurchase(self):
        conn = mem()
        ledger.open_lot(conn, "t", "X", "2026-05-01", 10, 100.0)
        events = tax.realize_sale(conn, "t", "2026-07-01", "X", 10, 900.0)
        self.assertAlmostEqual(events[0]["wash_disallowed"], 0.0)
        # Repurchase 6 shares within 30 days: 6/10 of the loss is disallowed.
        lot2 = ledger.open_lot(conn, "t", "X", "2026-07-10", 6, 92.0)
        dis = tax.apply_wash_on_buy(conn, "X", "2026-07-10", lot2)
        self.assertAlmostEqual(dis, 60.0)
        l2 = conn.execute("SELECT * FROM lots WHERE id=?", (lot2,)).fetchone()
        self.assertAlmostEqual(l2["basis_per_share"], 102.0)  # 92 + 60/6
        self.assertEqual(l2["holding_period_start"], "2026-05-01")
        r = conn.execute("SELECT * FROM realized").fetchone()
        self.assertAlmostEqual(r["wash_disallowed"], 60.0)
        self.assertAlmostEqual(r["wash_pending_qty"], 4.0)

    def test_no_wash_after_31_days(self):
        conn = mem()
        ledger.open_lot(conn, "t", "X", "2026-05-01", 10, 100.0)
        tax.realize_sale(conn, "t", "2026-06-01", "X", 10, 900.0)
        tax.expire_pending_washes(conn, "2026-07-06")
        lot2 = ledger.open_lot(conn, "t", "X", "2026-07-06", 10, 92.0)
        dis = tax.apply_wash_on_buy(conn, "X", "2026-07-06", lot2)
        self.assertAlmostEqual(dis, 0.0)

    def test_replacement_shares_absorb_once(self):
        conn = mem()
        ledger.open_lot(conn, "t", "X", "2026-05-01", 10, 100.0)
        tax.realize_sale(conn, "t", "2026-07-01", "X", 10, 900.0)  # -$100 pending
        lot2 = ledger.open_lot(conn, "t", "X", "2026-07-02", 10, 92.0)
        self.assertAlmostEqual(tax.apply_wash_on_buy(conn, "X", "2026-07-02", lot2), 100.0)
        # A second buy finds nothing left to absorb.
        lot3 = ledger.open_lot(conn, "t", "X", "2026-07-03", 10, 91.0)
        self.assertAlmostEqual(tax.apply_wash_on_buy(conn, "X", "2026-07-03", lot3), 0.0)


class TestTaxReserve(unittest.TestCase):
    def _realize(self, conn, gain, term, date="2026-07-01"):
        conn.execute(
            "INSERT INTO realized(ts,trade_date,symbol,qty,open_date,"
            "holding_period_start,proceeds,basis,gain,term) "
            "VALUES('t',?,'X',1,'2026-01-01','2026-01-01',0,0,?,?)",
            (date, gain, term),
        )

    def test_rates(self):
        conn = mem()
        self._realize(conn, 1000, "short")
        self._realize(conn, 1000, "long")
        self.assertAlmostEqual(tax.tax_reserve(conn, CFG), 240 + 150)

    def test_st_loss_offsets_lt_gain(self):
        conn = mem()
        self._realize(conn, -400, "short")
        self._realize(conn, 1000, "long")
        self.assertAlmostEqual(tax.tax_reserve(conn, CFG), 600 * 0.15)

    def test_net_loss_reserves_nothing_and_carries(self):
        conn = mem()
        self._realize(conn, -1000, "short", "2026-07-01")
        self.assertAlmostEqual(tax.tax_reserve(conn, CFG), 0.0)
        self._realize(conn, 600, "short", "2027-02-01")  # next year
        self.assertAlmostEqual(tax.tax_reserve(conn, CFG), 0.0)  # carried loss
        self._realize(conn, 1000, "short", "2027-03-01")
        self.assertAlmostEqual(tax.tax_reserve(conn, CFG), 600 * 0.24)

    def test_wash_disallowed_raises_reserve(self):
        conn = mem()
        # -$100 loss but fully wash-disallowed => allowed gain is 0, and the
        # other +$100 short gain is fully taxable.
        conn.execute(
            "INSERT INTO realized(ts,trade_date,symbol,qty,open_date,"
            "holding_period_start,proceeds,basis,gain,wash_disallowed,term) "
            "VALUES('t','2026-07-01','X',1,'2026-01-01','2026-01-01',0,0,-100,100,'short')"
        )
        self._realize(conn, 100, "short")
        self.assertAlmostEqual(tax.tax_reserve(conn, CFG), 24.0)

    def test_dividends_taxed(self):
        conn = mem()
        ledger.record_dividend(conn, "t", "2026-07-01", "2026-07-15", "X", 200)
        self.assertAlmostEqual(tax.tax_reserve(conn, CFG), 30.0)


if __name__ == "__main__":
    unittest.main()
