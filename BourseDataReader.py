import sqlite3

import requests

from DataExtractor import GetDataFromDB


class BourseDataReader:

    @staticmethod
    def get_excel():
        DbConnection = sqlite3.connect('example.db')
        cursor = DbConnection.cursor()

        cursor.execute("select * from id")
        count = 0

        rows = cursor.fetchall()
        print("Download started")
        size = len(rows)
        for row in rows:
            url = "http://old.tsetmc.com/tsev2/data/Export-txt.aspx?t=i&a=1&b=0&i=" + str(row[1])
            downloaded_file = requests.get(url)

            # create a new file with csv extension
            add = "./excel/" + str(row[1]) + ".csv"
            save_file = open(add, 'wb')

            # save file with content received from response
            save_file.write(downloaded_file.content)
            # close file
            save_file.close()
            count = count + 1
            a = count / size
            GetDataFromDB.update_progress(a)

        print("Download finished")

        DbConnection.close()
