# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.



# Press the green button in the gutter to run the script.

import csv

import sqlite3

if __name__ == '__main__':


    import sqlite3

    # create a data structure
    conn = sqlite3.connect('example.db')
    c = conn.cursor()

    c.execute("select * from id")

    rows = c.fetchall()
    count = 0

    c.execute("DELETE FROM tbl_data")
    conn.commit()

    for ro in rows:



        with open('%s.csv' % ro[1]) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    try:
                        c.execute("INSERT INTO tbl_data(TICKER,DTYYYYMMDD,FIRST,HIGH,LOW,"
                                  "CLOSE,VALUE,VOL,OPENINT,PER,OPEN,LAST,idSite,name,bigname)"
                                  " VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                                  (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9],
                                   row[10], row[11],ro[1], ro[2], ro[3]))
                        conn.commit()
                    except sqlite3.Error as error:
                        ss = error
                        ssss = "dsc"
                    line_count += 1
        print("Number : " , count ,"ID site : " , ro[1])
        count += 1


    conn.close()