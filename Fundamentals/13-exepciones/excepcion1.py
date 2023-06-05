
a = input("Ingresa valor de a: ")
b = input("Ingresa valor de b: ")

try:
    resultado = int(a) / int(b)
    print(resultado)

except ValueError:
    print("a/b no son numericos, o a y b no son numericos")
except ZeroDivisionError:
    print("Lo siento, no puedes dividir por cero")
except Exception as error:
    print(type(error))
    print("Lo siento, hubo un error:", error)


print("Fuera del bloque try-except")
