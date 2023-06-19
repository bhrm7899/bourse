import sqlite3

from Analyzer import Analyzer
from BourseDataInserter import BourseDataInserter
from BourseDataReader import BourseDataReader
from DataExtractor import GetDataFromDB

if __name__ == '__main__':

    print("1- read bourse data")
    print("2- insert in to database")
    print("3- analyze stocks")
    print("4- exit")

    a = input('\nenter 1-4 :')
    while a != '4':
        if a == '1':
            BourseDataReader.get_excel()
            a = input('\n enter 1-4 :')
        if a == '2':
            BourseDataInserter.inserter()
            a = input('\n enter 1-4 :')
        if a == '3':
            connection = sqlite3.connect('example.db')
            cursor = connection.cursor()
            date = 20230219

            getDataDB = GetDataFromDB()
            getDataDB.get_names_of_companies_and_store(cursor)
            getDataDB.get_all_datas_and_store(cursor)
            Analyzer(date, getDataDB).find_today()
            a = input('\nenter 1-4 :')
        else:
            a = input('\nenter 1-4 :')
