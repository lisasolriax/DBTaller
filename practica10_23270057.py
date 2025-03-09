#Jose Lisandro Lopez Lopez
#CRUD de los Profesores
from conexion import conectar

from conexion import conectar

# Agregar un profesor
def agregar_profesor(nombreProf):
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "INSERT INTO profesor (nombreProf) VALUES (%s)"
    valores = (nombreProf,)
    cursor.execute(sql, valores)
    conexion.commit()
    print("Profesor agregado.")
    cursor.close()
    conexion.close()

# Listar profesores
def listar_profesores():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM profesor")
    profesores = cursor.fetchall()
    for profesor in profesores:
        print(profesor)
    cursor.close()
    conexion.close()

# Modificar profesor
def actualizar_profesor(idprofesor, nuevo_nombre):
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "UPDATE profesor SET nombreProf = %s WHERE idprofesor = %s"
    valores = (nuevo_nombre, idprofesor)
    cursor.execute(sql, valores)
    conexion.commit()
    print("Profesor actualizado.")
    cursor.close()
    conexion.close()

# Eliminar profesor
def eliminar_profesor(idprofesor):
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "DELETE FROM profesor WHERE idprofesor = %s"
    cursor.execute(sql, (idprofesor,))
    conexion.commit()
    print("Profesor eliminado.")
    cursor.close()
    conexion.close()
    
    
#https://github.com/lisasolriax/DBTaller/blob/master/practica10_23270057.py