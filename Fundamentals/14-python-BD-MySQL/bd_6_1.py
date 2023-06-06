import mysql.connector

mi_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12",
    database="ecommerce")

mi_cursor = mi_db.cursor()

sql = """ UPDATE cliente
            SET nombre = %s
            WHERE nombre = %s """

valores = ("Juan", "Anderson")
mi_cursor.execute(sql, valores)
mi_db.commit()

mi_cursor.execute("SELECT * FROM cliente")
for reg in mi_cursor:
    print(reg)


mi_db.close()
