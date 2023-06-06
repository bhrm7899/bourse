import sqlite3

if __name__ == '__main__':

    # create a data structure
    DbConnection = sqlite3.connect('example.db')
    cursor = DbConnection.cursor()

    cursor.execute("select * from id")
    count = 0

    rows = cursor.fetchall()
    print("Download started")
    for row in rows:

        import requests
        
        id = "http://www.tsetmc.com/tsev2/data/Export-txt.aspx?t=i&a=1&b=0&i={addres}".format(addres=row[1])
        print("trying")
        downloaded_file = requests.get(id)
        
        # create a new file with jpg extension
        add = "{name}.csv".format(name=row[1])
        save_file = open(add, 'wb')
        
        # save file with content received from response
        save_file.write(downloaded_file.content)
        # close file
        save_file.close()
        count = count + 1
        print("Number : ", count)

    print("Download finished")

    DbConnection.close()
