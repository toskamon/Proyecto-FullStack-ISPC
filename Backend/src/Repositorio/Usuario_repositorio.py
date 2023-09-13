from Repositorio.Conexion import *

def crear_user(nombre,apellido,email,dni,domicilio,rol):
     try:
        connection.connect()
        
        query = "INSERT INTO Usuarios(nombre,apellido,email,dni,domicilio,rol)VALUES (%s,%s,%s,%s,%s,%s)"
        values = (nombre,apellido,email,dni,domicilio,rol)
        connection.cursor.execute(query, values)
        connection.commit()
        id_insertado = connection.cursor.lastrowid
        print("El Usuario se inserto correctamente en la base de datos.")
        return id_insertado
        
     except mysql.connector.Error as err:
        print("Error al intentar insertar el Usuario:", err)
     finally:
         if connection:
            connection.close()
         
      