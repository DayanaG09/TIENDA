from basededatos import crearConexion

class Venta:
    def __init__(self):
        self.idVenta=None
        self.fecha=None
        self.idVendedor=None
        self.idCliente=None
        
    def getFecha(self):
        return self.fecha
    def setFecha(self,fecha):
        self.fecha=fecha
    def getIdVendedor(self):
        return self.idVendedor
    def setIdVendedor(self,vendedor):
        self.idVendedor=vendedor
    def getIdCliente(self):
        return self.idCliente
    def setIdCliente(self,cliente):
        self.idCliente=cliente
        
    def setVenta(self,listaVenta):
        self.setFecha(listaVenta[0])
        self.setIdVendedor(listaVenta[1])
        self.setIdCliente(listaVenta[2])
        
    def crearVenta(self):
        conexion1 = crearConexion()
        cursor = conexion1.cursor()
        try:   
            cursor.execute("INSERT INTO venta (Fecha_venta,Id_vendedor,Id_cliente) VALUES (%s,%s,%s)", (self.fecha,self.idVendedor, self.idCliente))
            conexion1.commit()
            print("Venta realizada con exito")
            return True  
        except Exception as e:
            print(f"Error al realizar la venta: {e}")
            return False
        finally:   
            cursor.close()
            conexion1.close()      
            
    def consultarCliente(self):
        conexion1 = crearConexion()
        cursor = conexion1.cursor()
        try:             
            cursor.execute(f"SELECT * FROM venta")
            consulta = cursor.fetchall()
            return consulta      
        except Exception as e:
            print(f"Error al consultar venta: {e}")    
            return None
        finally:    
            cursor.close()
            conexion1.close()