import mysql.connector

my_db= mysql.connector.connect(
    host="localhost",
    user="root",
    password="12",
    database="ecommerce"
)

cursor= my_db.cursor()

query="""ALTER TABLE cliente  ADD cliente_id INT AUTO_INCREMENT PRIMARY KEY"""
cursor.execute(query)

cursor.execute("DESCRIBE cliente")
for col in cursor:
     print(col)
      
my_db.close()