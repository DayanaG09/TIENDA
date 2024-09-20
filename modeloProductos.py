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
        self.datos=[]
    
        ##Datos
        def getDatos(self):
            return self.datos
        def setDatos(self, datos):
            self.datos= datos
        ##nombre productos  
        def getNombreProducto(self):
            return self.nombreProducto
        def setNombreProducto(self, name):
            self.nombreProducto= name 
        ## LLave primaria o codigo identificador del producto
        def getPrimaryKey(self):
            return self.pkProducto
        def setPrimaryKey(self, codigo):
            self.pkProducto= codigo 
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
        ##precio productos
        def getPrecio(self):
            return self.precioProducto
        def setPrecio(self, precio):
            self.precioProducto= precio 
        #detalles
        def getDetalles(self):
            return self.detalles
        def setDetalles(self, detalles):
            self.detalles= detalles
        ##categoria
        def getCategory(self):
            return self.categoria
        def setCategory(self, categoria):
            self.categoria= categoria
            
  ###REGISTRAR PRODUCTOS
  #1. SE HACE CONEXION CON LA BASE DE DATOS.  
            
    def registrarProducto (name, codigo,existencia, productosVendidos, precio, detalles, categoria):
                conexion1 = crearConexion()
                cursor = conexion1.cursor()
                cursor.execute(f"INSERT INTO productos (name, codigo, existencia, productosVendidos, precio) VALUES ('{name}','{codigo}','{existencia}','{detalles}','{categoria}','{productosVendidos}','{precio}')")
                conexion1.commit()
                print("Datos Guardados con exito")
    
##CONSULTAR O BUSCAR PRODUCTOS
##2. DESPUES DE TENER YA LOS PRODUCTOS REGISTRADOS PROCEDEMOS A BUSCARLOS.
    def consultarProductos():
            conexion1 = crearConexion()
            cursor = conexion1.cursor()
            cursor.execute(f"SELECT * FROM productos")
            consulta = cursor.fetchall()
            return consulta
    
###CONSULTA DE CATEGORIA
    def consultaCategoria(categoria):
            conexion1 = conexion1.crearConexion()
            cursor = conexion1.cursor()
            cursor.execute(f"SELECT * FROM productos WHERE categoria = '{categoria}'")
            consulta = cursor.fetchall()
            return consulta
    
##GENERAR INFORME
    def crearArchivo(self,datoTitulo,datosInforme):
        nombreArchivo=datoTitulo+".txt"
        with open(nombreArchivo, 'w', encoding='utf-8') as archivo:
            json.dump(datosInforme, archivo)
        return nombreArchivo
    def leerArchivo(self,auxArchivo):
        with open(auxArchivo,"r") as archivo:
            datoContenido=archivo.read()
            print(datoContenido)
            archivo.close()
    
    def sobreescribirArchivo(self,auxArchivo):
        with open(auxArchivo,"w") as archivo:
            datoContenido=archivo.write()
            print(datoContenido)
            archivo.close()
            
    def agregar_al_Archivo(self,auxArchivo):
        with open(auxArchivo,"a") as archivo:
            datoContenido=archivo.write()
            print(datoContenido)
            archivo.close()
            
    def deserializar(self,nombreArchivo):
        with open(nombreArchivo+".txt","r") as archivo:
            datoCreado=json.load(archivo)
        return datoCreado
            
            
Producto.datos= Producto.consultarProductos()
print(Producto.datos)
respuesta = Producto.consultaCategoria()
print(respuesta)
nombre_a=input("Nombre del producto:")
detalles_a= input("Detalles: ")
categoria_a= input("Categoria: ")
precio_a=float("Precio: ")
Out=int("Cantidades vendidas: ")

Producto.name = nombre_a
Producto.detalles = detalles_a
Producto.categoria = categoria_a
Producto.precio= precio_a
Producto.cantidadesVendidas= Out

Producto.registrarProducto (Producto.name, Producto.detalles, Producto.categoria, Producto.precio, Producto.cantidadesVendidas)
