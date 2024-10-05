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
        categorias=[]
        try:             
            cursor.execute(f"SELECT * FROM categoria")
            consulta = cursor.fetchall()
            for fila in consulta:
                categoria=Categoria()
                categoria.set_categoria(fila)
                categorias.append(categoria)
            return categorias
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
            cursor.execute(f"SELECT Nombre_categoria FROM categoria WHERE Id_categoria = %s",(self.id))
            consulta = cursor.fetchall()
            self.set_nombre(consulta)
        except Exception as e:
            print(f"Error al consultar las categorías: {e}")
            return None
        finally:
            cursor.close()
            conexion1.close()