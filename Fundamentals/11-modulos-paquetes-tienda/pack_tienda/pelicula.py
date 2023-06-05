peliculas = []

class Pelicula:
    def __init__(self, nombre="", duracion="", stock=0):
        self.nombre = nombre
        self.duracion = duracion
        self.stock = stock

    def Agregar_Pelicula(self, nombre, duracion, stock):
        self.nombre = nombre
        self.duracion = duracion
        self.stock = stock
        peliculas.append({"Pelicula": nombre,
                          "Duracion": duracion,
                          "Stock": stock})

    def Listar_Peliculas(self):
        return peliculas

#p = Pelicula()
#p.Agregar_Pelicula("Tarzan", "1:35:00", 21)
#p.Agregar_Pelicula("Rambo", "1:32:00", 12)
#print(p.Listar_Peliculas())

