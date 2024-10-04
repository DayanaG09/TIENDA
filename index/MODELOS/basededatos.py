import mysql.connector
from mysql.connector import Error
      
def crearConexion():
    try:    
        connection= mysql.connector.connect(
            host='localhost',
            database= 'drogueria_haybetsalud',
            user= 'root',
            password= ''
            )
        if connection.is_connected():
            print("Conexión exitosa a la base de datos")
            return connection 
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None
    
def verificacionConexion(datoConexion):
    if datoConexion.is_connected():
        #1.crear un objeto cursor para ejecutar consultas.
        cursor=datoConexion.cursor()
        try:
            #2.ejecutar una consulta SQL
            #consulta para seleccionar todos los registros de 'tabla_ejemplo'
            cursor.execute("SELECT * FROM products")
            #3.recuperar los resultados de la consulta 
            resultados= cursor.fetchall() #recupera todas las filas de la consulta 
            print(resultados)
        except Error as e:
            print(f"Error al ejecutar la consulta: {e}")
        finally:
            cursor.close()
            datoConexion.close()