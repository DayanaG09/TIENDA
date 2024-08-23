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
        framePrincipal.config(bg="#80b380",pady=10,padx=10)
        framePrincipal.pack(expand=True, fill="both")
        
        frameEncabezado=tk.Frame(framePrincipal)
        frameEncabezado.config(bg="#98c3a1",height=200)
        frameEncabezado.pack(padx=10,pady=10, expand=True, fill="both")
        frameSecciones=tk.Frame(frameEncabezado)
        frameSecciones.config(bg="#fcf6d2")
        frameSecciones.place(relx=0.16,rely=0.05,relheight=0.9,relwidth=0.24,anchor="n")
        home=tk.Button(frameSecciones)
        home.place(relx=0.12,rely=0.81,relheight=0.18,relwidth=0.2,anchor="n")
        labelHome=tk.Label(home, text="Home")
        labelHome.pack(expand=True)
        products=tk.Button(frameSecciones)
        products.place(relx=0.35,rely=0.81,relheight=0.18,relwidth=0.2,anchor="n")
        labelProducts=tk.Label(products,text="Products")
        labelProducts.pack(expand=True)
        about=tk.Button(frameSecciones)
        about.place(relx=0.57,rely=0.81,relheight=0.18,relwidth=0.2,anchor="n")
        labelAbout=tk.Label(about,text="About")
        labelAbout.pack(expand=True)
        contact=tk.Button(frameSecciones)
        contact.place(relx=0.8,rely=0.81,relheight=0.18,relwidth=0.2,anchor="n")
        labelContact=tk.Label(contact,text="Contact")
        labelContact.pack(expand=True)
        frameTituloEmpresa=tk.Frame(frameEncabezado)
        frameTituloEmpresa.config(bg="#7b6ed6")
        frameTituloEmpresa.place(relx=0.5,rely=0.05,relheight=0.9,relwidth=0.40,anchor="n")
        nombre=tk.Label(frameTituloEmpresa, text="DROGUERIA HAYBET")
        nombre.config(width=15,height=8)
        nombre.pack(expand=True)
        frameImagenEncabezado=tk.Frame(frameEncabezado)
        frameImagenEncabezado.config(bg="#cc9b25")
        frameImagenEncabezado.place(relx=0.83,rely=0.05,relheight=0.9,relwidth=0.24,anchor="n")
        imagen=tk.Label(frameImagenEncabezado,text="Imagen")
        imagen.pack(expand=True)
        
        frameContenido=tk.Frame(framePrincipal)
        frameContenido.config(width=800,height=550,bg="#25857d")
        frameContenido.pack(pady=10,padx=10,expand=True, fill="both")
        
        frameLateral=tk.Frame(frameContenido)
        frameLateral.config(bg="#f9d423")
        frameLateral.place(relx=0.11,rely=0.07,relheight=0.85,relwidth=0.2,anchor="n")
        labelLateral=tk.Label(frameLateral, text="lateral")
        labelLateral.pack()
        
        frameCategorias=tk.Frame(frameContenido)
        frameCategorias.place(relx=0.55,rely=0.07,relheight=0.2, relwidth=0.65,anchor="n")
        labelCategorias=tk.Label(frameCategorias, text="Categorias")
        labelCategorias.pack()
        
        frameProductos=tk.Frame(frameContenido)
        frameProductos.place(relx=0.55,rely=0.3,relheight=0.6, relwidth=0.65,anchor="n")
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