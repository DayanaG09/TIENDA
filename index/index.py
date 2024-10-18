import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from MODELOS.basededatos import crearConexion
from MODELOS.modeloProductos import Producto
from MODELOS.modeloUsuario import Usuario
from VISTA.vistas.vista_login import Login
from CONTROLADOR.controlador import Controlador
conexion=crearConexion()
objProducto=Producto(conexion)
objUsuario=Usuario(conexion)
objControlador=Controlador(objUsuario,objProducto)
Ventana=Login(objControlador)
Ventana.ventana_ingreso()
Ventana.activar_mainloop()