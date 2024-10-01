import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image

class Interfaz:
    def __init__(self):
        self.ventanaLogin=None
        self.nombreUsuario=None
        self.documentoUsuario=None
        self.objControlador=None
        self.logo=None
        self.reproducir=None
        self.pastilla=None
        self.frameContenido=None
        self.image=None
        self.image1=None
        self.image2=None
        self.image0=None
        self.image3=None
        self.image4=None
        self.image5=None
        self.image6=None
        self.image7=None
        self.image8=None
        self.images=None
    def set_controlador(self,controlador):
        self.objControlador=controlador
        
        #SE DEBE BUSCAR LA MANERA DE VALIDACIÓN DE DATOS CON LA BASE DE DATOS
        #FALTA DESTINAR COLORES ESPECIFCOS E INNOVACION PARA LA INTERFAZ
        #FALTA HACER ALGUNOS CAMBIOS PARA TENER UNA INTERFAZ DIFERENTE PARA ADMIN Y OTRA PARA VENDEDOR
        #SE DEBEN CARGAR IMAGENES Y NOMBRE CON DESCRIPCION Y PRECIO PARA LOS PRODUCTOS
    def ventanaIngreso(self):
        self.ventanaLogin=tk.Tk()
        self.ventanaLogin.geometry("600x800")
        self.ventanaLogin.maxsize(600,800)
        self.ventanaLogin.title("INICIO SESION HAYBET SALUD")
        letra=("Georgia", 20, "bold")
        self.images = self.interfacePictures(r"index\CRUD_TIENDA\imagenes\pastillas.jpg", 250, 190)

        
        frameInicioSesion=tk.Frame(self.ventanaLogin)
        frameInicioSesion.config(bg="#96c7e6",width=400,height=500)
        frameInicioSesion.pack(expand=True,fill="both")
        
        frameTitulo=tk.Frame(frameInicioSesion)
        frameTitulo.place(relx=0.7,rely=0,relheight=0.242, relwidth=0.69, anchor="n")
        labelTitulo=tk.Label(frameTitulo,bg= "white", text="INICIO DE SESION")
        labelTitulo.config(font=letra, fg="#719ae2")
        labelTitulo.pack(expand=True,fill="both")
        
        frameLogin=tk.Frame(frameInicioSesion, bg="#96c7e6")
        frameLogin.place(relx=0.5,rely=0.25,relheight=0.7, relwidth=0.65, anchor="n")
        
        LabelImagenLogin=tk.Label(frameInicioSesion,image=self.images)
        LabelImagenLogin.place(relheight=0.1,relwidth=0.1,anchor="n")
        LabelImagenLogin.grid(padx=0.5, pady=0.5)
        
        labelNombre=tk.Label(frameLogin, bg= "#96c7e6",text="Nombre")
        labelNombre.config(font=letra)
        labelNombre.pack(pady=0.3)
        self.nombreUsuario=tk.StringVar()
        entryNombre=tk.Entry(frameLogin,textvariable=self.nombreUsuario)
        entryNombre.pack(pady=15)
        
        labelDocumento=tk.Label(frameLogin , bg= "#96c7e6",text="Documento")
        labelDocumento.config(font=letra)
        labelDocumento.pack(pady=15)
        self.documentoUsuario=tk.StringVar()
        entryDocumento=tk.Entry(frameLogin,textvariable=self.documentoUsuario)
        entryDocumento.pack(pady=15)
        
        frameRol=tk.Frame(frameLogin)
        frameRol.pack(pady=15)
       
        def habilitar_radio(opcion):
            botonAdmin.config(state="normal" if opcion == 1 else "disabled", font=("Georgia", 10 , "bold"))
            botonVendedor.config(state="normal" if opcion == 2 else "disabled", font=("Georgia", 10 , "bold"))
        
        botonAdmin=tk.Radiobutton(frameRol, text="Administrador",value=1)
        botonAdmin.grid(column=0,row=0, pady=5, padx=7)
        
        
        botonVendedor=tk.Radiobutton(frameRol, text="Vendedor",value=2)
        botonVendedor.grid(column=1, row=0, pady=5, padx=7)
        
        btn_Admi=tk.Button(frameRol, text="habilitar Admi", command=lambda:habilitar_radio(1))
        btn_Ven=tk.Button(frameRol, text="habilitar Admi", command=lambda:habilitar_radio(2))
        
        botonIngresar=tk.Button(frameLogin,text="Iniciar sesion",command=self.funcionIngresar)
        botonIngresar.config(font=letra)
        botonIngresar.pack(pady=15)
        
    def funcionIngresar(self):
        try:
            nombre=self.nombreUsuario.get()
            documento=self.documentoUsuario.get()

            if not nombre.isalpha():
                raise ValueError("El nombre solo debe contener letras")
            
            if not documento.isdigit():
                raise ValueError("El documento solo debe contener números")
            
            if not nombre or not documento:
                raise ValueError("Los campos deben ser llenados correctamente")
            
            self.ventanaLogin.withdraw()
            self.ventanaHome()
            #self.objControlador.inicioSesion(nombre,documento)
        except ValueError as e:
            messagebox.showerror("Error",str(e))
            
    def ventanaHome(self):
        
        ventanaTienda=tk.Toplevel()
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
        
        framePrincipal=tk.Frame(canvas, bg="#719ae2")
        framePrincipal.config(pady=10,padx=10)
        
        canvas.create_window((0,0), window=framePrincipal, anchor="nw")

        def _on_mouse_wheel(event):
            canvas.yview_scroll(-1 * int((event.delta / 120)), "units")

        canvas.bind_all("<MouseWheel>", _on_mouse_wheel)
        self.frameContenido=tk.Frame(framePrincipal)
        self.crearEncabezado(framePrincipal)
        self.crearContenido(self.frameContenido) 
        self.crearPiePagina(framePrincipal)
        
        
    def crearEncabezado(self,framePrincipal):
        letra=("Georgia",7, "bold")
        
        frameEncabezado=tk.Frame(framePrincipal)
        frameEncabezado.config(height=200, bg="white")
        frameEncabezado.pack(padx=10,pady=10, expand=True, fill="both")
        frameSecciones=tk.Frame(frameEncabezado, bg="white")
        frameSecciones.place(relx=0.16,rely=0.05,relheight=0.9,relwidth=0.28,anchor="n")
        home=tk.Button(frameSecciones,bg="#d6022a",  text="Home",font=letra , fg="white")
        home.place(relx=0.125,rely=0.81,relheight=0.2,relwidth=0.25,anchor="n")
        products=tk.Button(frameSecciones,  bg="#d6022a",text="Productos", font=letra , fg="white", command= lambda: self.mostrarProducts(self.frameContenido))
        products.place(relx=0.37,rely=0.81,relheight=0.2,relwidth=0.25,anchor="n")
        about=tk.Button(frameSecciones, bg="#d6022a", text="Informes", font=letra , fg="white", command=lambda: self.mostrarAbout(self.frameContenido))
        about.place(relx=0.62,rely=0.81,relheight=0.2,relwidth=0.25,anchor="n")
        contact=tk.Button(frameSecciones, bg="#d6022a", text="Contacto", font=letra , fg="white")
        contact.place(relx=0.87,rely=0.81,relheight=0.2,relwidth=0.25,anchor="n")
        frameTituloEmpresa=tk.Frame(frameEncabezado)
        frameTituloEmpresa.place(relx=0.52,rely=0.05,relheight=0.9,relwidth=0.4,anchor="n")
        nombre=tk.Label(frameTituloEmpresa,bg="white", text="DROGUERÍA HAYBET" , font=("Georgia",20 , "bold") , fg="#d6022a")
        nombre.config(width=30,height=10)
        nombre.pack(expand=True)
        self.logo=self.interfacePictures("index/CRUD_TIENDA/imagenes/logo_drogueriaHaybet.png",160,150)
        LabelImagenEncabezado=tk.Label(frameEncabezado,image=self.logo)
        LabelImagenEncabezado.config(bg="white")
        LabelImagenEncabezado.place(relx=0.86,rely=0.05,relheight=0.9,relwidth=0.24,anchor="n")
        
    
    def crearContenido(self,frameContenido):
        frameContenido.config(width=800,height=550, bg="#719ae2")
        frameContenido.pack(pady=10,padx=10,expand=True, fill="both")
        frameLateral=tk.Frame(frameContenido, bg="#8bb3e9")
        frameLateral.place(relx=0.11,rely=0.02,relheight=0.96,relwidth=0.2,anchor="n")
        self.reproducir=self.interfacePictures("index/CRUD_TIENDA/imagenes/imagen_reproducir.png",145,140)
        labelLateral=tk.Label(frameLateral, image=self.reproducir, bg="#a5ccf1" )
        labelLateral.pack(padx=5,pady=5)
        frameOptions=tk.Frame(frameLateral, bg="blue")
        frameOptions.place(relx=0.5,rely=0.28,relheight=0.7,relwidth=0.95, anchor="n")
        Apps=tk.Frame(frameOptions, bg="#8bb3e9")
        Apps.pack(expand=True,fill="both")
        lApps=tk.Label(Apps, text="Apps")
        lApps.pack(side="left")
        lApps.config( bg="#8bb3e9", font=("Georgia",8, "bold"), fg="black")
        Games=tk.Frame(frameOptions, bg="#a5ccf1")
        Games.pack(expand=True,fill="both")
        lGames=tk.Label(Games, text="Games")
        lGames.pack(side="left")
        lGames.config( bg="#a5ccf1", font=("Georgia",8, "bold"), fg="black")
        Movies=tk.Frame(frameOptions, bg="#8bb3e9")
        Movies.pack(expand=True,fill="both")
        lMovies=tk.Label(Movies, text="Movies")
        lMovies.pack(side="left")
        lMovies.config( bg="#8bb3e9", font=("Georgia",8, "bold"), fg="black")
        Books=tk.Frame(frameOptions, bg="#a5ccf1")
        Books.pack(expand=True,fill="both")
        lBooks=tk.Label(Books, text="Books")
        lBooks.pack(side="left")
        lBooks.config( bg="#a5ccf1", font=("Georgia",8, "bold"), fg="black")
        Newspapers=tk.Frame(frameOptions, bg="#8bb3e9")
        Newspapers.pack(expand=True,fill="both")
        lNewspapers=tk.Label(Newspapers, text="Newspapers")
        lNewspapers.pack(side="left")
        lNewspapers.config( bg="#8bb3e9", font=("Georgia",8, "bold"), fg="black")
        frameCategorias=tk.Frame(frameContenido, bg="#a5ccf1")
        frameCategorias.place(relx=0.605,rely=0.02,relheight=0.1, relwidth=0.77,anchor="n")
        frameCategorias.config(bg="#a5ccf1")
        botonC1=tk.Button(frameCategorias, text="Medicamentos", font=("Georgia",8, "bold"),bg="white", fg="#719ae2")
        botonC1.place(relx=0.1,rely=0.2,relheight=0.6, relwidth=0.18,anchor="n")
        botonC2=tk.Button(frameCategorias, text="Bebés", font=("Georgia",8, "bold"),bg="white", fg="#719ae2")
        botonC2.place(relx=0.3,rely=0.2,relheight=0.6, relwidth=0.18,anchor="n")
        botonC3=tk.Button(frameCategorias, text="Belleza", font=("Georgia",8, "bold") ,bg="white", fg="#719ae2")
        botonC3.place(relx=0.5,rely=0.2,relheight=0.6, relwidth=0.18,anchor="n")
        botonC4=tk.Button(frameCategorias, text="Bienestar", font=("Georgia",8, "bold"),bg="white", fg="#719ae2")
        botonC4.place(relx=0.7,rely=0.2,relheight=0.6, relwidth=0.18,anchor="n")
        botonC5=tk.Button(frameCategorias, text="Hogar",bg="white",  font=("Georgia",8, "bold"), fg="#719ae2")
        botonC5.place(relx=0.9,rely=0.2,relheight=0.6, relwidth=0.18,anchor="n")
        
    def mostrarProducts(self,frameContenido):
        letra=("Georgia",10, "bold")
        frameProductos=tk.Frame(frameContenido)
        frameProductos.place(relx=0.605,rely=0.13,relheight=0.85, relwidth=0.77,anchor="n")
        frameProductos.config(bg="#719ae2")
        frmTituloCatalogo=tk.Frame(frameProductos)
        frmTituloCatalogo.pack(padx=5,pady=5)
        labelTituloCatalogo=tk.Label(frmTituloCatalogo,text="PRODUCTOS", bg="#719ae2")
        labelTituloCatalogo.pack(expand=True,fill="both")
        labelTituloCatalogo.config(font=letra, fg="white")
        frmContenidoProductos=tk.Frame(frameProductos)
        frmContenidoProductos.pack(expand=True,fill="both")
        frmContenidoProductos.config(bg="#719ae2")
        
        self.image=self.interfacePictures("index/CRUD_TIENDA/imagenes/dolex.jpg",100,50)
        fProduct1=tk.Frame(frmContenidoProductos,height=40,width=40)
        fProduct1.place(relx=0.2,rely=0.05,relheight=0.25, relwidth=0.25,anchor="n")
        fProduct1.config(bg="#719ae2")
        LImagen1=tk.Label(fProduct1,image=self.image) 
        LImagen1.pack(expand=True,fill="both")
        LImagen1.config(bg="#719ae2")
        lp1=tk.Label(fProduct1,text="Medicamentos\nDolex\n $15.000",bg="white")
        lp1.config(bg="#aecef8", font=letra, fg="black")
        lp1.pack(expand=True,fill="both")
        self.image0=self.interfacePictures("index/CRUD_TIENDA/imagenes/bebe.jpg",100,50)
        fProduct2=tk.Frame(frmContenidoProductos, bg="#59baa9",height=20,width=20, )
        fProduct2.place(relx=0.5,rely=0.05,relheight=0.25, relwidth=0.25,anchor="n")
        fProduct2.config(bg="#719ae2")
        LImagen2=tk.Label(fProduct2,image=self.image0)
        LImagen2.pack(expand=True,fill="both")
        LImagen2.config(bg="#719ae2")
        lp2=tk.Label(fProduct2,text="   Cuidado del bebé\nPañales Huggies\n $50.000",bg="#ddffab")
        lp2.pack(expand=True,fill="both")
        lp2.config(bg="#aecef8", font=letra, fg="black")
        self.image2=self.interfacePictures("index/CRUD_TIENDA/imagenes/belleza.jpg",100,50)
        fProduct3=tk.Frame(frmContenidoProductos, bg="#59baa9",height=20,width=20, )
        fProduct3.place(relx=0.8,rely=0.05,relheight=0.25, relwidth=0.25,anchor="n")
        fProduct3.config(bg="#719ae2")
        LImagen3=tk.Label(fProduct3,image=self.image2)
        LImagen3.pack(expand=True,fill="both")
        LImagen3.config(bg="#719ae2")
        lp3=tk.Label(fProduct3,text="Belleza\nEsmalte+polvo\n precio $30.000",bg="#ddffab")
        lp3.pack(expand=True,fill="both")
        lp3.config(bg="#aecef8", font=letra, fg="black")
        self.image1=self.interfacePictures("index/CRUD_TIENDA/imagenes/mieltertos.jpg",100,50)
        fProduct4=tk.Frame(frmContenidoProductos, bg="#59baa9",height=20,width=20, )
        fProduct4.place(relx=0.2,rely=0.35,relheight=0.25, relwidth=0.25,anchor="n")
        fProduct4.config(bg="#719ae2")
        LImagen4=tk.Label(fProduct4,image=self.image1)
        LImagen4.pack(expand=True,fill="both")
        LImagen4.config(bg="#719ae2")
        lp4=tk.Label(fProduct4,text="Medicamentos\nMieltertos 1\\n $1.500",bg="#ddffab")
        lp4.pack(expand=True,fill="both")
        lp4.config(bg="#aecef8", font=letra, fg="black")
        self.image3=self.interfacePictures("index/CRUD_TIENDA/imagenes/benet.png",100,50)
        fProduct5=tk.Frame(frmContenidoProductos, bg="#59baa9",height=20,width=20, )
        fProduct5.place(relx=0.5,rely=0.35,relheight=0.25, relwidth=0.25,anchor="n")
        fProduct5.config(bg="#719ae2")
        LImagen5=tk.Label(fProduct5,image=self.image3)
        LImagen5.pack(expand=True,fill="both")
        LImagen5.config(bg="#719ae2")
        lp5=tk.Label(fProduct5,text="Bienestar\nBenet\n $80.000",bg="#ddffab")
        lp5.pack(expand=True,fill="both")
        lp5.config(bg="#aecef8", font=letra, fg="black")
        self.image4=self.interfacePictures("index/CRUD_TIENDA/imagenes/bebe2.png",100,50)
        fProduct6=tk.Frame(frmContenidoProductos, bg="#59baa9",height=20,width=20, )
        fProduct6.place(relx=0.8,rely=0.35,relheight=0.25, relwidth=0.25,anchor="n")
        fProduct6.config(bg="#719ae2")
        LImagen6=tk.Label(fProduct6,image=self.image4)
        LImagen6.pack(expand=True,fill="both")
        LImagen6.config(bg="#719ae2")
        lp6=tk.Label(fProduct6,text="Cuidado del bebé\nCrema N°4\n $10.000",bg="#ddffab")
        lp6.pack(expand=True,fill="both")
        lp6.config(bg="#aecef8", font=letra, fg="black")
        self.image5=self.interfacePictures("index/CRUD_TIENDA/imagenes/hogar.png",100,50)
        fProduct7=tk.Frame(frmContenidoProductos, bg="#59baa9",height=20,width=20, )
        fProduct7.place(relx=0.2,rely=0.65,relheight=0.25, relwidth=0.25,anchor="n")
        fProduct7.config(bg="#719ae2")
        LImagen7=tk.Label(fProduct7,image=self.image5)
        LImagen7.pack(expand=True,fill="both")
        LImagen7.config(bg="#719ae2")
        lp7=tk.Label(fProduct7,text="Hogar\nPapel Familia x12\n $15.000",bg="#ddffab")
        lp7.pack(expand=True,fill="both")
        lp7.config(bg="#aecef8", font=letra, fg="black")
        self.image6=self.interfacePictures("index/CRUD_TIENDA/imagenes/mieltertos2.jpg",100,50)
        fProduct8=tk.Frame(frmContenidoProductos, bg="#59baa9",height=20,width=20, )
        fProduct8.place(relx=0.5,rely=0.65,relheight=0.25, relwidth=0.25,anchor="n")
        fProduct8.config(bg="#719ae2")
        LImagen8=tk.Label(fProduct8,image=self.image6)
        LImagen8.pack(expand=True,fill="both")
        LImagen8.config(bg="#719ae2")
        lp8=tk.Label(fProduct8,text="Medicametos \nMieltertos ped\n $15.000",bg="#ddffab")
        lp8.pack(expand=True,fill="both")
        lp8.config(bg="#aecef8", font=letra, fg="black")
        self.image7=self.interfacePictures("index/CRUD_TIENDA/imagenes/bebe1.jpg",100,50)
        fProduct9=tk.Frame(frmContenidoProductos, bg="#59baa9",height=20,width=20, )
        fProduct9.place(relx=0.8,rely=0.65,relheight=0.25, relwidth=0.25,anchor="n")
        fProduct9.config(bg="#719ae2")
        LImagen9=tk.Label(fProduct9,image=self.image7)
        LImagen9.pack(expand=True,fill="both")
        LImagen9.config(bg="#719ae2")
        lp9=tk.Label(fProduct9,text="Cuidado del bebé\nLeche klim\n $80.000",bg="#ddffab")
        lp9.pack(expand=True,fill="both")
        lp9.config(bg="#aecef8", font=letra, fg="black")
            
    def mostrarAbout(self,frameContenido):
        letra=("Georgia",10, "bold")
        frameEstadisticas=tk.Frame(frameContenido)
        frameEstadisticas.place(relx=0.605,rely=0.13,relheight=0.85, relwidth=0.77,anchor="n")
        frameEstadisticas.config(bg="#8bb3e9")
        
        frmTituloInforme=tk.Frame(frameEstadisticas)
        frmTituloInforme.place(relx=0.5,rely=0.02,relheight=0.11,relwidth=0.95,anchor="n")
        labelTituloInforme=tk.Label(frmTituloInforme,text="Informe de productos")
        labelTituloInforme.pack(expand=True,fill="both")
        labelTituloInforme.config(bg="#8bb3e9", font= ("Georgia",15, "bold"), fg="black")
        
        
        frmMasVendidos=tk.Frame(frameEstadisticas, bg="#8bb3e9")
        frmMasVendidos.place(relx=0.265,rely=0.15,relheight=0.74,relwidth=0.46,anchor="n")
        frmTituloMas=tk.Frame(frmMasVendidos, bg="black")
        frmTituloMas.place(relx=0.5,rely=0.03,relheight=0.15,relwidth=0.7,anchor="n")
        labelTituloMas=tk.Label(frmTituloMas, text="Mas Vendidos")
        labelTituloMas.pack(expand=True,fill="both")
        labelTituloMas.config(bg="#8bb3e9", font=("Georgia",12, "bold"), fg="#d6022a")
        fNombreProductoMas=tk.Frame(frmMasVendidos)
        fNombreProductoMas.place(relx=0.27,rely=0.22,relheight=0.1,relwidth=0.45,anchor="n")
        lNombreProductoMas=tk.Label(fNombreProductoMas,text="Nombre Producto")
        lNombreProductoMas.pack(expand=True,fill="both")
        lNombreProductoMas.config(bg="#a5ccf1", font=("Georgia",8, "bold"), fg="#d6022a")
        fCantidadMas=tk.Frame(frmMasVendidos)
        fCantidadMas.place(relx=0.73,rely=0.22,relheight=0.1,relwidth=0.45,anchor="n")
        lCantidadMas=tk.Label(fCantidadMas,text="Cantidad")
        lCantidadMas.pack(expand=True, fill="both")
        lCantidadMas.config(bg="#a5ccf1", font=("Georgia",8, "bold"), fg="#d6022a")
        f1=tk.Frame(frmMasVendidos)
        f1.place(relx=0.27,rely=0.36,relheight=0.15,relwidth=0.45,anchor="n")
        f1.config(bg="#a5ccf1")
        f2=tk.Frame(frmMasVendidos)
        f2.place(relx=0.27,rely=0.52,relheight=0.15,relwidth=0.45,anchor="n")
        f2.config(bg="#a5ccf1")
        f3=tk.Frame(frmMasVendidos)
        f3.place(relx=0.27,rely=0.68,relheight=0.15,relwidth=0.45,anchor="n")
        f3.config(bg="#a5ccf1")
        f4=tk.Frame(frmMasVendidos)
        f4.place(relx=0.27,rely=0.84,relheight=0.15,relwidth=0.45,anchor="n")
        f4.config(bg="#a5ccf1")
        f5=tk.Frame(frmMasVendidos)
        f5.place(relx=0.73,rely=0.36,relheight=0.15,relwidth=0.45,anchor="n")
        f5.config(bg="#a5ccf1")
        f6=tk.Frame(frmMasVendidos)
        f6.place(relx=0.73,rely=0.52,relheight=0.15,relwidth=0.45,anchor="n")
        f6.config(bg="#a5ccf1")
        f7=tk.Frame(frmMasVendidos)
        f7.place(relx=0.73,rely=0.68,relheight=0.15,relwidth=0.45,anchor="n")
        f7.config(bg="#a5ccf1")
        f8=tk.Frame(frmMasVendidos)
        f8.place(relx=0.73,rely=0.84,relheight=0.15,relwidth=0.45,anchor="n")
        f8.config(bg="#a5ccf1")
        
        frmMenosVendidos=tk.Frame(frameEstadisticas , bg="#8bb3e9")
        frmMenosVendidos.place(relx=0.74,rely=0.15,relheight=0.74,relwidth=0.46,anchor="n")
        frmTituloMenos=tk.Frame(frmMenosVendidos)
        frmTituloMenos.place(relx=0.5,rely=0.03,relheight=0.15,relwidth=0.7,anchor="n")
        labelTituloMenos=tk.Label(frmTituloMenos, text="Menos Vendidos")
        labelTituloMenos.pack(expand=True,fill="both")
        labelTituloMenos.config(bg="#8bb3e9", font=("Georgia",12, "bold"), fg="#d6022a")
        fNombreProductoMenos=tk.Frame(frmMenosVendidos)
        fNombreProductoMenos.place(relx=0.27,rely=0.22,relheight=0.1,relwidth=0.45,anchor="n")
        lNombreProductoMenos=tk.Label(fNombreProductoMenos,text="Nombre Producto")
        lNombreProductoMenos.pack(expand=True, fill="both")
        lNombreProductoMenos.config(bg="#a5ccf1", font=("Georgia",8, "bold"),fg="#d6022a")
        fCantidadMenos=tk.Frame(frmMenosVendidos)
        fCantidadMenos.place(relx=0.73,rely=0.22,relheight=0.1,relwidth=0.45,anchor="n")
        lCantidadMenos=tk.Label(fCantidadMenos,text="Cantidad")
        lCantidadMenos.pack(expand=True, fill="both")
        lCantidadMenos.config(bg="#a5ccf1", font=("Georgia",8, "bold"), fg="#d6022a")
        f9=tk.Frame(frmMenosVendidos)
        f9.place(relx=0.27,rely=0.36,relheight=0.15,relwidth=0.45,anchor="n")
        f10=tk.Frame(frmMenosVendidos)
        f10.place(relx=0.27,rely=0.52,relheight=0.15,relwidth=0.45,anchor="n")
        f11=tk.Frame(frmMenosVendidos)
        f11.place(relx=0.27,rely=0.68,relheight=0.15,relwidth=0.45,anchor="n")
        f12=tk.Frame(frmMenosVendidos)
        f12.place(relx=0.27,rely=0.84,relheight=0.15,relwidth=0.45,anchor="n")
        f13=tk.Frame(frmMenosVendidos)
        f13.place(relx=0.73,rely=0.36,relheight=0.15,relwidth=0.45,anchor="n")
        f14=tk.Frame(frmMenosVendidos)
        f14.place(relx=0.73,rely=0.52,relheight=0.15,relwidth=0.45,anchor="n")
        f15=tk.Frame(frmMenosVendidos)
        f15.place(relx=0.73,rely=0.68,relheight=0.15,relwidth=0.45,anchor="n")
        f16=tk.Frame(frmMenosVendidos)
        f16.place(relx=0.73,rely=0.84,relheight=0.15,relwidth=0.45,anchor="n")
        f9.config(bg="#a5ccf1")
        f10.config(bg="#a5ccf1")
        f11.config(bg="#a5ccf1")
        f12.config(bg="#a5ccf1")
        f13.config(bg="#a5ccf1")
        f14.config(bg="#a5ccf1")
        f15.config(bg="#a5ccf1")
        f16.config(bg="#a5ccf1")
        
        botonGenerar=tk.Button(frameEstadisticas,text="Generar informe", command=None) #al pulsar debe generar un informe de tipo texto con ayuda del JSON
        botonGenerar.place(relx=0.83,rely=0.92,relheight=0.06,relwidth=0.17,anchor="n")
        botonGenerar.config( bg="#d6022a", font=("Georgia",7, "bold"), fg="white")
        
    def crearPiePagina(self,framePrincipal):
        framePiePagina=tk.Frame(framePrincipal, bg="#8bb3e9")
        framePiePagina.config(width=800,height=100)
        framePiePagina.pack(pady=10)
        self.pastilla=self.interfacePictures("index/CRUD_TIENDA/imagenes/imagen_doctor.png",305,80)
        labelLeft=tk.Label(framePiePagina, image=self.pastilla)
        labelLeft.place(relx=0.25,rely=0.05,relheight=0.9, relwidth=0.45,anchor="n")
        labelLeft.config(bg="#8bb3e9")
        frameRight=tk.Frame(framePiePagina, bg="#8bb3e9")
        frameRight.place(relx=0.75,rely=0.05,relheight=0.9, relwidth=0.45,anchor="n")
        pieHome=tk.Button(frameRight, text="Home")
        pieHome.place(relx=0.1,rely=0.25,relheight=0.5, relwidth=0.2,anchor="n")
        pieHome.config( bg="#d6022a", font=("Georgia",7, "bold"), fg="white")
        pieApps=tk.Button(frameRight, text="Apps")
        pieApps.place(relx=0.3,rely=0.25,relheight=0.5, relwidth=0.2,anchor="n")
        pieApps.config( bg="#d6022a", font=("Georgia",7, "bold"), fg="white")
        pieGames=tk.Button(frameRight, text="Games")
        pieGames.place(relx=0.5,rely=0.25,relheight=0.5, relwidth=0.2,anchor="n")
        pieGames.config( bg="#d6022a", font=("Georgia",7, "bold"), fg="white")
        pieMovies=tk.Button(frameRight, text="Movies")
        pieMovies.place(relx=0.7,rely=0.25,relheight=0.5, relwidth=0.2,anchor="n")
        pieMovies.config( bg="#d6022a", font=("Georgia",7, "bold"), fg="white")
        pieBooks=tk.Button(frameRight, text="Books")
        pieBooks.place(relx=0.9,rely=0.25,relheight=0.5, relwidth=0.2,anchor="n")
        pieBooks.config( bg="#d6022a", font=("Georgia",7, "bold"), fg="white")
        
    def interfacePictures(self,pic,ancho,altura):
        image= Image.open(pic).resize((ancho,altura))
        img=ImageTk.PhotoImage(image)
        return img
        
    def activar_mainloop(self):
        tk.mainloop()
        

Ventana=Interfaz()
Ventana.ventanaIngreso()
Ventana.activar_mainloop()