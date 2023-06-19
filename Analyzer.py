from colorama import Fore

from ChartAnalyzer import ChartAnalyzer
# DataBase Functions
from CustomPrinter import CustomPrinter
from DataCompany import DataCompany
from PatternRecognizer import PatternRecognizer


class Analyzer:

    def __init__(self, date, getDataDB):
        self.calculationsData = ChartAnalyzer()
        self.checkCandleSymbol = PatternRecognizer()
        self.date = date
        self.getDataDB = getDataDB

    def find_today(self):

        name_bullish, count_bullish = self.bullish_engulfing()

        self.bullish_engulfing_with_five_min_percent_body()

        self.hammer_and_bullish_engulfing()

        self.bearish_and_engulfing()

        self.bearish_and_hammer_and_engulfing()

        self.bearish_and_engulfing_and_volume()

        self.piercing_pattern_print()

        self.bearish_and_piercing_pattern()

        self.bearish_and_piercing_pattern_and_volume()

        self.bearish_and_morning_star()

        name_bearish, count_bearish = self.bearish_engulfing()

        self.hanging_man_and_bearish_engulfing()

        self.full_time_buy_queue()

        self.full_time_sell_queue()

        self.full_time_buy_queue_with_shadow()

        Analyzer.check_index_status(count_bearish, count_bullish)

    def bullish_engulfing(self):
        count = 0
        CustomPrinter.println("Bullish engulfing:", Fore.BLUE)  # pass
        results = list()
        for i in self.getDataDB.stock_names:
            company = self.getDataDB.final_data[i]
            date_index = self.check(company)
            if len(company) > date_index + 2:
                if date_index != -1 and self.checkCandleSymbol.is_bullish_engulfing(company[-date_index - 1],
                                                                                    company[-date_index]):
                    count += 1
                    result = i + " : " + str(count)
                    results.append(result)
                    CustomPrinter.print(i, Fore.CYAN)
                    CustomPrinter.println("   : " + str(count), Fore.YELLOW)
        return results, count

    def bullish_engulfing_with_five_min_percent_body(self):
        count = 0
        CustomPrinter.println("Bullish engulfing with min 5 percent body:", Fore.BLUE)  # pass
        results = list()
        for i in self.getDataDB.stock_names:
            company = self.getDataDB.final_data[i]
            date_index = self.check(company)
            if len(company) > date_index + 10:
                if date_index != -1 and self.checkCandleSymbol.is_bullish_engulfing(company[-date_index - 1],
                                                                                    company[
                                                                                        -date_index]) and \
                        self.calculationsData.min_body_bullish(company[-date_index], 5):
                    count += 1
                    result = i + " : " + str(count)
                    results.append(result)
                    CustomPrinter.print(i, Fore.CYAN)
                    CustomPrinter.println("   : " + str(count), Fore.YELLOW)
        return results

    def hammer_and_bullish_engulfing(self):
        count = 0
        CustomPrinter.println("hammer and bullish engulfing:", Fore.BLUE)  # pass
        results = list()
        for i in self.getDataDB.stock_names:
            company = self.getDataDB.final_data[i]
            date_index = self.check(company)
            if len(company) > date_index + 2:
                if date_index != -1 and self.checkCandleSymbol.is_bullish_hammer_engulfing(company[-date_index - 1],
                                                                                           company[
                                                                                               -date_index]):
                    count += 1
                    result = i + " : " + str(count)
                    results.append(result)
                    CustomPrinter.print(i, Fore.CYAN)
                    CustomPrinter.println("   : " + str(count), Fore.YELLOW)
        return results

    def bearish_and_engulfing(self):
        count = 0
        CustomPrinter.println("bearish and bullish engulfing :", Fore.BLUE)
        results = list()
        for i in self.getDataDB.stock_names:
            company = self.getDataDB.final_data[i]
            date_index = self.check(company)
            if len(company) > date_index + 10:
                if date_index != -1 and self.checkCandleSymbol.is_bullish_engulfing(company[-date_index - 1],
                                                                                    company[
                                                                                        -date_index]) \
                        and self.checkCandleSymbol.is_bearish(company[-date_index - 3: -date_index - 1]):
                    count += 1
                    result = i + " : " + str(count)
                    results.append(result)
                    CustomPrinter.print(i, Fore.CYAN)
                    CustomPrinter.println("   : " + str(count), Fore.YELLOW)
        return results

    def bearish_and_hammer_and_engulfing(self):
        count = 0
        CustomPrinter.println("bearish and hammer and bullish engulfing :", Fore.BLUE)
        results = list()
        for i in self.getDataDB.stock_names:
            company = self.getDataDB.final_data[i]
            date_index = self.check(company)
            if len(company) > date_index + 10:
                if date_index != -1 and self.checkCandleSymbol.is_bullish_hammer_engulfing(company[-date_index - 1],
                                                                                           company[
                                                                                               -date_index]) \
                        and self.checkCandleSymbol.is_bearish(company[-date_index - 3: -date_index - 1]):
                    count += 1
                    result = i + " : " + str(count)
                    results.append(result)
                    CustomPrinter.print(i, Fore.CYAN)
                    CustomPrinter.println("   : " + str(count), Fore.YELLOW)
        return results

    def bearish_and_engulfing_and_volume(self):
        count = 0
        CustomPrinter.println("bearish and bullish engulfing with volume:", Fore.BLUE)
        results = list()
        for i in self.getDataDB.stock_names:
            company = self.getDataDB.final_data[i]
            date_index = self.check(company)
            if len(company) > date_index + 35:
                vol1 = DataCompany.get_volume(company[-1])
                if date_index != -1 and self.checkCandleSymbol.is_bullish_engulfing(company[-date_index - 1],
                                                                                    company[
                                                                                        -date_index]) \
                        and self.checkCandleSymbol.is_bearish(company[-date_index - 3:-date_index - 1]) and vol1 > (
                        1.5 * self.calculationsData.avg_volume(company[-date_index - 29: -date_index - 1])):
                    count += 1
                    result = i + " : " + str(count)
                    results.append(result)
                    CustomPrinter.print(i, Fore.CYAN)
                    CustomPrinter.println("   : " + str(count), Fore.YELLOW)
        return results

    def piercing_pattern_print(self):
        count = 0
        CustomPrinter.println("piercingPattern:", Fore.BLUE)  # pass
        results = list()
        for i in self.getDataDB.stock_names:
            company = self.getDataDB.final_data[i]
            date_index = self.check(company)
            if len(company) > date_index + 2:
                if date_index != -1 and self.checkCandleSymbol.is_piercing_pattern(company[-date_index - 1],
                                                                                   company[-date_index]):
                    count += 1
                    result = i + " : " + str(count)
                    results.append(result)
                    CustomPrinter.print(i, Fore.CYAN)
                    CustomPrinter.println("   : " + str(count), Fore.YELLOW)
        return results

    def bearish_and_piercing_pattern(self):
        count = 0
        CustomPrinter.println("bearish and piercingPattern:", Fore.BLUE)
        results = list()
        for i in self.getDataDB.stock_names:
            company = self.getDataDB.final_data[i]
            date_index = self.check(company)
            if len(company) > date_index + 10:
                if date_index != -1 and self.checkCandleSymbol.is_piercing_pattern(company[-date_index - 1],
                                                                                   company[
                                                                                       -date_index]) and \
                        self.checkCandleSymbol.is_bearish(company[-date_index - 3:-date_index - 1]):
                    count += 1
                    result = i + " : " + str(count)
                    results.append(result)
                    CustomPrinter.print(i, Fore.CYAN)
                    CustomPrinter.println("   : " + str(count), Fore.YELLOW)
        return results

    def bearish_and_piercing_pattern_and_volume(self):
        count = 0
        CustomPrinter.println("bearish and piercingPattern with volume:", Fore.BLUE)
        results = list()
        for i in self.getDataDB.stock_names:
            company = self.getDataDB.final_data[i]
            date_index = self.check(company)
            if len(company) > date_index + 35:
                vol1 = DataCompany.get_volume(company[-1])
                if date_index != -1 and self.checkCandleSymbol.is_piercing_pattern(company[-date_index - 1],
                                                                                   company[
                                                                                       -date_index]) and \
                        self.checkCandleSymbol.is_bearish(company[-date_index - 3:-date_index - 1]) and vol1 > (
                        1.5 * self.calculationsData.avg_volume(company[-date_index - 29:-date_index - 1])):
                    count += 1
                    result = i + " : " + str(count)
                    results.append(result)
                    CustomPrinter.print(i, Fore.CYAN)
                    CustomPrinter.println("   : " + str(count), Fore.YELLOW)
        return results

    def bearish_and_morning_star(self):
        count = 0
        CustomPrinter.println("bearish and MorningStar:", Fore.BLUE)
        results = list()
        for i in self.getDataDB.stock_names:
            company = self.getDataDB.final_data[i]
            date_index = self.check(company)
            if len(company) > date_index + 15:
                if date_index != -1 and self.checkCandleSymbol.is_morning_star(company[-date_index - 2],
                                                                               company[-date_index - 1],
                                                                               company[
                                                                                   -date_index]) and \
                        self.checkCandleSymbol.is_bearish(company[-date_index - 5:-date_index - 3]):
                    count += 1
                    result = i + " : " + str(count)
                    results.append(result)
                    CustomPrinter.print(i, Fore.CYAN)
                    CustomPrinter.println("   : " + str(count), Fore.YELLOW)
        return results

    def bearish_engulfing(self):
        count = 0
        CustomPrinter.println("Bearish engulfing:", Fore.BLUE)
        results = list()
        for i in self.getDataDB.stock_names:
            company = self.getDataDB.final_data[i]
            date_index = self.check(company)
            if len(company) > date_index + 2:
                if date_index != -1 and self.checkCandleSymbol.is_bearish_engulfing(company[-date_index - 1],
                                                                                    company[-date_index]):
                    count += 1
                    result = i + " : " + str(count)
                    results.append(result)
                    CustomPrinter.print(i, Fore.CYAN)
                    CustomPrinter.println("   : " + str(count), Fore.YELLOW)
        return results, count

    def hanging_man_and_bearish_engulfing(self):
        count = 0
        CustomPrinter.println("hanging man and bearish engulfing:", Fore.BLUE)
        results = list()
        for i in self.getDataDB.stock_names:
            company = self.getDataDB.final_data[i]
            date_index = self.check(company)
            if len(company) > date_index + 2:
                if date_index != -1 and self.checkCandleSymbol.is_bearish_hammer_engulfing(company[-date_index - 1],
                                                                                           company[
                                                                                               -date_index]):
                    count += 1
                    result = i + " : " + str(count)
                    results.append(result)
                    CustomPrinter.print(i, Fore.CYAN)
                    CustomPrinter.println("   : " + str(count), Fore.YELLOW)
        return results

    def full_time_buy_queue(self):
        count = 0
        CustomPrinter.println("buyQueue in some days:", Fore.BLUE)
        results = list()
        for i in self.getDataDB.stock_names:
            company = self.getDataDB.final_data[i]
            date_index = self.check(company)
            if len(company) > date_index + 2:
                if date_index != -1 and self.checkCandleSymbol.full_time_buy_queue(company[-date_index]):
                    count += 1
                    result = i + " : " + str(count)
                    results.append(result)
                    CustomPrinter.print(i, Fore.CYAN)
                    CustomPrinter.println("   : " + str(count), Fore.YELLOW)
        return results

    def full_time_sell_queue(self):
        count = 0
        CustomPrinter.println("sellQueue in some days:", Fore.BLUE)
        results = []
        for i in self.getDataDB.stock_names:
            company = self.getDataDB.final_data[i]
            date_index = self.check(company)
            if len(company) > date_index + 2:
                if date_index != -1 and self.checkCandleSymbol.full_time_sell_queue(company[-date_index]):
                    count += 1
                    result = i + " : " + str(count)
                    results.append(result)
                    CustomPrinter.print(i, Fore.CYAN)
                    CustomPrinter.println("   : " + str(count), Fore.YELLOW)
        return results

    def full_time_buy_queue_with_shadow(self):
        count = 0
        CustomPrinter.println("fullTime buyQueue with shadow:", Fore.BLUE)
        results = list()
        for i in self.getDataDB.stock_names:
            company = self.getDataDB.final_data[i]
            date_index = self.check(company)
            if len(company) > date_index + 2:
                if date_index != -1 and self.checkCandleSymbol.is_full_time_queue_with_shadow(
                        company[-date_index]):
                    count += 1
                    result = i + " : " + str(count)
                    results.append(result)
                    CustomPrinter.print(i, Fore.CYAN)
                    CustomPrinter.println("   : " + str(count), Fore.YELLOW)
        return results

    def check(self, company):
        date_index = -1
        for i in range(1, len(company)):
            if DataCompany.get_date(company[0 - i]) == self.date:
                date_index = i
                return date_index
        return date_index

    @staticmethod
    def check_index_status(count_bearish, count_bullish):
        if count_bearish * 1.3 < count_bullish:
            CustomPrinter.println("Tomorrow's index will be probably green", Fore.GREEN)
            return "green"
        if count_bearish > count_bullish * 1.3:
            CustomPrinter.println("Tomorrow's index will be probably red", Fore.RED)
            return "red"
        CustomPrinter.println("It is not possible to comment on tomorrow's index", Fore.LIGHTYELLOW_EX)
        return "-1"
