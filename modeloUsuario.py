from basededatos import crearConexion

class Usuario:
    def __init__ (self):
        self.usuario=None
        self.idUsuario=None
        self.celular=None
        self.cargo=None
        self.data=[]

    def getUsuario(self):
        return self.usuario
    def setUsuario(self, nombre):
        self.usuario=nombre
    def getIdusuario(self):
        return self.idUsuario
    def setIdusuario(self, identificador):
        self.idUsuario= identificador

    def registrarUsuario(self,identificador,nombre ):
        conexion1 = crearConexion()
        cursor = conexion1.cursor()
        cursor.execute(f"INSERT INTO usuario (Id_empleado, Nombre_empleado) VALUES ('{identificador}','{nombre}')")
        conexion1.commit()
        print("Datos Guardados con exito")  
        cursor.close()
        conexion1.close()
        
    def consultarUsuario(self):
        conexion1 = crearConexion()
        cursor = conexion1.cursor()
        cursor.execute(f"SELECT * FROM usuario")
        consulta = cursor.fetchall()
        cursor.close()
        conexion1.close()
        return consulta