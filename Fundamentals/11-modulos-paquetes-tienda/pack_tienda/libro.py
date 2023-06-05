libros = []

class Libro:
    def __init__(self, nombre="", hojas=0, stock=0):
        self.nombre = nombre
        self.hojas = hojas
        self.stock = stock

    def Agregar_Libro(self, nombre, hojas, stock):
        self.nombre = nombre
        self.hojas = hojas
        self.stock = stock
        libros.append({"Libro": nombre,
                       "Hojas": hojas,
                       "Stock": stock})

    def Listar_Libros(self):
        return libros

#l = Libro()
#l.Agregar_Libro("Matematicas I", 100, 23)
#l.Agregar_Libro("Programacion", 87, 12)
#print(l.Listar_Libros())
