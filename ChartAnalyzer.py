from DataCompany import DataCompany


class ChartAnalyzer:

    def __init__(self):
        self.r = 0

    @staticmethod
    def candle_status(row):
        if float(row[11]) > float(row[2]):
            return 1
        elif float(row[11]) < float(row[2]):
            return -1
        else:
            return 0

    @staticmethod
    def day_status(row):
        if float(row[5]) > float(row[10]):
            return 1
        elif float(row[5]) < float(row[10]):
            return -1
        else:
            return 0

    @staticmethod
    def trend_status(row1, row2):
        if float(row2[5]) > float(row1[5]):
            return 1
        elif float(row2[5]) < float(row1[5]):
            return -1
        else:
            return 0

    @staticmethod
    def avg_volume(rows):
        sum_avg = 0
        for row in rows:
            sum_avg += int(row[7])
        avg = sum_avg / len(rows)
        return avg

    @staticmethod
    def min_percent_bear_trend(row1, row2, percent):
        if float(row2[5]) <= float(row1[5]) - (percent * float(row1[5])):
            return True
        else:
            return False

    @staticmethod
    def min_percent_bull_trend(row1, row2, percent):
        if float(row2[5]) >= float(row1[5]) + ((percent / 100) * float(row1[5])):
            return True
        else:
            return False

    @staticmethod
    def last_lower_than_close(row, percent):
        last = DataCompany.get_last(row)
        close = DataCompany.get_close(row)
        if last + ((percent / 100) * last) <= close:
            return True
        else:
            return False

    @staticmethod
    def last_upper_than_close(row, percent):
        last = DataCompany.get_last(row)
        close = DataCompany.get_close(row)
        if last - ((percent / 100) * last) >= close:
            return True
        else:
            return False

    @staticmethod
    def cover2to1(row1, row2):
        first1 = DataCompany.get_first(row1)
        first2 = DataCompany.get_first(row2)
        last1 = DataCompany.get_last(row1)
        last2 = DataCompany.get_last(row2)
        if max(first2, last2) > max(first1, last1) and min(first2, last2) < min(first1, last1):
            return True
        else:
            return False

    @staticmethod
    def min_body_bullish(row, percent):
        first = DataCompany.get_first(row)
        last = DataCompany.get_last(row)
        if last > first + (first * (percent / 100)):
            return True
        else:
            return False

    @staticmethod
    def min_body_bearish(row, percent):
        first = DataCompany.get_first(row)
        last = DataCompany.get_last(row)
        if last < first - (first * (percent / 100)):
            return True
        else:
            return False

    @staticmethod
    def have_up_shadow(row):
        tmp = DataCompany.get_up_shadow(row)
        if tmp != 0:
            return True
        else:
            return False

    @staticmethod
    def have_down_shadow(row):
        tmp = DataCompany.get_down_shadow(row)
        if tmp != 0:
            return True
        else:
            return False

    @staticmethod
    def have_up_shadow_min_percent(row, min_percent):
        _max = max(DataCompany.get_first(row), DataCompany.get_last(row))
        if DataCompany.get_high(row) > _max + (_max * min_percent / 100):
            return True
        else:
            return False
