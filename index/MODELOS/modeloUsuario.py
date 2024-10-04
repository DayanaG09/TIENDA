from index.MODELOS.basededatos import crearConexion

class Usuario:
    def __init__ (self):
        self.idUsuario=None
        self.nombre=None
        self.celular=None
        self.cargo=None
        
    def getIdUsuario(self):
        return self.idUsuario
    def setIdUsuario(self, identificador):
        self.idUsuario= identificador
    def getNombre(self):
        return self.nombre
    def setNombre(self, nombre):
        self.nombre=nombre
    def getCelular(self):
        return self.celular
    def setCelular(self,celular):
        self.celular=celular
    def getCargo(self):
        return self.cargo
    def setCargo(self, cargo):
        self.cargo=cargo
        
    def set_usuario(self,listaUsuario):
        self.setIdUsuario(listaUsuario[0])
        self.setNombre(listaUsuario[1])
        self.setCelular(listaUsuario[2])
        self.setCargo(listaUsuario[3])
            
    def consultar_usuario(self):
        conexion1 = crearConexion()
        cursor = conexion1.cursor()
        try:             
            cursor.execute(f"SELECT * FROM usuario")
            consulta = cursor.fetchall()
            return consulta
        except Exception as e:
            print(f"Error al consultar los usuarios: {e}")    
            return None
        finally:    
            cursor.close()
            conexion1.close()
            
    def validar_usuario(self):
        conexion1 = crearConexion()
        cursor = conexion1.cursor()
        try:             
            cursor.execute(f"SELECT Id_usuario, Nombre FROM usuario WHERE Id_usuario = %s AND Nombre = %s", (self.idUsuario,self.nombre))
            consulta = cursor.fetchall()
            return len(consulta)>0
        except Exception as e:
            print(f"Error al consultar los usuarios: {e}")
            return False
        finally:    
            cursor.close()
            conexion1.close()