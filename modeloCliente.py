from basededatos import crearConexion

class Cliente:
    
    def __init__(self):
        self.idCliente=None
        self.nombre=None
        self.apellido=None

    def getId(self):
        return self.idCliente
    def setId(self,idCliente):
        self.idCliente=idCliente
    def getNombre(self):
        return self.nombre
    def setNombre(self,nombre):
        self.nombre=nombre
    def getApellido(self):
        return self.apellido
    def setApellido(self,apellido):
        self.apellido=apellido
    
    def setCliente(self,listaCliente):
        self.setId(listaCliente[0])
        self.setNombre(listaCliente[1])
        self.setApellido(listaCliente[2])
        
    def registrarCliente(self):
        conexion1 = crearConexion()
        cursor = conexion1.cursor()
        try:   
            cursor.execute("INSERT INTO cliente (Id_cliente, Nombre, Apellido) VALUES (%s,%s,%s)", (self.idCliente,self.nombre, self.apellido))
            conexion1.commit()
            print("Datos Guardados con exito")
            return True  
        except Exception as e:
            print(f"Error al guardar los datos: {e}")
            return False
        finally:   
            cursor.close()
            conexion1.close()  

    def consultarCliente(self):
        conexion1 = crearConexion()
        cursor = conexion1.cursor()
        try:             
            cursor.execute(f"SELECT * FROM cliente WHERE Id_cliente=%s", (self.idCliente,))
            consulta = cursor.fetchall()
            return consulta      
        except Exception as e:
            print(f"Error al consultar los cliente: {e}")    
            return None
        finally:    
            cursor.close()
            conexion1.close()