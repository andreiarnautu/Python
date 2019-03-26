import sqlite3

def connect() :
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    connection.commit()
    connection.close()


def insert(title, author, year, isbn) :
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
    connection.commit()
    connection.close()


def view() :
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM book")
    rows = cursor.fetchall()

    connection.close()
    return rows


connect()
insert("Book#1", "John Cena", 2005, 89238929213)
print(view())
