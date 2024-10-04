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
        
    def consulta_productos(self):
        consulta_producto=self.objModeloUsuario.consultar_producto()
        return consulta_producto
        
    def consulta_categoria(self):
        consulta_categoria=self.objModeloCategoria.consultar_categoria()
        return consulta_categoria
    