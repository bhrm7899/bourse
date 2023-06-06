from CalculationsData import CalculationsData
from CheckCandleSymbol import CheckCandleSymbol
from Const import Const
from DataCompany import DataCompany


# DataBase Functions
class Strategies:

    def __init__(self, date, getDataDB):
        self.calculationsData = CalculationsData()
        self.checkCandleSymbol = CheckCandleSymbol()
        self.data_company = DataCompany()
        self.date = date
        self.getDataDB = getDataDB

    def find_today(self):

        self.bullish_engulfing_print()

        self.bullish_engulfing_with_five_min_percent_body()

        self.hammer_and_bullish_engulfing()

        self.bearish_and_engulfing()

        self.bearish_and_hammer_and_engulfing()

        self.bearish_and_engulfing_and_volume()

        self.piercing_pattern_print()

        self.bearish_and_piercing_pattern()

        self.bearish_and_piercing_pattern_and_volume()

        self.bearish_and_morning_star()

        self.bearish_engulfing_print()

        self.hammer_and_bearish_engulfing()

        self.full_time_buy_queue()

        self.full_time_sell_queue()

        self.full_time_buy_queue_with_shadow()

    def bullish_engulfing_print(self):
        print(Const.star)
        count = 0
        print("Bullish engulfing print :")  # pass
        for i in self.getDataDB.stock_names:
            company = self.getDataDB.final_data[i]
            date_index = self.check(company)
            if len(company) > date_index + 2:
                if date_index != -1 and self.checkCandleSymbol.is_bullish_engulfing(company[-date_index - 1],
                                                                                    company[-date_index]):
                    count += 1
                    print(count, " : ", i)

    def bullish_engulfing_with_five_min_percent_body(self):
        print(Const.star)
        count = 0
        print("Bullish engulfing with min 5 percent body print :")  # pass
        for i in self.getDataDB.stock_names:
            company = self.getDataDB.final_data[i]
            date_index = self.check(company)
            if len(company) > date_index + 10:
                if date_index != -1 and self.checkCandleSymbol.is_bullish_engulfing(company[-date_index - 1],
                                                                                    company[
                                                                                        -date_index]) and self.calculationsData.min_body_bullish(
                    company[-date_index], 5):
                    count += 1
                    print(count, " : ", i)

    def hammer_and_bullish_engulfing(self):
        print(Const.star)
        count = 0
        print("hammer and bullish engulfing :")  # pass
        for i in self.getDataDB.stock_names:
            company = self.getDataDB.final_data[i]
            date_index = self.check(company)
            if len(company) > date_index + 2:
                if date_index != -1 and self.checkCandleSymbol.is_bullish_hammer_engulfing(company[-date_index - 1],
                                                                                           company[
                                                                                               -date_index]):
                    count += 1
                    print(count, " : ", i)

    def bearish_and_engulfing(self):
        print(Const.star)
        count = 0
        print("is bearish and engulfing :")
        for i in self.getDataDB.stock_names:
            company = self.getDataDB.final_data[i]
            date_index = self.check(company)
            if len(company) > date_index + 10:
                if date_index != -1 and self.checkCandleSymbol.is_bullish_engulfing(company[-date_index - 1],
                                                                                    company[
                                                                                        -date_index]) and self.checkCandleSymbol.is_bearish(
                    company[-date_index - 3: -date_index - 1]):
                    count += 1
                    print(count, " : ", i)

    def bearish_and_hammer_and_engulfing(self):
        print(Const.star)
        count = 0
        print("is bearish and hammer and engulfing :")
        for i in self.getDataDB.stock_names:
            company = self.getDataDB.final_data[i]
            date_index = self.check(company)
            if len(company) > date_index + 10:
                if date_index != -1 and self.checkCandleSymbol.is_bullish_hammer_engulfing(company[-date_index - 1],
                                                                                           company[
                                                                                               -date_index]) and self.checkCandleSymbol.is_bearish(
                    company[-date_index - 3: -date_index - 1]):
                    count += 1
                    print(count, " : ", i)

    def bearish_and_engulfing_and_volume(self):
        print(Const.star)
        count = 0
        print("is bearish and engulfing and volume:")
        for i in self.getDataDB.stock_names:
            company = self.getDataDB.final_data[i]
            date_index = self.check(company)
            if len(company) > date_index + 35:
                vol1 = self.data_company.get_volume(company[-1])
                if date_index != -1 and self.checkCandleSymbol.is_bullish_engulfing(company[-date_index - 1],
                                                                                    company[
                                                                                        -date_index]) and self.checkCandleSymbol.is_bearish(
                    company[-date_index - 3:-date_index - 1]) and vol1 > (
                        1.5 * self.calculationsData.avg_volume(company[-date_index - 29: -date_index - 1])):
                    count += 1
                    print(count, " : ", i)

    def piercing_pattern_print(self):
        print(Const.star)
        count = 0
        print("piercingPattern print :")  # pass
        for i in self.getDataDB.stock_names:
            company = self.getDataDB.final_data[i]
            date_index = self.check(company)
            if len(company) > date_index + 2:
                if date_index != -1 and self.checkCandleSymbol.is_piercing_pattern(company[-date_index - 1],
                                                                                   company[-date_index]):
                    count += 1
                    print(count, " : ", i)

    def bearish_and_piercing_pattern(self):
        print(Const.star)
        count = 0
        print("is bearish and piercingPattern :")
        for i in self.getDataDB.stock_names:
            company = self.getDataDB.final_data[i]
            date_index = self.check(company)
            if len(company) > date_index + 10:
                if date_index != -1 and self.checkCandleSymbol.is_piercing_pattern(company[-date_index - 1],
                                                                                   company[
                                                                                       -date_index]) and self.checkCandleSymbol.is_bearish(
                    company[-date_index - 3:-date_index - 1]):
                    count += 1
                    print(count, " : ", i)

    def bearish_and_piercing_pattern_and_volume(self):
        print(Const.star)
        count = 0
        print("is bearish and piercingPattern and volume:")
        for i in self.getDataDB.stock_names:
            company = self.getDataDB.final_data[i]
            date_index = self.check(company)
            if len(company) > date_index + 35:
                vol1 = self.data_company.get_volume(company[-1])
                if date_index != -1 and self.checkCandleSymbol.is_piercing_pattern(company[-date_index - 1],
                                                                                   company[
                                                                                       -date_index]) and self.checkCandleSymbol.is_bearish(
                    company[-date_index - 3:-date_index - 1]) and vol1 > (
                        1.5 * self.calculationsData.avg_volume(company[-date_index - 29:-date_index - 1])):
                    count += 1
                    print(count, " : ", i)

    def bearish_and_morning_star(self):
        print(Const.star)
        count = 0
        print("is bearish and MorningStar :")
        for i in self.getDataDB.stock_names:
            company = self.getDataDB.final_data[i]
            date_index = self.check(company)
            if len(company) > date_index + 15:
                if date_index != -1 and self.checkCandleSymbol.is_morning_star(company[-date_index - 2],
                                                                               company[-date_index - 1],
                                                                               company[
                                                                                   -date_index]) and self.checkCandleSymbol.is_bearish(
                    company[-date_index - 5:-date_index - 3]):
                    count += 1
                    print(count, " : ", i)

    def bearish_engulfing_print(self):
        print(Const.star)
        count = 0
        print("Bearish engulfing print :")
        for i in self.getDataDB.stock_names:
            company = self.getDataDB.final_data[i]
            date_index = self.check(company)
            if len(company) > date_index + 2:
                if date_index != -1 and self.checkCandleSymbol.is_bearish_engulfing(company[-date_index - 1],
                                                                                    company[-date_index]):
                    count += 1
                    print(count, " : ", i)

    def hammer_and_bearish_engulfing(self):
        print(Const.star)
        count = 0
        print("hammer and bearish engulfing :")
        for i in self.getDataDB.stock_names:
            company = self.getDataDB.final_data[i]
            date_index = self.check(company)
            if len(company) > date_index + 2:
                if date_index != -1 and self.checkCandleSymbol.is_bearish_hammer_engulfing(company[-date_index - 1],
                                                                                           company[
                                                                                               -date_index]):
                    count += 1
                    print(count, " : ", i)

    def full_time_buy_queue(self):
        print(Const.star)
        count = 0
        print("fullTime buyQueue :")
        for i in self.getDataDB.stock_names:
            company = self.getDataDB.final_data[i]
            date_index = self.check(company)
            if len(company) > date_index + 2:
                if date_index != -1 and self.checkCandleSymbol.full_time_buy_queue(company[-date_index]):
                    count += 1
                    print(count, " : ", i)

    def full_time_sell_queue(self):
        print(Const.star)
        count = 0
        print("fullTime sellQueue :")
        for i in self.getDataDB.stock_names:
            company = self.getDataDB.final_data[i]
            date_index = self.check(company)
            if len(company) > date_index + 2:
                if date_index != -1 and self.checkCandleSymbol.full_time_sell_queue(company[-date_index]):
                    count += 1
                    print(count, " : ", i)

    def full_time_buy_queue_with_shadow(self):
        print(Const.star)
        count = 0
        print("fullTime buyQueue with shadow :")
        for i in self.getDataDB.stock_names:
            company = self.getDataDB.final_data[i]
            date_index = self.check(company)
            if len(company) > date_index + 2:
                if date_index != -1 and self.checkCandleSymbol.is_full_time_queue_with_shadow(
                        company[-date_index]):
                    count += 1
                    print(count, " : ", i)

    def check(self, company):
        date_index = -1
        for i in range(1, len(company)):
            if self.data_company.get_date(company[0 - i]) == self.date:
                date_index = i
                return date_index
        return date_index
