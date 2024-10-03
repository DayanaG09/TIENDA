from basededatos import crearConexion
import json

class Producto:
    
    def __init__(self):
        self.nombreProducto=None
        self.pkProducto=None
        self.detalles=None
        self.categoria=None
        self.existenciaProducto=None
        self.cantidadesVendidas=None
        self.precioProducto=None
        
    ## LLave primaria o codigo identificador del producto
    def getPrimaryKey(self):
        return self.pkProducto
    ##nombre productos  
    def getNombreProducto(self):
        return self.nombreProducto
    def setNombreProducto(self, name):
        self.nombreProducto= name 
    ## Existencia del producto   
    def getExistencia(self):
        return self.existenciaProducto
    def setExistencia(self, existencia):
        self.existenciaProducto= existencia 
    ##Cantidades vendidas
    def getCantidadesVendidas(self):
        return self.cantidadesVendidas
    def setCantidadesVendidas(self, productosVendidos):
        self.cantidadesVendidas= productosVendidos 
    ##categoria
    def getCategory(self):
        return self.categoria
    def setCategory(self, categoria):
        self.categoria= categoria
    #detalles
    def getDetalles(self):
        return self.detalles
    def setDetalles(self, detalles):
        self.detalles= detalles
    ##precio productos
    def getPrecio(self):
        return self.precioProducto
    def setPrecio(self, precio):
        self.precioProducto= precio 
            
  ###REGISTRAR PRODUCTOS
  #1. SE HACE CONEXION CON LA BASE DE DATOS.  
            
    def registrarProducto (self,nombre, cantidadExistencia, cantidadVendida, categoria, detalles, precioProducto):
        conexion1 = crearConexion()
        cursor = conexion1.cursor()
        try:
            cursor.execute("INSERT INTO products (nombre__producto,cantidad_existencia,cantidad_vendidas, categoria, detalles,precio_products) VALUES (%s,%s,%s,%s,%s,%s)", (nombre,cantidadExistencia,cantidadVendida,categoria,detalles,precioProducto))
            conexion1.commit()
            print("Datos Guardados con exito")
        except Exception as e:
            print(f"Erro al guardar los datos:{e}")
        finally:
            cursor.close()
            conexion1.close()
        
##CONSULTAR O BUSCAR PRODUCTOS
##2. DESPUES DE TENER YA LOS PRODUCTOS REGISTRADOS PROCEDEMOS A BUSCARLOS.
    def consultarProducto(self, producto):
        conexion1 = crearConexion()
        cursor = conexion1.cursor()
        try:
            cursor.execute(f"SELECT * FROM products WHERE products = %s", (producto))
            consulta = cursor.fetchall()
            return consulta
        except Exception as e:
            print(f"Error al consultar los productos: {e}")
            return None
        finally:
            cursor.close()
            conexion1.close()
    
###CONSULTA DE CATEGORIA
    def consultaCategoria(self,categoria):
        conexion1 = crearConexion()
        cursor = conexion1.cursor()
        try:
            cursor.execute(f"SELECT * FROM productos WHERE categoria = %s",(categoria))
            consulta = cursor.fetchall()
            return consulta
        except Exception as e:
            print(f"Error al consultar las categorías: {e}")
            return None
        finally:
            cursor.close()
            conexion1.close()
    
##GENERAR INFORME
    def crearArchivo(self,datoTitulo,contenidoInforme):
        nombreArchivo=datoTitulo+".txt"
        with open(nombreArchivo, 'w', encoding='utf-8') as archivo:
            json.dump(contenidoInforme, archivo)
        return nombreArchivo
    def leerArchivo(self,auxArchivo):
        with open(auxArchivo,"r") as archivo:
            datoContenido=archivo.read()
            print(datoContenido)
            archivo.close()
    
    def sobreescribirArchivo(self,auxArchivo):#falta añadir el contenido
        with open(auxArchivo,"w") as archivo:
            datoContenido=archivo.write()
            print(datoContenido)
            archivo.close()
            
    def agregar_al_Archivo(self,auxArchivo):#falta añadir el contenido
        with open(auxArchivo,"a") as archivo:
            datoContenido=archivo.write()
            print(datoContenido)
            archivo.close()
            
    def deserializar(self,nombreArchivo):
        with open(nombreArchivo+".txt","r") as archivo:
            datoCreado=json.load(archivo)
        return datoCreado