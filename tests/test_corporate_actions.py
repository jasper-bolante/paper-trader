"""Splits and dividends on held positions."""
import unittest

from trader import corporate_actions, db, ledger


def mem():
    return db.connect(":memory:")


def noop_log(kind, symbol, detail):
    pass


class TestSplit(unittest.TestCase):
    def _seed_split(self, conn, ratio):
        conn.execute(
            "INSERT INTO corporate_actions(symbol,type,ex_date,rate) "
            "VALUES('NVDA','forward_split','2026-07-06',?)", (ratio,),
        )

    def test_forward_split_scales_lots_and_stops(self):
        conn = mem()
        ledger.open_lot(conn, "t", "NVDA", "2026-06-01", 10, 120.0)
        conn.execute(
            "INSERT INTO position_state(symbol,entry_date,highest_close,stop_price) "
            "VALUES('NVDA','2026-06-01',130.0,117.0)"
        )
        conn.execute(
            "INSERT INTO orders(created_ts,created_date,symbol,side,qty,"
            "remaining_qty,order_type,stop_price) "
            "VALUES('t','2026-06-01','NVDA','sell',10,10,'stop',117.0)"
        )
        self._seed_split(conn, 2.0)
        corporate_actions.apply_due(conn, "t", "2026-07-06", lambda s: 65.0, noop_log)
        lot = conn.execute("SELECT * FROM lots").fetchone()
        self.assertAlmostEqual(lot["qty_open"], 20)
        self.assertAlmostEqual(lot["basis_per_share"], 60.0)  # total basis unchanged
        st = conn.execute("SELECT * FROM position_state").fetchone()
        self.assertAlmostEqual(st["stop_price"], 58.5)
        o = conn.execute("SELECT * FROM orders").fetchone()
        self.assertAlmostEqual(o["remaining_qty"], 20)
        self.assertAlmostEqual(o["stop_price"], 58.5)

    def test_fractional_shares_paid_cash_in_lieu(self):
        conn = mem()
        ledger.open_lot(conn, "t", "XYZ", "2026-06-01", 7, 100.0)
        conn.execute(
            "INSERT INTO corporate_actions(symbol,type,ex_date,rate) "
            "VALUES('XYZ','forward_split','2026-07-06',?)", (1.5,),
        )
        corporate_actions.apply_due(conn, "t", "2026-07-06", lambda s: 66.67, noop_log)
        # 7 * 1.5 = 10.5 -> 10 shares + 0.5 * 66.67 cash-in-lieu
        self.assertAlmostEqual(ledger.position_qty(conn, "XYZ"), 10, places=6)
        cash = conn.execute(
            "SELECT amount FROM cash_ledger WHERE type='cash_in_lieu'"
        ).fetchone()
        self.assertAlmostEqual(cash["amount"], 33.34, places=2)

    def test_not_held_marks_applied_without_effect(self):
        conn = mem()
        self._seed_split(conn, 2.0)
        corporate_actions.apply_due(conn, "t", "2026-07-06", lambda s: 65.0, noop_log)
        ca = conn.execute("SELECT applied FROM corporate_actions").fetchone()
        self.assertEqual(ca["applied"], 1)
        self.assertEqual(ledger.position_qty(conn, "NVDA"), 0)


class TestDividend(unittest.TestCase):
    def test_dividend_accrues_and_settles_on_pay_date(self):
        conn = mem()
        ledger.open_lot(conn, "t", "MSFT", "2026-06-01", 12, 400.0)
        conn.execute(
            "INSERT INTO corporate_actions(symbol,type,ex_date,pay_date,rate) "
            "VALUES('MSFT','cash_dividend','2026-07-06','2026-07-20',0.83)"
        )
        corporate_actions.apply_due(conn, "t", "2026-07-06", lambda s: 400.0, noop_log)
        self.assertAlmostEqual(ledger.settled_cash(conn, "2026-07-06"), 0.0)
        self.assertAlmostEqual(ledger.settled_cash(conn, "2026-07-20"), 9.96)


if __name__ == "__main__":
    unittest.main()
