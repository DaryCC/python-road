import mysql.connector

my_db= mysql.connector.connect(
    host="localhost",
    user="root",
    password="12",
    database="ecommerce"
)

mi_cursor=my_db.cursor()

query="""CREATE TABLE cliente(
    nombre VARCHAR(255),
    apellido VARCHAR(255))"""

mi_cursor.execute(query)

# query="""DROP TABLE IF EXISTS cliente"""
# mi_cursor.execute(query)

mi_cursor.execute("show tables")
for tablas in mi_cursor:
    print (tablas)

mi_cursor.close()