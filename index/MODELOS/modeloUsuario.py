class Usuario:
    def __init__ (self,conexion):
        self.conexion=conexion
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
            
    def consultar_usuarios(self):
        cursor = self.conexion.cursor()
        usuarios=[]
        try:             
            cursor.execute(f"SELECT * FROM usuario")
            consulta = cursor.fetchall()
            for fila in consulta:
                usuario=Usuario(self.conexion)
                usuario.set_usuario(fila)
                usuarios.append(usuario)
            return usuarios
        except Exception as e:
            print(f"Error al consultar los usuarios: {e}")    
            return None
        finally:    
            cursor.close()
            
            
    def validar_usuario(self):
        cursor = self.conexion.cursor()
        try:             
            cursor.execute(f"SELECT * FROM usuario WHERE Id_usuario = %s AND Nombre = %s AND Cargo = %s", (self.idUsuario,self.nombre, self.cargo))
            consulta = cursor.fetchall()
            return len(consulta)>0
        except Exception as e:
            print(f"Error al consultar los usuarios: {e}")
            return False
        finally:    
            cursor.close()