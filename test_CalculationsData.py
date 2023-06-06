from unittest import TestCase
import CalculationsData


class TestCalculationsData(TestCase):
    calculationsData = CalculationsData()
    def test_candle_status(self):
        row = ['SepehrSaderat.Inv.', '20230201', '8200.00', '8520.00', '7850.00', '8130.00', '53398853190', '6592424',
               '1827', 'D', '8160.00', '7960.00', '114312662654155', 'وسپهر', 'سرمايه گذاري مالي سپهرصادرات']
        self.assertEqual(calculationsData.candle_status(row), 1)
    #
    # def test_day_status(self):
    #     self.fail()
    #
    # def test_trend_status(self):
    #     self.fail()
    #
    # def test_avg_volume(self):
    #     self.fail()
    #
    # def test_min_percent_bear_trend(self):
    #     self.fail()
    #
    # def test_min_percent_bull_trend(self):
    #     self.fail()
    #
    # def test_last_lower_than_close(self):
    #     self.fail()
    #
    # def test_last_upper_than_close(self):
    #     self.fail()
    #
    # def test_cover2to1(self):
    #     self.fail()
    #
    # def test_min_body_bullish(self):
    #     self.fail()
    #
    # def test_min_body_bearish(self):
    #     self.fail()
    #
    # def test_have_up_shadow(self):
    #     self.fail()
    #
    # def test_have_down_shadow(self):
    #     self.fail()
    #
    # def test_have_up_shadow_min_percent(self):
    #     self.fail()
