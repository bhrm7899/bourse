from unittest import TestCase

from CheckCandleSymbol import CheckCandleSymbol


class TestCheckCandleSymbol(TestCase):
    def test_is_doji(self):
        row = ['SepehrSaderat.Inv.', '20230201', '8200.00', '8520.00', '7850.00', '8130.00', '53398853190', '6592424', '1827', 'D',
        '8160.00', '7960.00', '114312662654155', 'وسپهر', 'سرمايه گذاري مالي سپهرصادرات']
        self.assertFalse(CheckCandleSymbol.is_doji(row))

    def test_is_hammer_hanging_man(self):
        row = ['SepehrSaderat.Inv.', '20230201', '8200.00', '8520.00', '7850.00', '8130.00', '53398853190', '6592424',
               '1827', 'D',
               '8160.00', '7960.00', '114312662654155', 'وسپهر', 'سرمايه گذاري مالي سپهرصادرات']
        self.assertFalse(CheckCandleSymbol.is_hammer_hanging_man(row))

    # def test_is_bearish_engulfing(self):
    #     self.fail()
    #
    # def test_is_bullish_engulfing(self):
    #     self.fail()
    #
    # def test_is_bullish_hammer_engulfing(self):
    #     self.fail()
    #
    # def test_is_bearish_hammer_engulfing(self):
    #     self.fail()
    #
    # def test_is_piercing_pattern(self):
    #     self.fail()
    #
    # def test_is_morning_star(self):
    #     self.fail()
    #
    # def test_without_shadow(self):
    #     self.fail()
    #
    # def test_full_time_buy_queue(self):
    #     self.fail()
    #
    # def test_full_time_sell_queue(self):
    #     self.fail()
    #
    # def test_is_full_time_queue(self):
    #     self.fail()
    #
    # def test_is_full_time_queue_with_shadow(self):
    #     self.fail()
    #
    # def test_is_bearish(self):
    #     self.fail()
