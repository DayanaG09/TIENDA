class Producto:
    
    def __init__(self,conexion):
        self.conexion=conexion
        self.idProducto=None
        self.nombre=None
        self.existencia=None
        self.cantidadesVendidas=None
        self.categoria=None
        self.detalles=None
        self.precio=None
        
    ## LLave primaria o codigo identificador del producto
    def get_id_producto(self):
        return self.idProducto
    def set_id_producto(self,idProducto):
        self.idProducto=idProducto
    ##nombre productos  
    def get_nombre(self):
        return self.nombre
    def set_nombre(self, nombre):
        self.nombre = nombre
    ## Existencia del producto   
    def get_existencia(self):
        return self.existencia
    def set_existencia(self, existencia):
        self.existencia= existencia 
    ##Cantidades vendidas
    def get_cantidades_vendidas(self):
        return self.cantidadesVendidas
    def set_cantidades_vendidas(self, cantidadesVendidas):
        self.cantidadesVendidas= cantidadesVendidas 
    ##categoria
    def get_categoria(self):
        return self.categoria
    def set_categoria(self, categoria):
        self.categoria= categoria
    #detalles
    def get_detalles(self):
        return self.detalles
    def set_detalles(self, detalles):
        self.detalles= detalles
    ##precio productos
    def get_precio(self):
        return self.precio
    def set_precio(self, precio):
        self.precio = precio
        
    def set_producto(self,listaProductos):
        self.set_id_producto(listaProductos[0])
        self.set_nombre(listaProductos[1])
        self.set_existencia(listaProductos[2])
        self.set_cantidades_vendidas(listaProductos[3])
        self.set_categoria(listaProductos[4])
        self.set_detalles(listaProductos[5])
        self.set_precio(listaProductos[6])
        
    def set_producto2(self,listaProductos):
        self.set_nombre(listaProductos[0])
        self.set_existencia(listaProductos[1])
        self.set_cantidades_vendidas(listaProductos[2])
        self.set_categoria(listaProductos[3])
        self.set_detalles(listaProductos[4])
        self.set_precio(listaProductos[5])
            
  ###REGISTRAR PRODUCTOS   
    def crear_producto (self):
        cursor = self.conexion.cursor()
        
        try:
            cursor.execute("INSERT INTO producto (nombre__producto,cantidad_existencia,cantidad_vendidas, categoria, detalles,precio_producto) VALUES (%s,%s,%s,%s,%s,%s)", (self.nombre,self.existencia,self.cantidadesVendidas,self.categoria,self.detalles,self.precio))
            self.conexion.commit()
        except Exception as e:
            print(f"Erro al guardar los datos:{e}")
        finally:
            cursor.close()
    
    def modificar_producto(self):
        cursor = self.conexion.cursor()
        try:
            cursor.execute("""
                UPDATE producto
                SET nombre__producto=%s, cantidad_existencia=%s, cantidad_vendidas=%s, 
                    categoria=%s, detalles=%s, precio_producto=%s 
                WHERE Id_producto=%s
                """, (self.nombre,self.existencia,self.cantidadesVendidas,self.categoria,self.detalles,self.precio,self.idProducto))
            self.conexion.commit()
            return True
        except Exception as e:
            print(f"Error al modificar el producto: {e}")
            return False
        finally:
            cursor.close()

    def eliminar_producto(self):
        cursor = self.conexion.cursor()
        try:
            cursor.execute("DELETE FROM producto WHERE Id_producto=%s", (self.idProducto,))
            self.conexion.commit()
            return True
        except Exception as e:
            print(f"Error al eliminar el producto: {e}")
            return False
        finally:
            cursor.close()

        
##CONSULTAR O BUSCAR PRODUCTOS
    def consultar_productos(self):
        cursor = self.conexion.cursor()
        productos = []
        try:
            cursor.execute("SELECT * FROM producto")
            consulta = cursor.fetchall()
            for fila in consulta:
                producto=Producto(self.conexion)
                producto.set_producto(fila)
                productos.append(producto)
            return productos
        except Exception as e:
            print(f"Error al consultar los productos: {e}")
            return None
        finally:
            cursor.close()
            
    def consultar_productos_masVendidos(self): #este metodo debe consultar el producto indicado por el usuario
        cursor = self.conexion.cursor()
        try:
            cursor.execute("SELECT producto.nombre__producto, producto.cantidad_vendidas FROM producto ORDER BY producto.cantidad_vendidas DESC LIMIT 4")
            consulta = cursor.fetchall()
            return consulta
        except Exception as e:
            print(f"Error al consultar los productos más vendidos: {e}")
            return None
        finally:
            cursor.close()
            
    def consultar_productos_menosVendidos(self):
        cursor = self.conexion.cursor()
        try:
            cursor.execute("SELECT producto.nombre__producto, producto.cantidad_vendidas FROM producto ORDER BY producto.cantidad_vendidas ASC LIMIT 4")
            consulta = cursor.fetchall()
            return consulta
        except Exception as e:
            print(f"Error al consultar los productos más vendidos: {e}")
            return None
        finally:
            cursor.close()