from MODELOS.basededatos import crearConexion
from MODELOS.modeloProductos import Producto
from MODELOS.modeloUsuario import Usuario
from VISTA.vista import Interfaz
from CONTROLADOR.controlador import Controlador
conexion=crearConexion()
objProducto=Producto(conexion)
objUsuario=Usuario(conexion)
objControlador=Controlador(objUsuario,objProducto)
Ventana=Interfaz(objControlador)
Ventana.ventana_ingreso()
Ventana.activar_mainloop()