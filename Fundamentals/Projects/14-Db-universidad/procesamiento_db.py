import mysql.connector


def Conexion_DB():
    return mysql.connector.connect(
        host="localhost", user="root", password="12", database="universidad"
    )


def Registrar_Alumno(nombre,apellido,carrera,edad):
    db=Conexion_DB()
    mi_cursor=db.cursor()


    query="""INSERT INTO estudiantes (nombre,apellido,carrera,edad) VALUES(%s,%s,%s,%s)"""
    valores=(nombre,apellido,carrera,edad)

    try:
        mi_cursor.execute(query,valores)
    except Exception as e:
        print(e)
        db.rollback()
        retorno= 1
    else:
        db.commit()
        retorno= 0
    finally:
        return retorno


# resultado=Registrar_Alumno("Dary","Nadia","meca",30)
# int(resultado)
def Obtener_Alumno_Id(id):
    db=Conexion_DB()
    cursor=db.cursor()
    
    valores=(id,)

    query="""select * from estudiantes where estudiante_id=%s"""

    try: 
        cursor.execute(query,(id,))
    except Exception as e:
        print(e)
        db.rollback()
        retorno=1
    else:
        retorno=()
        for alumno in cursor:
            retorno=alumno
    finally:
        db.close()
        return retorno


# print(Obtener_Alumno_Id(4))    

    
def Actualizar_Carrera_Alumno(carrera, id_est):
    mi_db = Conexion_DB()
    mi_cursor = mi_db.cursor()

    sql = """ UPDATE estudiantes
                SET carrera = %s
                WHERE estudiante_id = %s """

    valores = (carrera, id_est)

    try:
        mi_cursor.execute(sql, valores)
    except:
        mi_db.rollback()
        retorno = 1
    else:
        mi_db.commit()
        retorno = 0
    finally:
        mi_db.close()
        return retorno

#resultado = Actualizar_Carrera_Alumno("Desarrollo Web", 1)
#print(resultado)

def Eliminar_Alumno(id_est):
    mi_db = Conexion_DB()
    mi_cursor = mi_db.cursor()

    sql = """ DELETE FROM estudiantes
                WHERE estudiante_id = %s """

    valores = (id_est,)

    try:
        mi_cursor.execute(sql, valores)
    except:
        mi_db.rollback()
        retorno = 1
    else:
        mi_db.commit()
        retorno = 0
    finally:
        mi_db.close()
        return retorno

#resultado = Eliminar_Alumno(2)
#print(resultado)
def Listar_Alumnos():
    db=Conexion_DB()
    cursor=db.cursor()

    query="""select * from estudiantes"""
    try:
        cursor.execute(query)

    except Exception as e:
        print(e)
        db.rollback()
        retorno=1
    else:
        retorno=[]

        for alumno in cursor:
            retorno.append(alumno)
    finally:
        db.close()
        return retorno
