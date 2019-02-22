import sqlite3


def create_table():
    #  Connect to database
    #  Create a cursor object
    connection = sqlite3.connect("lite.db")
    cursor = connection.cursor()

    #  Create database if it does not exist.
    cursor.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    connection.commit()
    connection.close()


def insert_element(item, quantity, price):
    connection = sqlite3.connect("lite.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO store VALUES (?, ?, ?)", (item, quantity, price))
    connection.commit()
    connection.close()


def view() :
    connection = sqlite3.connect("lite.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM store")
    rows = cursor.fetchall()
    connection.close()
    return rows

create_table()
insert_element("Liverpool T-Shirt", 100, 20)
insert_element("Arsenal T-Shirt", 40, 20)
insert_element("Barcelona T-Shirt", 80, 20)
print(view())