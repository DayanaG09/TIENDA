from index.MODELOS.basededatos import crearConexion

class Categoria:
    def __init__(self):
        self.categoria=None
        self.nombre=None
        
    def getNombre(self):
        return self.nombre
    def setNombre(self,nombre):
        self.nombre=nombre      

    #tambien está en el modeloProducto, REVISAR
    def consultarCategoria(self):
        conexion1 = crearConexion()
        cursor = conexion1.cursor()
        try:             
            cursor.execute(f"SELECT * FROM categoria")
            consulta = cursor.fetchall()
            return consulta      
        except Exception as e:
            print(f"Error al consultar la categoria: {e}")    
            return None
        finally:    
            cursor.close()
            conexion1.close()