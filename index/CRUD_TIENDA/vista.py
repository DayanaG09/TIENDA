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
        ventanaTienda.geometry("850x750")
        ventanaTienda.maxsize(850,750)
        ventanaTienda.title("DROGUERIA HAYBET SALUD")
        
        frameForCanvas=tk.Frame(ventanaTienda)
        frameForCanvas.pack(fill="both",expand=True)
        
        canvas=tk.Canvas(frameForCanvas)
        canvas.pack(side="left",fill="both",expand=True)
        
        scrollbar=tk.Scrollbar(frameForCanvas, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")
        
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))     
        
        framePrincipal=tk.Frame(canvas)
        framePrincipal.config(bg="#80b380",pady=10,padx=10)
        
        canvas.create_window((0,0), window=framePrincipal, anchor="nw")

        def _on_mouse_wheel(event):
            canvas.yview_scroll(-1 * int((event.delta / 120)), "units")

        canvas.bind_all("<MouseWheel>", _on_mouse_wheel)
        
        frameEncabezado=tk.Frame(framePrincipal)
        frameEncabezado.config(bg="#98c3a1",height=200)
        frameEncabezado.pack(padx=10,pady=10, expand=True, fill="both")
        frameSecciones=tk.Frame(frameEncabezado)
        frameSecciones.config(bg="#fcf6d2")
        frameSecciones.place(relx=0.16,rely=0.05,relheight=0.9,relwidth=0.28,anchor="n")
        home=tk.Button(frameSecciones, text="Home")
        home.place(relx=0.125,rely=0.81,relheight=0.2,relwidth=0.25,anchor="n")
        products=tk.Button(frameSecciones, text="Products")
        products.place(relx=0.37,rely=0.81,relheight=0.2,relwidth=0.25,anchor="n")
        about=tk.Button(frameSecciones, text="About")
        about.place(relx=0.62,rely=0.81,relheight=0.2,relwidth=0.25,anchor="n")
        contact=tk.Button(frameSecciones, text="Contact")
        contact.place(relx=0.87,rely=0.81,relheight=0.2,relwidth=0.25,anchor="n")
        frameTituloEmpresa=tk.Frame(frameEncabezado)
        frameTituloEmpresa.config(bg="#7b6ed6")
        frameTituloEmpresa.place(relx=0.52,rely=0.05,relheight=0.9,relwidth=0.4,anchor="n")
        nombre=tk.Label(frameTituloEmpresa, text="DROGUERIA HAYBET")
        nombre.config(width=15,height=8)
        nombre.pack(expand=True)
        frameImagenEncabezado=tk.Frame(frameEncabezado)
        frameImagenEncabezado.config(bg="#cc9b25")
        frameImagenEncabezado.place(relx=0.86,rely=0.05,relheight=0.9,relwidth=0.24,anchor="n")
        imagen=tk.Label(frameImagenEncabezado,text="Imagen")
        imagen.pack(expand=True)
        
        frameContenido=tk.Frame(framePrincipal)
        frameContenido.config(width=800,height=550,bg="#25857d")
        frameContenido.pack(pady=10,padx=10,expand=True, fill="both")
        frameLateral=tk.Frame(frameContenido)
        frameLateral.config(bg="#f9d423")
        frameLateral.place(relx=0.11,rely=0.02,relheight=0.96,relwidth=0.2,anchor="n")
        labelLateral=tk.Label(frameLateral, text="lateral")
        labelLateral.pack()
        frameOptions=tk.Frame(frameLateral)
        frameOptions.config(bg="#ddffab")
        frameOptions.place(relx=0.5,rely=0.28,relheight=0.7,relwidth=0.95, anchor="n")
        Apps=tk.Frame(frameOptions)
        Apps.config(bg="#d9abff")
        Apps.pack(expand=True,fill="both")
        lApps=tk.Label(Apps, text="Apps")
        lApps.pack(side="left")
        Games=tk.Frame(frameOptions)
        Games.config(bg="#3a89c9")
        Games.pack(expand=True,fill="both")
        lGames=tk.Label(Games, text="Games")
        lGames.pack(side="left")
        Movies=tk.Frame(frameOptions)
        Movies.config(bg="#f9c593")
        Movies.pack(expand=True,fill="both")
        lMovies=tk.Label(Movies, text="Movies")
        lMovies.pack(side="left")
        Books=tk.Frame(frameOptions)
        Books.config(bg="#84967e")
        Books.pack(expand=True,fill="both")
        lBooks=tk.Label(Books, text="Books")
        lBooks.pack(side="left")
        Newspapers=tk.Frame(frameOptions)
        Newspapers.config(bg="#59baa9")
        Newspapers.pack(expand=True,fill="both")
        lNewspapers=tk.Label(Newspapers, text="Newspapers")
        lNewspapers.pack(side="left")
        frameCategorias=tk.Frame(frameContenido)
        frameCategorias.place(relx=0.605,rely=0.02,relheight=0.1, relwidth=0.77,anchor="n")
        botonC1=tk.Button(frameCategorias, text="Categoría")
        botonC1.place(relx=0.1,rely=0.2,relheight=0.6, relwidth=0.18,anchor="n")
        botonC2=tk.Button(frameCategorias, text="Categoría")
        botonC2.place(relx=0.3,rely=0.2,relheight=0.6, relwidth=0.18,anchor="n")
        botonC3=tk.Button(frameCategorias, text="Categoría")
        botonC3.place(relx=0.5,rely=0.2,relheight=0.6, relwidth=0.18,anchor="n")
        botonC4=tk.Button(frameCategorias, text="Categoría")
        botonC4.place(relx=0.7,rely=0.2,relheight=0.6, relwidth=0.18,anchor="n")
        botonC5=tk.Button(frameCategorias, text="Categoría")
        botonC5.place(relx=0.9,rely=0.2,relheight=0.6, relwidth=0.18,anchor="n")
        frameProductos=tk.Frame(frameContenido)
        frameProductos.place(relx=0.605,rely=0.13,relheight=0.85, relwidth=0.77,anchor="n")
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
        frameLeft=tk.Frame(framePiePagina, bg="#e97f02")
        frameLeft.place(relx=0.25,rely=0.05,relheight=0.9, relwidth=0.45,anchor="n")
        frameRight=tk.Frame(framePiePagina, bg="#e97f02")
        frameRight.place(relx=0.75,rely=0.05,relheight=0.9, relwidth=0.45,anchor="n")
        pieHome=tk.Button(frameRight, text="Home")
        pieHome.place(relx=0.1,rely=0.25,relheight=0.5, relwidth=0.2,anchor="n")
        pieApps=tk.Button(frameRight, text="Apps")
        pieApps.place(relx=0.3,rely=0.25,relheight=0.5, relwidth=0.2,anchor="n")
        pieGames=tk.Button(frameRight, text="Games")
        pieGames.place(relx=0.5,rely=0.25,relheight=0.5, relwidth=0.2,anchor="n")
        pieMovies=tk.Button(frameRight, text="Movies")
        pieMovies.place(relx=0.7,rely=0.25,relheight=0.5, relwidth=0.2,anchor="n")
        pieBooks=tk.Button(frameRight, text="Books")
        pieBooks.place(relx=0.9,rely=0.25,relheight=0.5, relwidth=0.2,anchor="n")
        #crear secciones del mockup
        
        #falta crear la interfaz de informe de productos
        #tambien hay que hacer dos interfaces(administrador,cliente)
        
    def activar_mainloop(self):
        tk.mainloop()
        

Ventana=Interfaz()
Ventana.ventanaHome()
Ventana.activar_mainloop()