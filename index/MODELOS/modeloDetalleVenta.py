from index.MODELOS.basededatos import crearConexion

class DetalleVenta:
    def __init__(self):
        self.idVenta = None
        self.idProducto = None
        self.cantidad = None
        self.precio = None
        self.total=None

    def setDetalle(self, listaDetalle):
        self.idVenta = listaDetalle[0]
        self.idProducto = listaDetalle[1]
        self.cantidad = listaDetalle[2]
        self.precio = listaDetalle[3]
        self.total=listaDetalle[4]

    def crearDetalleVenta(self):
        conexion1 = crearConexion()
        cursor = conexion1.cursor()
        try:
            cursor.execute("INSERT INTO detalle_venta (Id_venta, Id_producto, Cantidad, Precio) VALUES (%s, %s, %s, %s,%s)",(self.idVenta, self.idProducto, self.cantidad, self.precio,self.total))
            conexion1.commit()
            print("Detalle de venta guardado con éxito")
            return True
        except Exception as e:
            print(f"Error al guardar el detalle de la venta: {e}")
            return False
        finally:
            cursor.close()
            conexion1.close()
            
    def consultarDetalleVenta(self):
        conexion1 = crearConexion()
        cursor = conexion1.cursor()
        try:             
            cursor.execute(f"SELECT * FROM detalle_venta")
            consulta = cursor.fetchall()
            return consulta
        except Exception as e:
            print(f"Error al consultar los cliente: {e}")    
            return None
        finally:    
            cursor.close()
            conexion1.close()