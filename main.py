import sqlite3

from GetDataFromDB import GetDataFromDB
from Strategies import Strategies

if __name__ == '__main__':
    connection = sqlite3.connect('example.db')
    cursor = connection.cursor()

    date = 20230219
    TestDate = 20230124

    getDataDB = GetDataFromDB()
    getDataDB.get_names_of_companies_and_store(cursor)
    getDataDB.get_all_datas_and_store(cursor)
    Strategies(date, getDataDB).find_today()
