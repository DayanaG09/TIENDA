from index.MODELOS.basededatos import crearConexion

class Usuario:
    def __init__ (self):
        self.idUsuario=None
        self.nombre=None
        self.celular=None
        self.cargo=None
        
    def get_id_usuario(self):
        return self.idUsuario
    def set_id_usuario(self, identificador):
        self.idUsuario= identificador
    def get_nombre(self):
        return self.nombre
    def set_nombre(self, nombre):
        self.nombre=nombre
    def get_celular(self):
        return self.celular
    def set_celular(self,celular):
        self.celular=celular
    def get_cargo(self):
        return self.cargo
    def set_cargo(self, cargo):
        self.cargo=cargo
        
    def set_usuario(self,listaUsuario):
        self.set_id_usuario(listaUsuario[0])
        self.set_nombre(listaUsuario[1])
        self.set_celular(listaUsuario[2])
        self.set_cargo(listaUsuario[3])
            
    def consultar_usuario(self):
        conexion1 = crearConexion()
        cursor = conexion1.cursor()
        try:             
            cursor.execute(f"SELECT * FROM usuario")
            consulta = cursor.fetchall()
            self.set_usuario(consulta)
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