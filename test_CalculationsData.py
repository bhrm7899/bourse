from unittest import TestCase

from CalculationsData import CalculationsData


class TestCalculationsData(TestCase):
    row = ['SepehrSaderat.Inv.', '20230201', '8200.00', '8520.00', '7850.00', '8130.00', '53398853190', '6592424',
           '1827', 'D', '8160.00', '7960.00', '114312662654155', 'وسپهر', 'سرمايه گذاري مالي سپهرصادرات']

    row2 = ['SepehrSaderat.Inv.', '20230219', '4119.00', '4119.00', '3700.00', '3848.00', '5050484693', '1329910',
            '400', 'D', '3850.00', '3788.00', '114312662654155', 'وسپهر', 'سرمايه گذاري مالي سپهرصادرات']

    def test_candle_status(self):
        self.assertEqual(CalculationsData.candle_status(self.row), -1)

    def test_day_status(self):
        self.assertEqual(CalculationsData.day_status(self.row), -1)

    def test_trend_status(self):
        self.assertEqual(CalculationsData.trend_status(self.row, self.row2), -1)

    def test_avg_volume(self):
        self.assertEqual(CalculationsData.avg_volume(self.row), -1)

    def test_min_percent_bear_trend(self):
        self.assertFalse(CalculationsData.min_percent_bear_trend(self.row, self.row2, 5))

    def test_min_percent_bull_trend(self):
        self.assertFalse(CalculationsData.min_percent_bull_trend(self.row, self.row2, 5))

    def test_last_lower_than_close(self):
        self.assertFalse(CalculationsData.last_lower_than_close(self.row, 5))

    def test_last_upper_than_close(self):
        self.assertFalse(CalculationsData.last_upper_than_close(self.row, 5))

    def test_cover2to1(self):
        self.assertFalse(CalculationsData.cover2to1(self.row, self.row2))

    def test_min_body_bullish(self):
        self.assertFalse(CalculationsData.min_body_bullish(self.row, 5))

    def test_min_body_bearish(self):
        self.assertFalse(CalculationsData.min_body_bearish(self.row, 5))

    def test_have_up_shadow(self):
        self.assertTrue(CalculationsData.have_up_shadow(self.row))

    def test_have_down_shadow(self):
        self.assertTrue(CalculationsData.have_down_shadow(self.row))

    def test_have_up_shadow_min_percent(self):
        self.assertFalse(CalculationsData.have_up_shadow_min_percent(self.row, 5))
