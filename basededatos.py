import mysql.connector
from mysql.connector import Error
      
def crearConexion():
        
        connection= mysql.connector.connect(
            host='localhost',
            database= 'drogueria_haybetsalud',
            user= 'root',
            password= ''
        
            )
        return connection 
    
def verificacionConexion(datoConexion):
    if datoConexion.is_connected():
        print("conexion exitosa a la base de datos")
        #2.crear un objeto cursor para ejecutar consultas.
        cursor=datoConexion.cursor()
        #3 ejecutar una consulta SQL
        #consulta para seleccionar todos los registros de 'tabla_ejemplo'
        cursor.execute("SELECT * FROM producto")
        #4 recuperar los resultados de la consulta 
        resultados= cursor.fetchall() #recupera todas las filas de la consulta 
        print(resultados)
        
aux=crearConexion()
print(aux)
