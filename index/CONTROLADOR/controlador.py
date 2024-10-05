class Controlador:
    def __init__(self,objModeloUsuario,objModeloProducto,objModeloCategoria):
        self.objModeloUsuario=objModeloUsuario
        self.objModeloProducto=objModeloProducto
        self.objModeloCategoria=objModeloCategoria
        
    def validar_inicio_sesion(self,listaUsuario):
        listaUsuarioDatos=listaUsuario
        self.objModeloUsuario.set_usuario(listaUsuarioDatos)
        validacion_consulta=self.objModeloUsuario.validarUsuario()
        return validacion_consulta
    
    def consultar_usuarios(self):
        consultaUsuario=self.objModeloUsuario.consultar_usuario()
        return consultaUsuario

    def crear_producto(self, lista_productos):
        lista_productos_datos=lista_productos
        self.objModeloProducto.set_producto(lista_productos_datos)    
        validar_consulta=self.objModeloProducto.crear_producto()
        return validar_consulta
        
    def modificar_producto(self,lista_productos):
        lista_productos_datos=lista_productos
        self.objModeloProducto.setProducto(lista_productos_datos)    
        validar_consulta=self.objModeloProducto.modificar_producto()
        return validar_consulta
        
    def eliminar_producto(self,lista_productos):
        lista_productos_datos=lista_productos
        self.objModeloProducto.set_producto(lista_productos_datos)    
        validar_consulta=self.objModeloProducto.eliminar_producto()
        return validar_consulta
    
    def consultar_producto(self,producto):
        self.objModeloProducto.set_id_producto(producto)
        self.objModeloProducto.consultar_producto()
        producto_nuevo=self.objModeloProducto.get_nombre()
        return producto_nuevo
        
    def consultar_productos(self):
        consulta_producto=self.objModeloUsuario.consultar_productos()
        return consulta_producto
    
    def consulta_categoria(self,categoria):
        self.objModeloCategoria.set_id(categoria)
        self.objModeloCategoria.consulta_categoria()
        categoria_nueva=self.objModeloCategoria.get_id()
        return categoria_nueva
        
    def consultar_categoria(self):
        consulta_categoria=self.objModeloCategoria.consultar_categorias()
        return consulta_categoria
    
    def crear_archivo(self):
        datoUsuario=self.objModelo.get_listaUsuarios()
        datoTitulo=self.objModelo.get_nombreArchivo()
        archivoCreado=self.objModelo.crearArchivo(datoUsuario,datoTitulo)
        self.objModelo.leerArchivo(archivoCreado)
    