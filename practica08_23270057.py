#Jose Lisandro LOpez Lopez 23270057
#CRUD de las linea de investigacion
from conexion import conectar

# Agregar una nueva línea de investigación
def agregar_linea(clavein, nombre):
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "INSERT INTO lineainv (clavein, nombre) VALUES (%s, %s)"
    valores = (clavein, nombre)
    cursor.execute(sql, valores)
    conexion.commit()
    print("Línea de investigación agregada.")
    cursor.close()
    conexion.close()

#Listar todas las líneas de investigación
def listar_lineas():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM lineainv")
    lineas = cursor.fetchall()
    for linea in lineas:
        print(linea)
    cursor.close()
    conexion.close()

#Actualizar una línea de investigación
def actualizar_linea(clavein, nuevo_nombre):
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "UPDATE lineainv SET nombre = %s WHERE clavein = %s"
    valores = (nuevo_nombre, clavein)
    cursor.execute(sql, valores)
    conexion.commit()
    print("Línea de investigación actualizada.")
    cursor.close()
    conexion.close()

#Eliminar una línea de investigación
def eliminar_linea(clavein):
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "DELETE FROM lineainv WHERE clavein = %s"
    cursor.execute(sql, (clavein,))
    conexion.commit()
    print("Línea de investigación eliminada.")
    cursor.close()
    conexion.close()
