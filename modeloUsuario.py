class Usuario:
    def __init__(self):
        self.usuario=None
        self.idUsuario=None
        self.celular=None
        self.cargo=None
        self.data=[]
    
def getDatos():
    return self.data
def setDatos(datas):
    self.data= datas
def getUsuario():
    return self.usuario
def setUsuario(nombre):
    self.usuario=nombre
def getIdusuario():
    return self.idUsuario
def setIdusuario(identificador):
    self.idUsuario= identificador
def getCelular():
    return self.celular
def setCelular(contacto):
    self.celular= contacto
def getCargo():
    return self.cargo
def setCargo(nivel):
    self.cargo= nivel


def registrarUsuario(nombre, identificador, contacto, nivel):
        conexion1 = conexion.crearConexion()
        cursor = conexion1.cursor()
        cursor.execute(f"INSERT INTO uduarios (nombre, identificador, contacto, nivel) VALUES ('{nombre}','{identificador}','{contacto}','{nivel}')")
        conexion1.commit()
        print("Datos Guardados con exito")  
        
def consultarUsuario(registrarUsuario):
        conexion1 = conexion.crearConexion()
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