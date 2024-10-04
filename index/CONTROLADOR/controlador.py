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
