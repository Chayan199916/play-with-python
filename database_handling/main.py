import sqlite3

def createTable():
    conn = sqlite3.connect('demo.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS STORE (ITEM TEXT, PRICE REAL, NO_OF_ITEMS INTEGER)")
    conn.commit()
    conn.close()

def insertIntoTable(item, price, no):
    conn = sqlite3.connect('demo.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO STORE VALUES(?, ?, ?)", (item, price, no))
    conn.commit()
    conn.close() 

def showData():
    conn = sqlite3.connect('demo.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM STORE")
    rows = cur.fetchall()
    conn.close()
    return rows

def deleteData(item):
    conn = sqlite3.connect('demo.db')
    cur = conn.cursor()
    obj = cur.execute("DELETE FROM STORE WHERE ITEM = ?", (item,))
    print(obj)
    conn.commit()
    conn.close()

def updateData(item, price, no):
    conn = sqlite3.connect('demo.db')
    cur = conn.cursor()
    cur.execute("UPDATE STORE SET PRICE = ?, NO_OF_ITEMS = ? WHERE ITEM = ?", (price, no, item))
    conn.commit()
    conn.close()

if __name__ == "__main__":

    # createTable()
    # insertIntoTable('pen', 20, 2)
    # insertIntoTable('pencil', 10, 4)
    # insertIntoTable('eraser', 5, 5)
    # insertIntoTable('sharpner', 5, 10)
    # print(showData())
    # updateData('pencil', 8, 9)
    deleteData('pencil')