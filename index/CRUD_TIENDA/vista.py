import tkinter as tk
from tkinter import messagebox

class Interfaz:
    def __init__(self,objControlador):
        self.nombreUsuario=None
        self.documentoUsuario=None
        self.objControlador=None
        
    def set_controlador(self,controlador):
        self.objControlador=controlador
        
    def ventana(self):
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
        botonIngresar=tk.Button(frameLogin,text="INGRESAR",command=None)
        botonIngresar.config(font=(16,"bold"))
        botonIngresar.pack()
        
        ventanaTienda=tk.Tk
        