from DataCompany import DataCompany


class CalculationsData:

    def candle_status(self, row):  # common
        if float(row[11]) > float(row[2]):
            return 1  # green
        elif float(row[11]) < float(row[2]):
            return -1
        else:
            return 0

    def day_status(self, row):  # stop price
        if float(row[5]) > float(row[10]):
            return 1  # green
        elif float(row[5]) < float(row[10]):
            return -1
        else:
            return 0

    def trend_status(self, row1, row2):  # close stop price
        if float(row2[5]) > float(row1[5]):
            return 1  # bullish
        elif float(row2[5]) < float(row1[5]):
            return -1
        else:
            return 0

    def avg_volume(self, rows):
        sum_avg = 0
        for row in rows:
            sum_avg += int(row[7])
        avg = sum_avg / len(rows)
        return avg

    def min_percent_bear_trend(self, row1, row2, percent):
        if float(row2[5]) <= float(row1[5]) - (percent * float(row1[5])):
            return True
        else:
            return False

    def min_percent_bull_trend(self, row1, row2, percent):
        if float(row2[5]) >= float(row1[5]) + ((percent / 100) * float(row1[5])):
            return True
        else:
            return False

    def last_lower_than_close(self, row, percent):
        data_company = DataCompany()
        last = data_company.get_last(row)
        close = data_company.get_close(row)
        if last + ((percent / 100) * last) <= close:
            return True
        else:
            return False

    def last_upper_than_close(self, row, percent):
        data_company = DataCompany()
        last = data_company.get_last(row)
        close = data_company.get_close(row)
        if last - ((percent / 100) * last) >= close:
            return True
        else:
            return False

    def cover2to1(self, row1, row2):
        data_company = DataCompany()
        first1 = data_company.get_first(row1)
        first2 = data_company.get_first(row2)
        last1 = data_company.get_last(row1)
        last2 = data_company.get_last(row2)
        if max(first2, last2) > max(first1, last1) and min(first2, last2) < min(first1, last1):
            return True
        else:
            return False

    def min_body_bullish(self, row, percent):
        data_company = DataCompany()
        first = data_company.get_first(row)
        last = data_company.get_last(row)
        if last > first + (first * (percent / 100)):
            return True
        else:
            return False

    def min_body_bearish(self, row, percent):
        data_company = DataCompany()
        first = data_company.get_first(row)
        last = data_company.get_last(row)
        if last < first - (first * (percent / 100)):
            return True
        else:
            return False

    def have_up_shadow(self, row):
        data_company = DataCompany()
        tmp = data_company.get_up_shadow(row)
        if tmp != 0:
            return True
        else:
            return False

    def have_down_shadow(self, row):
        data_company = DataCompany()
        tmp = data_company.get_down_shadow(row)
        if tmp != 0:
            return True
        else:
            return False

    def have_up_shadow_min_percent(self, row, min_percent):
        data_company = DataCompany()
        _max = max(data_company.get_first(row), data_company.get_last(row))
        if data_company.get_high(row) > _max + (_max * min_percent / 100):
            return True
        else:
            return False
