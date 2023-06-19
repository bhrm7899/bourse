import sys

from colorama import Fore

from CustomPrinter import CustomPrinter


class GetDataFromDB:

    def __init__(self):
        self.stock_names = list()
        self.final_data = dict()

    def get_names_of_companies_and_store(self, cursor):
        names_query = "SELECT DISTINCT t.name FROM tbl_data t"
        cursor.execute(names_query)
        rows = cursor.fetchall()
        for row in rows:
            self.stock_names.append(row[0])

    def get_all_datas_and_store(self, cursor):
        CustomPrinter.println("start", Fore.GREEN)
        count = 0
        size = len(self.stock_names)
        for i in self.stock_names:
            count += 1
            line = "SELECT * FROM tbl_data t WHERE t.name = '" + i + "' ORDER BY DTYYYYMMDD"
            cursor.execute(line)
            rows = cursor.fetchall()
            new_list = list()
            for row in rows:
                new_list.append(row)
            self.final_data[i] = new_list
            a = count / size
            GetDataFromDB.update_progress(a)
            # print(count)

    @staticmethod
    def update_progress(progress):
        barLength = 100  # Modify this to change the length of the progress bar
        status = ""
        if isinstance(progress, int):
            progress = float(progress)
        if not isinstance(progress, float):
            progress = 0
            status = "error: progress var must be float\r\n"
        if progress < 0:
            progress = 0
            status = "Halt...\r\n"
        if progress >= 1:
            progress = 1
            status = "Done...\r\n"
        block = int(round(barLength * progress))
        text = "\rPercent: [{0}] {1}% {2}".format("#" * block + "-" * (barLength - block),
                                                  "{:.2f}".format(round(progress * 100, 2)), status)
        sys.stdout.write(text)
        sys.stdout.flush()
