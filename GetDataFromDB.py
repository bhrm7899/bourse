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
        print(len(self.stock_names))

    def get_all_datas_and_store(self, cursor):
        count = 0
        for i in self.stock_names:
            count += 1
            line = "SELECT * FROM tbl_data t WHERE t.name = '" + i + "' ORDER BY DTYYYYMMDD"
            cursor.execute(line)
            rows = cursor.fetchall()
            new_list = list()
            for row in rows:
                new_list.append(row)
            self.final_data[i] = new_list
            print(count)
