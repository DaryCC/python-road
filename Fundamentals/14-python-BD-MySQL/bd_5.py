import mysql.connector

mi_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12",
    database="ecommerce")

mi_cursor = mi_db.cursor()

#sql = """SELECT * FROM cliente"""

#sql = """ SELECT nombre, apellido FROM cliente """

#sql = """ SELECT nombre, apellido FROM cliente
#            WHERE nombre = 'Maria' """

sql = """ SELECT nombre, apellido FROM cliente
            WHERE nombre = %s """

valores = ("Pedro",)
mi_cursor.execute(sql, valores)



for reg in mi_cursor:
    print(reg)


mi_db.close()
