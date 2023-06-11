from unittest import TestCase

from CheckCandleSymbol import CheckCandleSymbol


class TestCheckCandleSymbol(TestCase):
    row = ['SepehrSaderat.Inv.', '20230201', '8200.00', '8520.00', '7850.00', '8130.00', '53398853190', '6592424',
           '1827', 'D', '8160.00', '7960.00', '114312662654155', 'وسپهر', 'سرمايه گذاري مالي سپهرصادرات']

    row2 = ['SepehrSaderat.Inv.', '20230219', '4119.00', '4119.00', '3700.00', '3848.00', '5050484693',
            '1329910',
            '400', 'D', '3850.00', '3788.00', '114312662654155', 'وسپهر', 'سرمايه گذاري مالي سپهرصادرات']
    row3 = ['SepehrSaderat.Inv.', '20230219', '4119.00', '4119.00', '3700.00', '3848.00', '5050484693',
            '1329910',
            '400', 'D', '3850.00', '3788.00', '114312662654155', 'وسپهر', 'سرمايه گذاري مالي سپهرصادرات']

    def test_is_doji(self):
        self.assertFalse(CheckCandleSymbol.is_doji(self.row))

    def test_is_hammer_hanging_man(self):
        self.assertFalse(CheckCandleSymbol.is_hammer_hanging_man(self.row))

    def test_is_bearish_engulfing(self):
        self.assertFalse(CheckCandleSymbol().is_bearish_engulfing(self.row, self.row2))

    def test_is_bullish_engulfing(self):
        self.assertFalse(CheckCandleSymbol().is_bullish_engulfing(self.row, self.row2))

    def test_is_bullish_hammer_engulfing(self):
        self.assertFalse(CheckCandleSymbol().is_bullish_hammer_engulfing(self.row, self.row2))

    def test_is_bearish_hammer_engulfing(self):
        self.assertFalse(CheckCandleSymbol().is_bearish_hammer_engulfing(self.row, self.row2))

    def test_is_piercing_pattern(self):
        self.assertFalse(CheckCandleSymbol().is_piercing_pattern(self.row, self.row2))

    def test_is_morning_star(self):
        self.assertFalse(CheckCandleSymbol().is_morning_star(self.row, self.row2, self.row3))

    def test_without_shadow(self):
        self.assertFalse(CheckCandleSymbol.without_shadow(self.row))

    def test_full_time_buy_queue(self):
        self.assertFalse(CheckCandleSymbol().full_time_buy_queue(self.row))

    def test_full_time_sell_queue(self):
        self.assertFalse(CheckCandleSymbol().full_time_sell_queue(self.row))

    def test_is_full_time_queue(self):
        self.assertFalse(CheckCandleSymbol().is_full_time_queue(self.row))

    def test_is_full_time_queue_with_shadow(self):
        self.assertFalse(CheckCandleSymbol.is_full_time_queue_with_shadow(self.row))

    def test_is_bearish(self):
        rows = [self.row, self.row2]
        self.assertTrue(CheckCandleSymbol.is_bearish(rows))
