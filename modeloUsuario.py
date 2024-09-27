from basededatos import crearConexion

class Usuario:
    def __init__ (self):
    
        self.usuario=None
        self.idUsuario=None
        self.celular=None
        self.cargo=None
        self.data=[]
      
        def getDatos(self):
            return self.data
        def setDatos(self,datas):
            self.data= datas
        def getUsuario(self):
            return self.usuario
        def setUsuario(self, nombre):
            self.usuario=nombre
        def getIdusuario(self):
            return self.idUsuario
        def setIdusuario(self, identificador):
            self.idUsuario= identificador
        def getCelular(self):
            return self.celular
        def setCelular(self, contacto):
            self.celular= contacto
        def getCargo(self):
            return self.cargo
        def setCargo(self, nivel):
            self.cargo= nivel


    def registrarUsuario(nombre, identificador, contacto, nivel):
        conexion1 = crearConexion()
        cursor = conexion1.cursor()
        cursor.execute(f"INSERT INTO uduarios (nombre, identificador, contacto, nivel) VALUES ('{nombre}','{identificador}','{contacto}','{nivel}')")
        conexion1.commit()
        print("Datos Guardados con exito")  
        
    def consultarUsuario():
        conexion1 = crearConexion()
        cursor = conexion1.cursor()
        cursor.execute(f"SELECT * FROM usuario")
        consulta = cursor.fetchall()
        return consulta

Usuario.data=Usuario.consultarUsuario()

nombre1= input("Nombre Usuario: ")
documento= input("Numero de Documento: ")
numero=input("Numero de Celular: ")
cargo= input("Cargo desempeñado en la empresa Administrador/Vendedor")

Usuario.nombre= nombre1
Usuario.identificador= documento
Usuario.contacto= numero
Usuario.nivel= cargo

Usuario.registrarUsuario(Usuario.nombre, Usuario.identificador, Usuario.contacto, Usuario.nivel)
