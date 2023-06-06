import procesamiento_db as modulo

# Registrar_Alumno(nombre, apellido, carrera, edad)
# Listar_Alumnos()
# Obtener_Alumno_Id(id_est)
# Actualizar_Carrera_Alumno(carrera, id_est)
# Eliminar_Alumno(id_est)

while True:
    print("")
    print("=== Estudiantes ===")
    print("1. Registrar un Alumno")
    print("2. Listar Alumnos")
    print("3. Buscar un Alumno")
    print("4. Actualizar carrera de alumno")
    print("5. Eliminar un Alumno")
    print("6. Cerrar Sistema")
    print("===================")
    opcion = int(input("Elige una opcion (1-6): ").strip())
    print("===================")
    print("")

    if opcion == 1:
        print("=== Datos de Alumno ===")
        nom = input("Nombre: ").strip().capitalize()
        ape = input("Apellido: ").strip().capitalize()
        car = input("Carrera: ").strip().capitalize()
        eda = int(input("Edad: ").strip())
        res = modulo.Registrar_Alumno(nom, ape, car, eda)
        if res == 1:
            print("=== Ups, hubo un error al insertar ===")
        else:
            print("=== Alumno Inscrito ===")
            
    elif opcion == 2:
        print("=== Listado de Alumnos ===")
        res = modulo.Listar_Alumnos()
        print(res)

    elif opcion == 3:
        print("=== Buscar un Alumno ===")
        est_id = int(input("Id de Alumno: ").strip())
        res = modulo.Obtener_Alumno_Id(est_id)
        if res == 1:
            print("== Ups, hubo un error al buscar ==")
        elif res == ():
            print("== No hay alumno con ese ID ==")
        else:
            print(res)
            
    elif opcion == 4:
        print("=== Actualizar Carrera de Alumno ===")
        est_id = int(input("Id de Alumno: ").strip())
        res = modulo.Obtener_Alumno_Id(est_id)
        if res == 1:
            print("== Ups, hubo un error al buscar ==")
        elif res == ():
            print("== No hay alumno con ese ID ==")
        else:
            carr = input("Ingresa nueva carrera: ").strip().capitalize()
            res = modulo.Actualizar_Carrera_Alumno(carr, est_id)
            if res == 1:
                print("== Ups, hubo un error al actualizar ==")
            else:
                print("== Carrera cambiada ==")

    elif opcion == 5:
        print("=== Eliminar un Alumno ===")
        est_id = int(input("Id de Alumno: ").strip())
        res = modulo.Obtener_Alumno_Id(est_id)
        if res == 1:
            print("== Ups, Intentalo nuevamente ==")
        elif res == ():
            print("== No hay alumno con ese ID ==")
        else:
            res = modulo.Eliminar_Alumno(est_id)
            if res == 1:
                print("== Ups, hubo un error al eliminar ==")
            else:
                print("== Alumno eliminado ==")

    elif opcion == 6:
        print("==== Sistema Cerrado ====")
        break
    
    else:
        print("Error, intentalo nuevamente")

    
