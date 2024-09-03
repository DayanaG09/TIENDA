class productos: 
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
    def getDatos():
        return self.datos
    def setDatos():
        self.datos= dato 
    ##nombre productos  
    def getDatos():
        return self.datos
    def setNombreProducto(name):
        self.nombreProducto= name 
    ## LLave primaria o codigo identificador del producto
    def getPrimaryKey():
        return self.pkProducto
    def setPrimaryKey(codigo):
        self.pkProducto= codigo 
    ## Existencia del producto   
    def getExistencia():
        return self.existenciaProducto
    def setExistencia(existencia):
        self.existenciaProducto= existencia 
    ##Cantidades vendidas
    def getCantidadesVendidas():
        return self.cantidadesVendidas
    def setCantidadesVendidas(productosVendidos):
        self.cantidadesVendidas= productosVendidos 
    ##precio productos
    def getPrecio():
        return self.precioProducto
    def setPrecio(precio):
        self.precioProducto= precio 
    #detalles
    def getDetalles():
        return self.detalles
    def setDetalles(detalles):
        self.detalles= detalles
    ##categoria
    def getCategory():
        return self.categoria
    def setCategory(categoria):
        self.categoria= categoria
        
    ###REGISTRAR PRODUCTOS
    #1. SE HACE CONEXION CON LA BASE DE DATOS.  
        
    def registrarProducto (name, codigo,existencia, productosVendidos, precio, detalles, categoria):
            conexion1 = conexion.crearConexion()
            cursor = conexion1.cursor()
            cursor.execute(f"INSERT INTO productos (name, codigo, existencia, productosVendidos, precio) VALUES ('{name}','{codigo}','{existencia}','{detalles}','{categoria}','{productosVendidos}','{precio}')")
            conexion1.commit()
            print("Datos Guardados con exito")
        
    ##CONSULTAR O BUSCAR PRODUCTOS
    ##2. DESPUES DE TENER YA LOS PRODUCTOS REGISTRADOS PROCEDEMOS A BUSCARLOS.
    def consultarProductos():
            conexion1 = conexion.crearConexion()
            cursor = conexion1.cursor()
            cursor.execute(f"SELECT * FROM productos")
            consulta = cursor.fetchall()
            return consulta
        
    ###CONSULTA DE CATEGORIA
    def consultaCategoria(categoria):
            conexion1 = conexion.crearConexion()
            cursor = conexion1.cursor()
            cursor.execute(f"SELECT * FROM productos WHERE categoria = '{categoria}'")
            consulta = cursor.fetchall()
            return consulta
        
    ##GENERAR INFORME
    def generarInforme(productosVendidos):
                with open(f'{productosVendidos}', 'w', encoding='utf8') as archivo:

                    json.dumps(productos.datos, archivo)
                print("informe generado")
                
            
productos.datos= productos.consultarProductos()
print(productos.datos)
respuesta = productos.consultaCategoria()
print(respuesta)
nombre_a=input("Nombre del producto:")
detalles_a= input("Detalles: ")
categoria_a= input("Categoria: ")
precio_a=float("Precio: ")
Out=int("Cantidades vendidas: ")



productos.name = nombre_a
productos.detalles = detalles_a
productos.categoria = categoria_a
productos.precio= precio_a
productos.cantidadesVendidas= Out

productos.registrarProducto (productos.name, productos.detalles, productos.categoria, productos.precio, productos.cantidadesVendidas)
