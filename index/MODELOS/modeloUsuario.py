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
        
    def setUsuario(self,listaUsuario):
        self.setIdUsuario(listaUsuario[0])
        self.setNombre(listaUsuario[1])
        self.setCelular(listaUsuario[2])
        self.setCargo(listaUsuario[3])

    def registrarUsuario(self):
        conexion1 = crearConexion()
        cursor = conexion1.cursor()
        try:   
            cursor.execute("INSERT INTO usuario (Id_usuario, Nombre, Celular, Cargo) VALUES (%s,%s,%s,%s)", (self.idUsuario,self.nombre,self.celular,self.cargo))
            conexion1.commit()
            print("Datos Guardados con exito")  
            return True
        except Exception as e:
            print(f"Error al guardar los datos: {e}")
            return False
        finally:   
            cursor.close()
            conexion1.close()
            
    def modificarUsuario(self):
        conexion1 = crearConexion()
        cursor = conexion1.cursor()
        try:
            cursor.execute("""
                UPDATE usuario
                SET Id_usuario=%s, Nombre=%s, Celular=%s, Cargo=%s
                WHERE Id_producto=%s
                """, (self.idUsuario,self.nombre, self.celular, self.cargo))
            conexion1.commit()   
            print("Usuario modificado con éxito")
            return True   
        except Exception as e:
            print(f"Error al modificar el usuario: {e}")
            return False
        finally:
            cursor.close()
            conexion1.close()

    def eliminarUsuario(self):
        conexion1 = crearConexion()
        cursor = conexion1.cursor()
        try:
            cursor.execute("DELETE FROM usuario WHERE Id_usuario=%s", (self.idUsuario,))
            conexion1.commit()
            print("Usuario eliminado con éxito")
            return True
        except Exception as e:
            print(f"Error al eliminar el usuario: {e}")
            return False
        finally:
            cursor.close()
            conexion1.close()
            
    def consultarUsuario(self):
        conexion1 = crearConexion()
        cursor = conexion1.cursor()
        try:             
            cursor.execute(f"SELECT * FROM usuario WHERE Id_usuario=%s", (self.idUsuario,))
            consulta = cursor.fetchall()
            return consulta
        except Exception as e:
            print(f"Error al consultar los usuarios: {e}")    
            return None
        finally:    
            cursor.close()
            conexion1.close()
            
    def validarUsuario(self,listaUsuarioRegistrado):
        conexion1 = crearConexion()
        cursor = conexion1.cursor()
        id_usuario=listaUsuarioRegistrado[0]
        nombre=listaUsuarioRegistrado[1]
        try:             
            cursor.execute(f"SELECT * FROM usuario WHERE Id_usuario = %s AND Nombre = %s", (id_usuario,nombre))
            consulta = cursor.fetchall()
            return len(consulta)>0
        except Exception as e:
            print(f"Error al consultar los usuarios: {e}")
            return False
        finally:    
            cursor.close()
            conexion1.close()