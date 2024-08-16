import tkinter as tk
from tkinter import messagebox

class Interfaz:
    def __init__(self,objControlador):
        self.nombreUsuario=None
        self.documentoUsuario=None
        self.objControlador=None
        
    def set_controlador(self,controlador):
        self.objControlador=controlador
        
    def ventanaIngreso(self):
        ventanaLogin=tk.Tk()
        ventanaLogin.config(width=600,height=800)
        ventanaLogin.title("INICIO SESION HAYBET SALUD")
        frameInicioSesion=tk.Frame(ventanaLogin)
        frameInicioSesion.config(bg="light blue",width=400,height=400)
        frameInicioSesion.pack()
        frameTitulo=tk.Frame(frameInicioSesion)
        frameTitulo.pack(pady=20)
        labelInicioSesion=tk.Label(frameTitulo,text="INICIO DE SESION")
        labelInicioSesion.config(font=(18,"bold"))
        labelInicioSesion.pack()
        frameLogin=tk.Frame(frameInicioSesion)
        frameLogin.pack()
        labelNombre=tk.Label(frameLogin,text="Nombre")
        labelNombre.config(font=(14))
        labelNombre.pack(pady=(10,5))
        self.nombreUsuario=tk.StringVar()
        entryNombre=tk.Entry(frameLogin,textvariable=self.nombreUsuario)
        entryNombre.pack((0,10))
        labelDocumento=tk.Label(frameLogin,text="Documento")
        labelDocumento.config(font=(14))
        labelDocumento.pack(pady=(0,5))
        self.documentoUsuario=tk.StringVar()
        entryDocumento=tk.Entry(frameLogin,textvariable=self.documentoUsuario)
        entryDocumento.pack(pady=(0,10))
        botonIngresar=tk.Button(frameLogin,text="INGRESAR",command=self.funcionIngresar)
        botonIngresar.config(font=(16,"bold"))
        botonIngresar.pack()
        
    def funcionIngresar(self):
        try:
            nombre=self.nombreUsuario.get()
            documento=self.documentoUsuario.get()
            self.objControlador.inicioSesion(nombre,documento)
        except ValueError:
            messagebox.showerror("Error","Los campos deben ser llenados correctamente")
            
    def ventanaHome(self):
        ventanaTienda=tk.Tk
        ventanaTienda.config(width=900,height=900)
        ventanaTienda.title("DROGUERIA HAYBET SALUD")
        
        frameEncabezado=tk.Frame(ventanaTienda)
        frameEncabezado.config(width=800,height=200)
        frameEncabezado.pack(pady=10)
        frameSecciones=tk.Frame(frameEncabezado)
        frameSecciones.pack(padx=5)
        frameTituloEmpresa=tk.Frame(frameEncabezado)
        frameTituloEmpresa.pack(padx=5)
        frameImagen=tk.Frame(frameEncabezado)
        frameImagen.pack(padx=5)
        
        frameContenido=tk.Frame(ventanaTienda)
        frameContenido.config(width=800,height=550)
        frameContenido.pack(pady=10)
        frameLateral=tk.Frame(frameContenido)
        frameLateral.pack(pady=10,padx=20)
        #crear cada uno de las secciones que aparecen en el mockup
        frameCategorias=tk.Frame(frameContenido)
        frameCategorias.pack(pady=10)
        frameProductos=tk.Frame(frameContenido)
        frameProductos.pack(pady=5)
        frmTituloCatalogo=tk.Frame(frameProductos)
        frmTituloCatalogo.pack(padx=10,pady=10)
        #ahora averiguar si toca hacer un frame por cada producto.
        
        framePiePagina=tk.Frame(ventanaTienda)
        framePiePagina.config(width=800,height=100)
        framePiePagina.pack(pady=10)
        #crear secciones del mockup
        
        #falta crear la interfaz de informe de productos
        #tambien hay que hacer dos interfaces(administrador,cliente)
        
        