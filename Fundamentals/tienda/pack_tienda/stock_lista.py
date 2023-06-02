#from pelicula import Pelicula
#from libro import Libro

#p = Pelicula()
#l = Libro()

#p.Agregar_Pelicula("Tarzan", "1:25:03", 15)
#p.Agregar_Pelicula("Bourne", "1:35:03", 3)
#p.Agregar_Pelicula("El Hobit", "1:40:00", 20)
#p.Agregar_Pelicula("Rambo", "1:43:00", 6)
#l.Agregar_Libro("Matematica I", 120, 13)
#l.Agregar_Libro("Matematica II", 100, 21)
#l.Agregar_Libro("Matematica III", 90, 26)
#l.Agregar_Libro("Matematica IV", 95, 14)

def Listar_Stock(numero_stock, obj_p, obj_l):
    lista_productos = []
    nueva_lista = []

    for pel in obj_p.Listar_Peliculas():
        lista_productos.append(pel)

    for lib in obj_l.Listar_Libros():
        lista_productos.append(lib)

    for producto in lista_productos:
        if numero_stock >= producto["Stock"]:
            nueva_lista.append(producto)

    return nueva_lista

#print(Listar_Stock(14))
