import sqlite3


def create_table():
    #  Connect to database
    #  Create a cursor object
    connection = sqlite3.connect("lite.db")
    cursor = connection.cursor()

    #  Create database if it does not exist.
    cursor.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    #  Add data to the database.
    cursor.execute("INSERT INTO store VALUES ('Wine Glass', 5, 10.5)")
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


print(view())