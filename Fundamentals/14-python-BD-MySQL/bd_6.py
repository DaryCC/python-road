import mysql.connector

mi_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12",
    database="ecommerce")

mi_cursor = mi_db.cursor()

sql = """ DELETE FROM cliente
            WHERE nombre = %s """

valores = ("Carlos",)
mi_cursor.execute(sql, valores)
mi_db.commit()

mi_cursor.execute("SELECT * FROM cliente")
for reg in mi_cursor:
    print(reg)


mi_db.close()
