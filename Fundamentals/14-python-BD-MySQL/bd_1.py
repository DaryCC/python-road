import mysql.connector

mi_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12"

    
)


mi_cursor = mi_db.cursor()

# sql="CREATE DATABASE ecommerce"
# mi_cursor.execute(sql)

# sql="DROP DATABASE ecommerce"
# mi_cursor.execute(sql)

sql="SHOW DATABASES"
mi_cursor.execute(sql)

for items in mi_cursor:
    print(items)


mi_db.close()