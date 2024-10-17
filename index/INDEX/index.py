from MODELOS.basededatos import crearConexion
from MODELOS.modeloProductos import Producto
from MODELOS.modeloUsuario import Usuario
from index.VISTA.vistas.vista_interfaz_inicial import Interfaz
from CONTROLADOR.controlador import Controlador
conexion=crearConexion()
objProducto=Producto(conexion)
objUsuario=Usuario(conexion)
objControlador=Controlador(objUsuario,objProducto)
Ventana=Interfaz(objControlador)
Ventana.ventana_ingreso()
Ventana.activar_mainloop()