import psycopg2

#  Function that creates a table.
def create_table():
    #  Connect to database
    #  Create a cursor object
    connection = psycopg2.connect("dbname='postgres' user='postgres' password='scouser' host='localhost' port='5432'")
    cursor = connection.cursor()
    #  Create database if it does not exist.
    cursor.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    connection.commit()
    connection.close()


#  Function that inserts a given element in the database.
def insert_element(item, quantity, price):
    connection = psycopg2.connect("dbname='postgres' user='postgres' password='scouser' host='localhost' port='5432'")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO store VALUES (%s, %s, %s)", (item, quantity, price))
    connection.commit()
    connection.close()


#  Function that deletes a given element from the database.
def delete_element(item):
    connection = psycopg2.connect("dbname='postgres' user='postgres' password='scouser' host='localhost' port='5432'")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM store WHERE item = %s", (item,))
    connection.commit()
    connection.close()


#  Function that updates the parameters of a given element
def update_element(item, quantity, price):
    connection = psycopg2.connect("dbname='postgres' user='postgres' password='scouser' host='localhost' port='5432'")
    cursor = connection.cursor()
    cursor.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s", (quantity, price, item))
    connection.commit()
    connection.close()


#  Function that allows us to see the content of the database.
def view() :
    connection = psycopg2.connect("dbname='postgres' user='postgres' password='scouser' host='localhost' port='5432'")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM store")
    rows = cursor.fetchall()
    connection.close()
    return rows


create_table()
delete_element("Liverpool T-Shirt")
insert_element("Liverpool T-Shirt", 200, 50.5)
print(view())
