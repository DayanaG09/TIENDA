import json
from datetime import datetime
class Controlador:
    def __init__(self,objModeloUsuario,objModeloProducto,objModeloCategoria):
        self.objModeloUsuario=objModeloUsuario
        self.objModeloProducto=objModeloProducto
        self.objModeloCategoria=objModeloCategoria
        
    def validar_inicio_sesion(self,listaUsuario):
        listaUsuarioDatos=listaUsuario
        self.objModeloUsuario.set_usuario(listaUsuarioDatos)
        validacion_consulta=self.objModeloUsuario.validar_usuario()
        return validacion_consulta
    
    def consultar_usuarios(self):
        consultaUsuario=self.objModeloUsuario.consultar_usuario()
        return consultaUsuario

    def crear_producto(self, lista_productos):
        lista_productos_datos=lista_productos
        self.objModeloProducto.set_producto2(lista_productos_datos)    
        validar_consulta=self.objModeloProducto.crear_producto()
        return validar_consulta
        
    def modificar_producto(self,lista_productos):
        if len(lista_productos) < 7:
            print("Error: no se pasó el ID del producto.")
            return False
        lista_productos_datos=lista_productos
        self.objModeloProducto.set_producto(lista_productos_datos)    
        validar_consulta=self.objModeloProducto.modificar_producto()
        return validar_consulta
        
    def eliminar_producto(self,id):
        id_producto=id
        self.objModeloProducto.set_id_producto(id_producto)    
        validar_consulta=self.objModeloProducto.eliminar_producto()
        return validar_consulta
    
    def consultar_productos_masVendidos(self):
        listaMasVendidos=self.objModeloProducto.consultar_productos_masVendidos()
        return listaMasVendidos
    
    def consultar_productos_menosVendidos(self):
        listaMenosVendidos=self.objModeloProducto.consultar_productos_menosVendidos()
        return listaMenosVendidos
        
    def consultar_productos(self):
        consulta_producto=self.objModeloProducto.consultar_productos()
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
        fecha_actual = datetime.now()
        fecha_formateada = fecha_actual.strftime('%Y-%m-%d %H:%M:%S')

        listaMasVendidos = self.objModeloProducto.consultar_productos_masVendidos()
        listaMenosVendidos = self.objModeloProducto.consultar_productos_menosVendidos()

        informe = {
            "fecha_informe": fecha_formateada,
            "productos_mas_vendidos": [
                {"nombre": listaMasVendidos[i][0], "cantidad": listaMasVendidos[i][1]} 
                for i in range(min(4, len(listaMasVendidos)))
            ],
            "productos_menos_vendidos": [
                {"nombre": listaMenosVendidos[i][0], "cantidad": listaMenosVendidos[i][1]} 
                for i in range(min(4, len(listaMenosVendidos)))
            ]
        }

        nombreArchivo = "Informe_de_ventas.txt"
        with open(nombreArchivo, 'w', encoding='utf-8') as archivo:
            json.dump(informe, archivo, ensure_ascii=False, indent=4)
    