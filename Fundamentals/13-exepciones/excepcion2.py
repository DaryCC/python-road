

try:
    archivo = open("prueba.txt")
except Exception as err:
    print("Error al abrir archivo:", err)
else:
    print("Archivo abierto, continua...")
finally:
    print("Procedimiento final, Nos vemos...")
