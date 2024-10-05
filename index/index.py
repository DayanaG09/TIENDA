from MODELOS.basededatos import crearConexion
from MODELOS.modeloCategoria import Categoria
from MODELOS.modeloProductos import Producto
from MODELOS.modeloUsuario import Usuario
from VISTA.vista import Interfaz
from CONTROLADOR.controlador import Controlador
conexion=crearConexion()
objCategoria=Categoria(conexion)
objProducto=Producto(conexion)
objUsuario=Usuario(conexion)
objControlador=Controlador(objUsuario,objProducto,objCategoria)
Ventana=Interfaz(objControlador)
Ventana.ventana_ingreso()
Ventana.activar_mainloop()