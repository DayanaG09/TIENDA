from index.MODELOS.basededatos import crearConexion

class Categoria:
    def __init__(self):
        self.id=None
        self.nombre=None
        
    def get_id(self):
        return self.id
    def set_id(self,id):
        self.id=id    
    def get_nombre(self):
        return self.nombre
    def set_nombre(self,nombre):
        self.nombre=nombre      
        
    def set_categoria(self, listaCategoria):
        self.set_id(listaCategoria[0])
        self.set_nombre(listaCategoria[1])

    #tambien está en el modeloProducto, REVISAR
    def consultar_categorias(self):
        conexion1 = crearConexion()
        cursor = conexion1.cursor()
        try:             
            cursor.execute(f"SELECT * FROM categoria")
            consulta = cursor.fetchall()
            self.set_categoria(consulta)     
        except Exception as e:
            print(f"Error al consultar la categoria: {e}")    
            return None
        finally:    
            cursor.close()
            conexion1.close()
            
    def consulta_categoria(self,categoria):
        conexion1 = crearConexion()
        cursor = conexion1.cursor()
        try:
            cursor.execute(f"SELECT Id_consulta FROM producto WHERE categoria = %s",(categoria))
            consulta = cursor.fetchall()
            self.set_id(consulta)
        except Exception as e:
            print(f"Error al consultar las categorías: {e}")
            return None
        finally:
            cursor.close()
            conexion1.close()