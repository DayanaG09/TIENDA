from basededatos import crearConexion

class Usuario:
    def __init__ (self):
        self.usuario=None
        self.idUsuario=None
        self.cargo=None

    def getUsuario(self):
        return self.usuario
    def setUsuario(self, nombre):
        self.usuario=nombre
    def getIdUsuario(self):
        return self.idUsuario
    def setIdUsuario(self, identificador):
        self.idUsuario= identificador
    def getCargo(self):
        return self.cargo
    def setCargo(self, cargo):
        self.cargo=cargo

    def registrarUsuario(self,identificador,nombre ):
        conexion1 = crearConexion()
        cursor = conexion1.cursor()
        try:   
            cursor.execute("INSERT INTO usuario (Id_empleado, Nombre_empleado) VALUES (%s,%s)", (identificador,nombre))
            conexion1.commit()
            print("Datos Guardados con exito")  
        except Exception as e:
            print(f"Error al guardar los datos: {e}")
        finally:   
            cursor.close()
            conexion1.close()
            
    def consultarUsuario(self):
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
            
    def validarUsuario(self,listaUsuario):
        conexion1 = crearConexion()
        cursor = conexion1.cursor()
        id_usuario=listaUsuario[1]
        nombre=listaUsuario[0]
        try:             
            cursor.execute(f"SELECT * FROM usuario WHERE Id_empleado = %s AND Nombre_empleado = %s", (id_usuario,nombre))
            consulta = cursor.fetchall()
            return True
        except Exception as e:
            print(f"Error al consultar los usuarios: {e}")
            return False
        finally:    
            cursor.close()
            conexion1.close()