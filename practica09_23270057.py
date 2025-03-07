#Jose Lisandro Lopez Lopez 23270057
#CRUD de los tipo de proyecto
from conexion import conectar

#Agregar un tipo de proyecto
def agregar_tipo(tipo, nombre):
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "INSERT INTO tipoproyecto (tipo, nombre) VALUES (%s, %s)"
    valores = (tipo, nombre)
    cursor.execute(sql, valores)
    conexion.commit()
    print("Tipo de proyecto agregado.")
    cursor.close()
    conexion.close()

#Listar todos los tipos de proyecto
def listar_tipos():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM tipoproyecto")
    tipos = cursor.fetchall()
    for tipo in tipos:
        print(tipo)
    cursor.close()
    conexion.close()

# Actualizar un tipo de proyecto
def actualizar_tipo(tipo, nuevo_nombre):
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "UPDATE tipoproyecto SET nombre = %s WHERE tipo = %s"
    valores = (nuevo_nombre, tipo)
    cursor.execute(sql, valores)
    conexion.commit()
    print("Tipo de proyecto actualizado.")
    cursor.close()
    conexion.close()

# Eliminar un tipo de proyecto
def eliminar_tipo(tipo):
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "DELETE FROM tipoproyecto WHERE tipo = %s"
    cursor.execute(sql, (tipo,))
    conexion.commit()
    print("Tipo de proyecto eliminado.")
    cursor.close()
    conexion.close()
    
    #el enlace aunque al DBTaller donde se encuentra mis archivos
    #https://github.com/lisasolriax/DBTaller.git