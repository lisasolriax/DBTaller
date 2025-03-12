# Jose Lisandro Lopez Lopez
# CRUD de Profesores, corregido con la conexion y Menú Interactivo

import mysql.connector

#Conexión a MySQL
def conectar():
    return mysql.connector.connect(
         host="localhost",      
        user="root",            
        password="solriax234", 
        database="dbtaller"       
    )

#Agregar un profesor
def agregar_profesor(nombreProf):
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "INSERT INTO profesor (nombreProf) VALUES (%s)"
    valores = (nombreProf,)
    cursor.execute(sql, valores)
    conexion.commit()
    print("Profesor agregado correctamente.")
    cursor.close()
    conexion.close()

#Listar profesores
def listar_profesores():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM profesor")
    profesores = cursor.fetchall()
    print("\nLista de Profesores:")
    for profesor in profesores:
        print(f"ID: {profesor[0]} | Nombre: {profesor[1]}")
    cursor.close()
    conexion.close()

#Modificar profesor
def actualizar_profesor(idprofesor, nuevo_nombre):
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "UPDATE profesor SET nombreProf = %s WHERE idprofesor = %s"
    valores = (nuevo_nombre, idprofesor)
    cursor.execute(sql, valores)
    conexion.commit()
    print("Profesor actualizado correctamente.")
    cursor.close()
    conexion.close()

#Eliminar profesor
def eliminar_profesor(idprofesor):
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "DELETE FROM profesor WHERE idprofesor = %s"
    cursor.execute(sql, (idprofesor,))
    conexion.commit()
    print("Profesor eliminado correctamente.")
    cursor.close()
    conexion.close()

#Menú interactivo
def menu():
    while True:
        print("\nMENÚ CRUD - Profesores")
        print("A. Agregar un Profesor")
        print("B. Listar Profesores")
        print("C. Modificar Profesor")
        print("D. Eliminar Profesor")
        print("E. Salir")
        
        opcion = input("Seleccione una opción (A/B/C/D/E): ").upper()

        if opcion == "A":
            nombre = input("Ingrese el nombre del profesor: ")
            agregar_profesor(nombre)

        elif opcion == "B":
            listar_profesores()

        elif opcion == "C":
            listar_profesores()
            idprofesor = int(input("Ingrese el ID del profesor a modificar: "))
            nuevo_nombre = input("Ingrese el nuevo nombre: ")
            actualizar_profesor(idprofesor, nuevo_nombre)

        elif opcion == "D":
            listar_profesores()
            idprofesor = int(input("Ingrese el ID del profesor a eliminar: "))
            eliminar_profesor(idprofesor)

        elif opcion == "E":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida, intente nuevamente.")

#Ejecutar el menú
if __name__ == "__main__":
    menu()

    
    
#https://github.com/lisasolriax/DBTaller/blob/main/practica10_23270057.py