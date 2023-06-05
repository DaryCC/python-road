'''Aquí se implementa los polimorfismo y ya'''
from pack_tienda.libro import Libro
from pack_tienda.pelicula import Pelicula
from pack_tienda.stock_lista import Listar_Stock

print("-----Bienvenido Admin-----")
while True:
    print("")
    print("1. Agregar una pelicula")
    print("2. Listar Peliculas")
    print("3. Agregar un Libro")
    print("4. Listar Libros")
    print("5. Ver productos con poco stock")
    print("6. Salir")
    opcion = input("Que quieres hacer?: (1-6)").strip()
    print("")
    p = Pelicula()
    l = Libro()
    if int(opcion) == 1:
        print("----Datos de la pelicula---")
        nom = input("Nombre de pelicula: ").strip().capitalize()
        dur = input("Duracion: ").strip()
        stock = int(input("Stock: ").strip())
        p.Agregar_Pelicula(nom, dur, stock)
    elif int(opcion) == 2:
        lista = p.Listar_Peliculas()
        print(lista)
    elif int(opcion) == 3:
        print("----Datos de Libro---")
        nom = input("Nombre de Libro: ").strip().capitalize()
        hojas = int(input("Hojas: ").strip())
        stock = int(input("Stock: ").strip())
        l.Agregar_Libro(nom, hojas, stock)
    elif int(opcion) == 4:
        lista = l.Listar_Libros()
        print(lista)
    elif int(opcion) == 5:
        stock = int(input("Cantidad a evaluar: ").strip())
        lista = Listar_Stock(stock, p, l)
        print("---Productos con stock menor que "+str(stock)+"--")
        print(lista)
    elif int(opcion) == 6:
        break
    else:
        print("Opcion invalida")

