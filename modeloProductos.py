from basededatos import crearConexion
import json

class Producto:
    
    def __init__(self):
        self.idProducto=None
        self.nombre=None
        self.existencia=None
        self.cantidadesVendidas=None
        self.categoria=None
        self.detalles=None
        self.precio=None
        
    ## LLave primaria o codigo identificador del producto
    def getIdProducto(self):
        return self.idProducto
    ##nombre productos  
    def getNombre(self):
        return self.nombre
    def setNombre(self, nombre):
        self.nombre = nombre
    ## Existencia del producto   
    def getExistencia(self):
        return self.existencia
    def setExistencia(self, existencia):
        self.existencia= existencia 
    ##Cantidades vendidas
    def getCantidadesVendidas(self):
        return self.cantidadesVendidas
    def setCantidadesVendidas(self, cantidadesVendidas):
        self.cantidadesVendidas= cantidadesVendidas 
    ##categoria
    def getCategoria(self):
        return self.categoria
    def setCategoria(self, categoria):
        self.categoria= categoria
    #detalles
    def getDetalles(self):
        return self.detalles
    def setDetalles(self, detalles):
        self.detalles= detalles
    ##precio productos
    def getPrecio(self):
        return self.precio
    def setPrecio(self, precio):
        self.precio = precio
        
    def setProducto(self,listaProductos):
        self.setNombre(listaProductos[0])
        self.setExistencia(listaProductos[1])
        self.setcantidadesVendidas(listaProductos[2])
        self.setCategoria(listaProductos[3])
        self.setDetalles(listaProductos[4])
        self.setPrecio(listaProductos[5])
            
  ###REGISTRAR PRODUCTOS
  #1. SE HACE CONEXION CON LA BASE DE DATOS.  
            
    def crearProducto (self, listaProductos):
        conexion1 = crearConexion()
        cursor = conexion1.cursor()
                
        #PARA OBTENER LA FECHA ACTUAL - SE USARÁ EN LA VISTA
        #fecha_actual = datetime.now()
        #fecha_formateada = fecha_actual.strftime('%Y-%m-%d %H:%M:%S')
        #from datetime import datetime
        
        try:
            cursor.execute("INSERT INTO produco (nombre__producto,cantidad_existencia,cantidad_vendidas, categoria, detalles,precio_products) VALUES (%s,%s,%s,%s,%s,%s)", (self.nombre,self.existencia,self.cantidadesVendidas,self.categoria,self.detalles,self.precio))
            conexion1.commit()
            print("Datos Guardados con exito")
        except Exception as e:
            print(f"Erro al guardar los datos:{e}")
        finally:
            cursor.close()
            conexion1.close()
        
##CONSULTAR O BUSCAR PRODUCTOS
##2. DESPUES DE TENER YA LOS PRODUCTOS REGISTRADOS PROCEDEMOS A BUSCARLOS.
    def consultarProductos(self):
        conexion1 = crearConexion()
        cursor = conexion1.cursor()
        try:
            cursor.execute("SELECT * FROM producto")
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
            cursor.execute(f"SELECT * FROM producto WHERE categoria = %s",(categoria))
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