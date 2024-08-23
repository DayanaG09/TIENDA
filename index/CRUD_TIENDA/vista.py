import tkinter as tk
from tkinter import messagebox

class Interfaz:
    def __init__(self):
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
        ventanaTienda=tk.Tk()
        ventanaTienda.config(width=1200,height=1200)
        ventanaTienda.title("DROGUERIA HAYBET SALUD")
        
        framePrincipal=tk.Frame(ventanaTienda)
        framePrincipal.config(bg="#80b380")
        framePrincipal.pack(expand=True, fill="both")
        
        frameEncabezado=tk.Frame(framePrincipal)
        frameEncabezado.config(bg="#98c3a1")
        frameEncabezado.pack(padx=10,pady=10, expand=True, fill="both")
        frameSecciones=tk.Frame(frameEncabezado)
        frameSecciones.config(bg="#75c9a3")
        frameSecciones.grid(column=0,row=0)
        home=tk.Button(frameSecciones)
        home.grid(column=0,row=0,sticky="s")
        labelHome=tk.Label(home, text="Home")
        labelHome.pack()
        products=tk.Button(frameSecciones)
        products.grid(column=1,row=0,sticky="s")
        labelProducts=tk.Label(products,text="Products")
        labelProducts.pack()
        about=tk.Button(frameSecciones)
        about.grid(column=2,row=0,sticky="s")
        labelAbout=tk.Label(about,text="About")
        labelAbout.pack()
        contact=tk.Button(frameSecciones)
        contact.grid(column=3,row=0,sticky="s")
        labelContact=tk.Label(contact,text="Contact")
        labelContact.pack()
        frameTituloEmpresa=tk.Frame(frameEncabezado)
        frameTituloEmpresa.config(bg="#75c9a3")
        frameTituloEmpresa.grid(column=1,row=0)
        nombre=tk.Label(frameTituloEmpresa, text="DROGUERIA HAYBET")
        nombre.config(width=15,height=8)
        nombre.pack()
        frameImagenEncabezado=tk.Frame(frameEncabezado)
        frameImagenEncabezado.config(bg="#75c9a3")
        frameImagenEncabezado.grid(column=2,row=0)
        imagen=tk.Label(frameImagenEncabezado,text="Imagen")
        imagen.pack()
        
        frameContenido=tk.Frame(framePrincipal)
        frameContenido.config(width=800,height=550,bg="#25857d")
        frameContenido.pack(pady=10,expand=True, fill="both")
        frameLateral=tk.Frame(frameContenido)
        frameLateral.pack(pady=10,padx=20)
        labelLateral=tk.Label(frameLateral, text="lateral")
        labelLateral.pack()
        frameCategorias=tk.Frame(frameContenido)
        frameCategorias.pack(pady=10)
        labelCategorias=tk.Label(frameCategorias, text="Categorias")
        labelCategorias.pack()
        frameProductos=tk.Frame(frameContenido)
        frameProductos.pack(pady=5)
        frmTituloCatalogo=tk.Frame(frameProductos)
        frmTituloCatalogo.pack(padx=5,pady=5)
        labelTituloCatalogo=tk.Label(frmTituloCatalogo,text="TITULO DE CATALOGO")
        labelTituloCatalogo.pack()
        frmContenidoProductos=tk.Frame(frameProductos)
        frmContenidoProductos.pack()
        labelContenidoProductos=tk.Label(frmContenidoProductos, text="CONTENIDO")
        labelContenidoProductos.pack()
        #ahora averiguar si toca hacer un frame por cada producto.
        
        framePiePagina=tk.Frame(framePrincipal)
        framePiePagina.config(width=800,height=100)
        framePiePagina.pack(pady=10)
        #crear secciones del mockup
        
        #falta crear la interfaz de informe de productos
        #tambien hay que hacer dos interfaces(administrador,cliente)
        
    def activar_mainloop(self):
        tk.mainloop()
        

Ventana=Interfaz()
Ventana.ventanaHome()
Ventana.activar_mainloop()
        
        