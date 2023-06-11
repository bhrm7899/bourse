from CalculationsData import CalculationsData
from DataCompany import DataCompany


class CheckCandleSymbol:
    def __init__(self):
        self.calculationsData = CalculationsData()
        self.r = 0

    @staticmethod
    def is_doji(row):
        body = DataCompany.get_body(row)
        diff = DataCompany.get_high(row) - DataCompany.get_low(row)

        if body < 0.2 * diff:
            return True
        else:
            return False

    @staticmethod
    def is_hammer_hanging_man(row):
        down_shadow = DataCompany.get_down_shadow(row)
        up_shadow = DataCompany.get_up_shadow(row)
        body = DataCompany.get_body(row)
        if down_shadow >= (2 * body) and up_shadow < (0.1 * down_shadow):
            return True
        else:
            return False

    def is_bearish_engulfing(self, row1, row2):
        if (self.calculationsData.candle_status(row1) != -1 or self.is_doji(
                row1)) and self.calculationsData.candle_status(row2) == -1 and \
                self.calculationsData.cover2to1(row1, row2):
            return True
        else:
            return False

    def is_bullish_engulfing(self, row1, row2):
        if (self.calculationsData.candle_status(row1) != 1 or self.is_doji(row1)) and \
                self.calculationsData.candle_status(row2) == 1 and self.calculationsData.cover2to1(row1, row2):
            return True
        else:
            return False

    def is_bullish_hammer_engulfing(self, row1, row2):
        if self.calculationsData.candle_status(row1) != 1 and self.calculationsData.candle_status(
                row2) == 1 and self.calculationsData.cover2to1(row1,
                                                               row2) and self.is_hammer_hanging_man(row1):
            return True
        else:
            return False

    def is_bearish_hammer_engulfing(self, row1, row2):
        if self.calculationsData.candle_status(row1) != -1 and self.calculationsData.candle_status(
                row2) == -1 and self.calculationsData.cover2to1(row1,
                                                                row2) and self.is_hammer_hanging_man(row1):
            return True
        else:
            return False

    def is_piercing_pattern(self, row1, row2):
        if self.calculationsData.candle_status(row1) != 1 and self.calculationsData.candle_status(
                row2) == 1 and DataCompany.get_first(
            row2) < DataCompany.get_last(row1) and DataCompany.get_last(row2) > (
                DataCompany.get_first(row1) + DataCompany.get_last(row1)) / 2:
            return True
        else:
            return False

    def is_morning_star(self, row1, row2, row3):
        if self.calculationsData.candle_status(row1) == -1 and self.calculationsData.candle_status(row3) == 1 and (
                2 * DataCompany.get_body(row2)) < DataCompany.get_body(row1) and (
                2 * DataCompany.get_body(row2)) < DataCompany.get_body(row3):
            if max(DataCompany.get_first(row2), DataCompany.get_last(row2)) < DataCompany.get_last(
                    row1) and DataCompany.get_last(row3) > (
                    DataCompany.get_first(row1) + DataCompany.get_last(row1)) / 2:
                return True
            else:
                return False
        else:
            return False

    @staticmethod
    def without_shadow(row):
        down_shadow = DataCompany.get_down_shadow(row)
        up_shadow = DataCompany.get_up_shadow(row)

        if down_shadow + up_shadow == 0:
            return True
        else:
            return False

    def full_time_buy_queue(self, row):
        low = DataCompany.get_low(row)
        high = DataCompany.get_high(row)

        if low == high and self.calculationsData.day_status(row) != -1 and high > DataCompany.get_open(row):
            return True
        else:
            return False

    def full_time_sell_queue(self, row):
        low = DataCompany.get_low(row)
        high = DataCompany.get_high(row)

        if low == high and self.calculationsData.day_status(row) != 1 and high < DataCompany.get_open(row):
            return True
        else:
            return False

    def is_full_time_queue(self, row):
        if self.full_time_sell_queue(row) or self.full_time_buy_queue(
                row):
            return True
        else:
            return False

    @staticmethod
    def is_full_time_queue_with_shadow(row):
        if DataCompany.get_first(row) == DataCompany.get_last(row) and DataCompany.get_low(
                row) < DataCompany.get_first(row):
            return True
        else:
            return False

    @staticmethod
    def is_bearish(rows):
        a = rows[0]
        maxData = DataCompany.get_close(rows[0])
        for i in rows:
            close = DataCompany.get_close(i)
            if maxData >= close:
                maxData = close
            else:
                return False
        return True
