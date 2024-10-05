
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image

class Interfaz:
    def __init__(self,objControlador):
        self.objControlador=objControlador
        self.ventanaLogin=None
        self.nombreUsuario=None
        self.documentoUsuario=None
        self.ventana_crear=None
        self.ventana_eliminar=None
        self.ventana_modificar=None
        self.cargoUsuario=None
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
        self.contactoDrogueria=None
        self.letra=None

    def ventana_ingreso(self):
        self.ventanaLogin=tk.Tk()
        self.ventanaLogin.geometry("600x800")
        self.ventanaLogin.maxsize(600,800)
        self.ventanaLogin.title("INICIO SESION HAYBET SALUD")
        self.letra=("Georgia", 20, "bold")
        self.images = self.interface_pictures(r"index\VISTA\imagenes\pastillas.jpg", 250, 190)

        frameInicioSesion=tk.Frame(self.ventanaLogin)
        frameInicioSesion.config(bg="#96c7e6",width=400,height=500)
        frameInicioSesion.pack(expand=True,fill="both")
        
        frameTitulo=tk.Frame(frameInicioSesion)
        frameTitulo.place(relx=0.7,rely=0,relheight=0.242, relwidth=0.69, anchor="n")
        labelTitulo=tk.Label(frameTitulo,bg= "white", text="INICIO DE SESION")
        labelTitulo.config(font=self.letra, fg="#d6022a")
        labelTitulo.pack(expand=True,fill="both")
        
        frameLogin=tk.Frame(frameInicioSesion, bg="#96c7e6")
        frameLogin.place(relx=0.5,rely=0.25,relheight=0.7, relwidth=0.65, anchor="n")
        
        LabelImagenLogin=tk.Label(frameInicioSesion,image=self.images)
        LabelImagenLogin.place(relheight=0.1,relwidth=0.1,anchor="n")
        LabelImagenLogin.grid(padx=0.5, pady=0.5)
        
        labelNombre=tk.Label(frameLogin, bg= "#96c7e6",text="Nombre")
        labelNombre.config(font=self.letra)
        labelNombre.pack(pady=0.3)
        self.nombreUsuario=tk.StringVar()
        entryNombre=tk.Entry(frameLogin,textvariable=self.nombreUsuario)
        entryNombre.pack(pady=15)
        
        labelDocumento=tk.Label(frameLogin , bg= "#96c7e6",text="Documento")
        labelDocumento.config(font=self.letra)
        labelDocumento.pack(pady=15)
        self.documentoUsuario=tk.StringVar()
        entryDocumento=tk.Entry(frameLogin,textvariable=self.documentoUsuario)
        entryDocumento.pack(pady=15)
        
        frameRol=tk.Frame(frameLogin)
        frameRol.pack(pady=15)
       
        self.cargoUsuario=tk.StringVar()
        
        botonAdmin=tk.Radiobutton(frameRol,variable=self.cargoUsuario, text="Administrador",value="Administrador")
        botonAdmin.grid(column=0,row=0, pady=5, padx=7)
        
        botonVendedor=tk.Radiobutton(frameRol,variable=self.cargoUsuario, text="Vendedor",value="Vendedor")
        botonVendedor.grid(column=1, row=0, pady=5, padx=7)
        
        botonIngresar=tk.Button(frameLogin,text="Iniciar sesion",command=self.funcion_ingresar, bg="#d6022a")
        botonIngresar.config(font=self.letra, fg="white")
        botonIngresar.pack(pady=15)
        
    def funcion_ingresar(self):
        try:
            nombre=self.nombreUsuario.get()
            documento=self.documentoUsuario.get()
            cargo=self.cargoUsuario.get()

            if not all(char.isalpha() or char.isspace() for char in nombre):
                raise ValueError("El nombre solo debe contener letras y espacios")
            
            if not documento.isdigit():
                raise ValueError("El documento solo debe contener números")
            
            if not nombre or not documento:
                raise ValueError("Los campos deben ser llenados correctamente")
            
            if not cargo:
                raise ValueError("Por favor, seleccione un rol")
            
            x=1
            listaUsuario=[documento,nombre,x,cargo]
            
            if self.objControlador.validar_inicio_sesion(listaUsuario):
                self.ventanaLogin.withdraw()
                if cargo == "Administrador":
                    self.ventana_home_admin()
                elif cargo == "Vendedor":
                    self.ventana_home_vendedor()
            else:
                messagebox.showerror("Error", "Usuario,contraseña o cargo incorrecto")
        except ValueError as e:
            messagebox.showerror("Error",str(e))
            
            
    def ventana_home_admin(self):
        
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
        self.crear_encabezado(framePrincipal)
        self.crear_contenido(self.frameContenido) 
        self.crear_pie_pagina(framePrincipal)
        
    def ventana_home_vendedor(self):
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
        self.crear_encabezado_vendedor(framePrincipal)    
        self.crear_contenido()
        self.crear_pie_pagina()
        
    def crear_encabezado(self,framePrincipal):
        self.letra=("Georgia",7, "bold")
        frameEncabezado=tk.Frame(framePrincipal)
        frameEncabezado.config(height=200, bg="white")
        frameEncabezado.pack(padx=10,pady=10, expand=True, fill="both")
        frameSecciones=tk.Frame(frameEncabezado, bg="white")
        frameSecciones.place(relx=0.16,rely=0.05,relheight=0.9,relwidth=0.28,anchor="n")
        home=tk.Button(frameSecciones,bg="#d6022a",  text="Home",font=self.letra , fg="white", command= lambda: self.ventana_home_admin(self.frameContenido))
        home.place(relx=0.125,rely=0.81,relheight=0.2,relwidth=0.25,anchor="n")
        products=tk.Button(frameSecciones,  bg="#d6022a",text="Productos", font=self.letra , fg="white", command= lambda: self.mostrar_productos(self.frameContenido))
        products.place(relx=0.37,rely=0.81,relheight=0.2,relwidth=0.25,anchor="n")
        about=tk.Button(frameSecciones, bg="#d6022a", text="Informes", font=self.letra , fg="white", command=lambda: self.mostrar_informes(self.frameContenido))
        about.place(relx=0.62,rely=0.81,relheight=0.2,relwidth=0.25,anchor="n")
        contact=tk.Button(frameSecciones, bg="#d6022a", text="Contacto", font=self.letra , fg="white", command=lambda: self.mostrar_contacto(self.frameContenido))
        contact.place(relx=0.87,rely=0.81,relheight=0.2,relwidth=0.25,anchor="n")
        frameTituloEmpresa=tk.Frame(frameEncabezado)
        frameTituloEmpresa.place(relx=0.52,rely=0.05,relheight=0.9,relwidth=0.4,anchor="n")
        nombre=tk.Label(frameTituloEmpresa,bg="white", text="DROGUERÍA HAYBET" , font=("Georgia",20 , "bold") , fg="#d6022a")
        nombre.config(width=30,height=10)
        nombre.pack(expand=True)
        self.logo=self.interface_pictures("index/VISTA/imagenes/logo_drogueriaHaybet.png",160,150)
        LabelImagenEncabezado=tk.Label(frameEncabezado,image=self.logo)
        LabelImagenEncabezado.config(bg="white")
        LabelImagenEncabezado.place(relx=0.86,rely=0.05,relheight=0.9,relwidth=0.24,anchor="n")
    
    def crear_encabezado_vendedor(self,framePrincipal):
        self.letra=("Georgia",7, "bold")
        frameEncabezado=tk.Frame(framePrincipal)
        frameEncabezado.config(height=200, bg="white")
        frameEncabezado.pack(padx=10,pady=10, expand=True, fill="both")
        frameSecciones=tk.Frame(frameEncabezado, bg="white")
        frameSecciones.place(relx=0.16,rely=0.05,relheight=0.9,relwidth=0.28,anchor="n")
        home=tk.Button(frameSecciones,bg="#d6022a",  text="Home",font=self.letra , fg="white", command=lambda: self.ventana_home_vendedor(self.frameContenido))
        home.place(relx=0.125,rely=0.81,relheight=0.2,relwidth=0.25,anchor="n")
        products=tk.Button(frameSecciones,  bg="#d6022a",text="Productos", font=self.letra , fg="white", command= lambda: self.mostrarProductos(self.frameContenido))
        products.place(relx=0.37,rely=0.81,relheight=0.2,relwidth=0.25,anchor="n")
        contact=tk.Button(frameSecciones, bg="#d6022a", text="Contacto", font=self.letra , fg="white", command=lambda: self.mostrarContacto(self.frameContenido))
        contact.place(relx=0.87,rely=0.81,relheight=0.2,relwidth=0.25,anchor="n")
        frameTituloEmpresa=tk.Frame(frameEncabezado)
        frameTituloEmpresa.place(relx=0.52,rely=0.05,relheight=0.9,relwidth=0.4,anchor="n")
        nombre=tk.Label(frameTituloEmpresa,bg="white", text="DROGUERÍA HAYBET" , font=("Georgia",20 , "bold") , fg="#d6022a")
        nombre.config(width=30,height=10)
        nombre.pack(expand=True)
        self.logo=self.interface_pictures("index/VISTA/imagenes/logo_drogueriaHaybet.png",160,150)
        LabelImagenEncabezado=tk.Label(frameEncabezado,image=self.logo)
        LabelImagenEncabezado.config(bg="white")
        LabelImagenEncabezado.place(relx=0.86,rely=0.05,relheight=0.9,relwidth=0.24,anchor="n")
    
    def crear_contenido(self,frameContenido):
        frameContenido.config(width=800,height=550, bg="#719ae2")
        frameContenido.pack(pady=10,padx=10,expand=True, fill="both")
        frameLateral=tk.Frame(frameContenido, bg="#8bb3e9")
        frameLateral.place(relx=0.11,rely=0.02,relheight=0.96,relwidth=0.2,anchor="n")
        self.reproducir=self.interface_pictures("index/VISTA/imagenes/imagen_reproducir.png",145,140)
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
        
    def mostrar_productos(self,frameContenido):
        self.letra=("Georgia",10, "bold")
        frameProductos=tk.Frame(frameContenido)
        frameProductos.place(relx=0.605,rely=0.13,relheight=0.85, relwidth=0.77,anchor="n")
        frameProductos.config(bg="#719ae2")
        frmTituloCatalogo=tk.Frame(frameProductos)
        frmTituloCatalogo.pack(padx=5,pady=5)
        labelTituloCatalogo=tk.Label(frmTituloCatalogo,text="PRODUCTOS", bg="#719ae2")
        labelTituloCatalogo.pack(expand=True,fill="both")
        labelTituloCatalogo.config(font=self.letra, fg="white")
        frmContenidoProductos=tk.Frame(frameProductos)
        frmContenidoProductos.pack(expand=True,fill="both")
        frmContenidoProductos.config(bg="#719ae2")
        
        self.image=self.interface_pictures("index/VISTA/imagenes/dolex.jpg",100,50)
        fProduct1=tk.Frame(frmContenidoProductos,height=40,width=40)
        fProduct1.place(relx=0.2,rely=0.05,relheight=0.25, relwidth=0.25,anchor="n")
        fProduct1.config(bg="#719ae2")
        LImagen1=tk.Label(fProduct1,image=self.image) 
        LImagen1.pack(expand=True,fill="both")
        LImagen1.config(bg="#719ae2")
        lp1=tk.Label(fProduct1,text="Medicamentos\nDolex\n $15.000",bg="white")
        lp1.config(bg="#aecef8", font=self.letra, fg="black")
        lp1.pack(expand=True,fill="both")
        self.image0=self.interface_pictures("index/VISTA/imagenes/bebe.jpg",100,50)
        fProduct2=tk.Frame(frmContenidoProductos, bg="#59baa9",height=20,width=20, )
        fProduct2.place(relx=0.5,rely=0.05,relheight=0.25, relwidth=0.25,anchor="n")
        fProduct2.config(bg="#719ae2")
        LImagen2=tk.Label(fProduct2,image=self.image0)
        LImagen2.pack(expand=True,fill="both")
        LImagen2.config(bg="#719ae2")
        lp2=tk.Label(fProduct2,text="   Cuidado del bebé\nPañales Huggies\n $50.000",bg="#ddffab")
        lp2.pack(expand=True,fill="both")
        lp2.config(bg="#aecef8", font=self.letra, fg="black")
        self.image2=self.interface_pictures("index/VISTA/imagenes/belleza.jpg",100,50)
        fProduct3=tk.Frame(frmContenidoProductos, bg="#59baa9",height=20,width=20, )
        fProduct3.place(relx=0.8,rely=0.05,relheight=0.25, relwidth=0.25,anchor="n")
        fProduct3.config(bg="#719ae2")
        LImagen3=tk.Label(fProduct3,image=self.image2)
        LImagen3.pack(expand=True,fill="both")
        LImagen3.config(bg="#719ae2")
        lp3=tk.Label(fProduct3,text="Belleza\nEsmalte+polvo\n precio $30.000",bg="#ddffab")
        lp3.pack(expand=True,fill="both")
        lp3.config(bg="#aecef8", font=self.letra, fg="black")
        self.image1=self.interface_pictures("index/VISTA/imagenes/mieltertos.jpg",100,50)
        fProduct4=tk.Frame(frmContenidoProductos, bg="#59baa9",height=20,width=20, )
        fProduct4.place(relx=0.2,rely=0.35,relheight=0.25, relwidth=0.25,anchor="n")
        fProduct4.config(bg="#719ae2")
        LImagen4=tk.Label(fProduct4,image=self.image1)
        LImagen4.pack(expand=True,fill="both")
        LImagen4.config(bg="#719ae2")
        lp4=tk.Label(fProduct4,text="Medicamentos\nMieltertos 1\\n $1.500",bg="#ddffab")
        lp4.pack(expand=True,fill="both")
        lp4.config(bg="#aecef8", font=self.letra, fg="black")
        self.image3=self.interface_pictures("index/VISTA/imagenes/benet.png",100,50)
        fProduct5=tk.Frame(frmContenidoProductos, bg="#59baa9",height=20,width=20, )
        fProduct5.place(relx=0.5,rely=0.35,relheight=0.25, relwidth=0.25,anchor="n")
        fProduct5.config(bg="#719ae2")
        LImagen5=tk.Label(fProduct5,image=self.image3)
        LImagen5.pack(expand=True,fill="both")
        LImagen5.config(bg="#719ae2")
        lp5=tk.Label(fProduct5,text="Bienestar\nBenet\n $80.000",bg="#ddffab")
        lp5.pack(expand=True,fill="both")
        lp5.config(bg="#aecef8", font=self.letra, fg="black")
        self.image4=self.interface_pictures("index/VISTA/imagenes/bebe2.png",100,50)
        fProduct6=tk.Frame(frmContenidoProductos, bg="#59baa9",height=20,width=20, )
        fProduct6.place(relx=0.8,rely=0.35,relheight=0.25, relwidth=0.25,anchor="n")
        fProduct6.config(bg="#719ae2")
        LImagen6=tk.Label(fProduct6,image=self.image4)
        LImagen6.pack(expand=True,fill="both")
        LImagen6.config(bg="#719ae2")
        lp6=tk.Label(fProduct6,text="Cuidado del bebé\nCrema N°4\n $10.000",bg="#ddffab")
        lp6.pack(expand=True,fill="both")
        lp6.config(bg="#aecef8", font=self.letra, fg="black")
        self.image5=self.interface_pictures("index/VISTA/imagenes/hogar.png",100,50)
        fProduct7=tk.Frame(frmContenidoProductos, bg="#59baa9",height=20,width=20, )
        fProduct7.place(relx=0.2,rely=0.65,relheight=0.25, relwidth=0.25,anchor="n")
        fProduct7.config(bg="#719ae2")
        LImagen7=tk.Label(fProduct7,image=self.image5)
        LImagen7.pack(expand=True,fill="both")
        LImagen7.config(bg="#719ae2")
        lp7=tk.Label(fProduct7,text="Hogar\nPapel Familia x12\n $15.000",bg="#ddffab")
        lp7.pack(expand=True,fill="both")
        lp7.config(bg="#aecef8", font=self.letra, fg="black")
        self.image6=self.interface_pictures("index/VISTA/imagenes/mieltertos2.jpg",100,50)
        fProduct8=tk.Frame(frmContenidoProductos, bg="#59baa9",height=20,width=20, )
        fProduct8.place(relx=0.5,rely=0.65,relheight=0.25, relwidth=0.25,anchor="n")
        fProduct8.config(bg="#719ae2")
        LImagen8=tk.Label(fProduct8,image=self.image6)
        LImagen8.pack(expand=True,fill="both")
        LImagen8.config(bg="#719ae2")
        lp8=tk.Label(fProduct8,text="Medicametos \nMieltertos ped\n $15.000",bg="#ddffab")
        lp8.pack(expand=True,fill="both")
        lp8.config(bg="#aecef8", font=self.letra, fg="black")
        self.image7=self.interface_pictures("index/VISTA/imagenes/bebe1.jpg",100,50)
        fProduct9=tk.Frame(frmContenidoProductos, bg="#59baa9",height=20,width=20, )
        fProduct9.place(relx=0.8,rely=0.65,relheight=0.25, relwidth=0.25,anchor="n")
        fProduct9.config(bg="#719ae2")
        LImagen9=tk.Label(fProduct9,image=self.image7)
        LImagen9.pack(expand=True,fill="both")
        LImagen9.config(bg="#719ae2")
        lp9=tk.Label(fProduct9,text="Cuidado del bebé\nLeche klim\n $80.000",bg="#ddffab")
        lp9.pack(expand=True,fill="both")
        lp9.config(bg="#aecef8", font=self.letra, fg="black")
        
        botonAdd=tk.Button(frmContenidoProductos,text="Agregar Producto", command=lambda:self.crear_producto( )) 
        botonAdd.place(relx=0.5,rely=0.92,relheight=0.06,relwidth=0.17,anchor="n")
        botonAdd.config( bg="#d6022a", font=("Georgia",7, "bold"), fg="white")
        
        botonActualizar=tk.Button(frmContenidoProductos,text="Actualizar producto", command=lambda: self.modificar_producto()) 
        botonActualizar.place(relx=0.67,rely=0.92,relheight=0.06,relwidth=0.17,anchor="n")
        botonActualizar.config( bg="#d6022a", font=("Georgia",7, "bold"), fg="white")
        
        botonDelete=tk.Button(frmContenidoProductos,text="Eliminar Producto", command=lambda: self.eliminar_producto()) 
        botonDelete.place(relx=0.84,rely=0.92,relheight=0.06,relwidth=0.17,anchor="n")
        botonDelete.config( bg="#d6022a", font=("Georgia",7, "bold"), fg="white")
    
    def crear_producto(self):
        self.letra = ("Georgia", 20, "bold")
        self.ventana_crear = tk.Tk()  # Corrección aquí
        self.ventana_crear.title("CREAR PRODUCTOS")
        self.ventana_crear.geometry('600x800')
        self.ventana_crear.maxsize(600,800)# Corrección aquí
          
        frameAgregar=tk.Frame(self.ventana_crear)
        frameAgregar.config(bg="#96c7e6",width=400,height=500)
        frameAgregar.pack(expand=True,fill="both")
        
        frameTitulo=tk.Frame(frameAgregar)
        frameTitulo.place(relx=0.5,rely=0,relheight=0.242, relwidth=50, anchor="n")
        labelTitulo=tk.Label(frameTitulo,bg= "white", text="AGREGAR PRODUCTO")
        labelTitulo.config(font=self.letra, fg="#d6022a")
        labelTitulo.pack(expand=True,fill="both")
        
        frameAdd=tk.Frame(frameAgregar, bg="#96c7e6")
        frameAdd.place(relx=0.5,rely=0.25,relheight=0.7, relwidth=0.65, anchor="n")
        
        
        label_id=tk.Label(frameAdd, bg= "#96c7e6",text="ID del producto")
        label_id.config(font=self.letra)
        label_id.pack(pady=0.3)
        self.id=tk.StringVar()
        entry_id=tk.Entry(frameAdd,textvariable=self.id)
        entry_id.pack(pady=15)
        
        labelNombre=tk.Label(frameAdd, bg= "#96c7e6",text="Nombre del producto")
        labelNombre.config(font=self.letra)
        labelNombre.pack(pady=0.3)
        self.nombre_med=tk.StringVar()
        entryNombre=tk.Entry(frameAdd,textvariable=self.nombre_med)
        entryNombre.pack(pady=15)
        
        label_cantidad=tk.Label(frameAdd , bg= "#96c7e6",text="Cantidad")
        label_cantidad.config(font=self.letra)
        label_cantidad.pack(pady=15)
        self.cantidad=tk.StringVar()
        entry_cantidad=tk.Entry(frameAdd,textvariable=self.cantidad)
        entry_cantidad.pack(pady=15)
        
        label_categoria=tk.Label(frameAdd , bg= "#96c7e6",text="Categoria")
        label_categoria.config(font=self.letra)
        label_categoria.pack(pady=15)
        self.categoria=tk.StringVar()
        entry_cat=tk.Entry(frameAdd,textvariable=self.categoria)
        entry_cat.pack(pady=15)
        
        label_descripcion=tk.Label(frameAdd , bg= "#96c7e6",text="Descripcion")
        label_descripcion.config(font=self.letra)
        label_descripcion.pack(pady=15)
        self.descripcion=tk.StringVar()
        entry_des=tk.Entry(frameAdd,textvariable=self.descripcion)
        entry_des.pack(pady=15)
        # Asegúrate de empaquetar el Treeview

        # Botón para registrar el producto
        boton_crear = tk.Button(self.ventana_crear, text="REGISTRAR PRODUCTO",
                                command=lambda: self.crear_producto("codigo, nombre, precio"),  # Pasar parámetros correctamente
                                bg="#d6022a")
        boton_crear.config(font=self.letra, fg="white")
        boton_crear.pack(pady=15)
    
    def eliminar_producto(self):
        self.letra = ("Georgia", 12, "bold")
        self.ventana_eliminar = tk.Tk()  # Corrección aquí
        self.ventana_eliminar.title("ELIMINAR PRODUCTOS")
        self.ventana_eliminar.geometry('500x600')

        frame_eliminar=tk.Frame(self.ventana_eliminar)
        frame_eliminar.config(bg="#96c7e6",width=400,height=600)
        frame_eliminar.pack(expand=True,fill="both")
        
        eliminar = ttk.Treeview(frame_eliminar, columns=("codigo", "producto", "precio"), show='headings')
        eliminar.heading("codigo", text="CODIGO")
        eliminar.heading("producto", text="Nombre Producto")
        eliminar.heading("precio", text="Precio Producto")
        eliminar.column("codigo", width=100)
        eliminar.column("producto", width=100)
        eliminar.column("precio", width=100)
        eliminar.pack() # Asegúrate de empaquetar el Treeview
        

        # Botón para eliminar el producto
        boton_eliminar = tk.Button(self.ventana_eliminar, text="Eliminar Producto",
                                   command=lambda: self.eliminar_producto("codigo, nombre, precio"),  # Corrección aquí
                                   bg="#d6022a")
        boton_eliminar.config(font=self.letra, fg="white")
        boton_eliminar.pack(pady=15)

    def modificar_producto(self):
        self.letra = ("Georgia", 12, "bold")
        self.ventana_modificar = tk.Tk()
        self.ventana_modificar.title("MODIFICAR PRODUCTOS")
        self.ventana_modificar.geometry('800x600')

        self.crear_titulo()
        self.crear_treeview()
        self.crear_formulario()

    def crear_titulo(self):
        frameTitulo = tk.Frame(self.ventana_modificar)
        frameTitulo.place(relx=0.5, rely=0, relheight=0.1, relwidth=1, anchor="n")
        labelTitulo = tk.Label(frameTitulo, bg="white", text="MODIFICAR PRODUCTO")
        labelTitulo.config(font=self.letra, fg="#d6022a")
        labelTitulo.pack(expand=True, fill="both")

    def crear_treeview(self):
        frame_treeview = tk.Frame(self.ventana_modificar, bg="white")
        frame_treeview.place(relx=0.05, rely=0.15, relheight=0.55, relwidth=0.9, anchor="nw")

        # Definir el Treeview
        self.tabla_productos = ttk.Treeview(frame_treeview, columns=("id", "nombre_producto", "cantidad_existencia", "cantidad_vendidas", "id_categoria", "detalles", "precio_productos"), show='headings')
        
        # Establecer encabezados
        headings = ["ID", "Nombre Producto", "Cantidad Existencia", "Cantidad Vendidas", "ID Categoría", "Detalles", "Precio"]
        for i, heading in enumerate(headings):
            self.tabla_productos.heading(self.tabla_productos["columns"][i], text=heading)

        self.tabla_productos.pack(expand=True, fill="both")
        self.cargar_productos_en_treeview()
        self.tabla_productos.bind("<<TreeviewSelect>>", self.selecciona_producto)

    def crear_formulario(self):
        frame_labels = tk.Frame(self.ventana_modificar, bg="#96c7e6")
        frame_labels.place(relx=0.05, rely=0.72, relheight=0.25, relwidth=0.9, anchor="nw")

        # Contenedor para la primera fila de los widgets
        first_row = tk.Frame(frame_labels, bg="#96c7e6")
        first_row.pack(pady=5)

        # NOMBRE
        labelNombre = tk.Label(first_row, text="Nombre")
        labelNombre.pack(side=tk.LEFT, padx=5)
        self.auxNombre = tk.StringVar()
        self.entry_nombre = tk.Entry(first_row, textvariable=self.auxNombre)
        self.entry_nombre.pack(side=tk.LEFT, padx=5)

        # CANTIDAD EXISTENCIA
        label_cantidadE = tk.Label(first_row, text="Cantidad Existencia")
        label_cantidadE.pack(side=tk.LEFT, padx=5)
        self.aux_existenciaE = tk.StringVar()
        self.entry_cantidadE = tk.Entry(first_row, textvariable=self.aux_existenciaE)
        self.entry_cantidadE.pack(side=tk.LEFT, padx=5)

        # CANTIDAD VENDIDAS
        label_cantidadV = tk.Label(first_row, text="Cantidad Vendidas")
        label_cantidadV.pack(side=tk.LEFT, padx=5)
        self.aux_vendidas = tk.StringVar()
        self.entry_cantidadV = tk.Entry(first_row, textvariable=self.aux_vendidas)
        self.entry_cantidadV.pack(side=tk.LEFT, padx=5)

        # Contenedor para la segunda fila de los widgets
        second_row = tk.Frame(frame_labels, bg="#96c7e6")
        second_row.pack(pady=5)

        # CATEGORIAS
        labelCategoria = tk.Label(second_row, text="Categoría")
        labelCategoria.pack(side=tk.LEFT, padx=5)
        self.aux_categoria = tk.StringVar()
        self.entry_cat = tk.Entry(second_row, textvariable=self.aux_categoria)
        self.entry_cat.pack(side=tk.LEFT, padx=5)

        # DETALLES
        label_detalles = tk.Label(second_row, text="Detalles")
        label_detalles.pack(side=tk.LEFT, padx=5)
        self.aux_detalles = tk.StringVar()
        self.entry_detalles = tk.Entry(second_row, textvariable=self.aux_detalles)
        self.entry_detalles.pack(side=tk.LEFT, padx=5)

        # PRECIO
        label_precio = tk.Label(second_row, text="Precio")
        label_precio.pack(side=tk.LEFT, padx=5)
        self.aux_precio = tk.StringVar()
        self.entry_precio = tk.Entry(second_row, textvariable=self.aux_precio)
        self.entry_precio.pack(side=tk.LEFT, padx=5)

        # Botón para modificar
        boton_modificar = tk.Button(frame_labels, text="Modificar Producto", command=self.confirmar_modificacion, bg="#d6022a", fg="white")
        boton_modificar.pack(pady=15)

    def cargar_productos_en_treeview(self):
        productos = self.objControlador.consultar_productos()
        if productos:
            for producto in productos:
                self.tabla_productos.insert("", "end", values=(
                    producto.get_id_producto(),
                    producto.get_nombre(),
                    producto.get_existencia(),
                    producto.get_cantidades_vendidas(),
                    producto.get_categoria(),
                    producto.get_detalles(),
                    producto.get_precio()
                ))
                print(producto)

    def selecciona_producto(self, event=None):
        seleccionado = self.tabla_productos.selection()
        if seleccionado:
            item = self.tabla_productos.item(seleccionado[0])
            values = item['values']

            # Asignar los valores a las variables StringVar
            self.auxNombre.set(values[1])
            self.aux_existenciaE.set(values[2])
            self.aux_vendidas.set(values[3])
            self.aux_categoria.set(values[4])
            self.aux_detalles.set(values[5])
            self.aux_precio.set(values[6])

    def confirmar_modificacion(self):
        datos_modificados = [self.auxNombre.get(), self.aux_existenciaE.get(), self.aux_vendidas.get(), self.aux_categoria.get(), self.aux_detalles.get(), self.aux_precio.get()]
        resultado = self.objControlador.modificar_producto(datos_modificados)

        if resultado:
            tk.messagebox.showinfo("Éxito", "El producto fue modificado exitosamente.")
            self.cargar_productos_en_treeview()
        else:
            tk.messagebox.showerror("Error", "Hubo un problema al modificar el producto.")


    
    def mostrar_productos_vendedor(self,frameContenido):
        self.letra=("Georgia",10, "bold")
        frameProductos=tk.Frame(frameContenido)
        frameProductos.place(relx=0.605,rely=0.13,relheight=0.85, relwidth=0.77,anchor="n")
        frameProductos.config(bg="#719ae2")
        frmTituloCatalogo=tk.Frame(frameProductos)
        frmTituloCatalogo.pack(padx=5,pady=5)
        labelTituloCatalogo=tk.Label(frmTituloCatalogo,text="PRODUCTOS", bg="#719ae2")
        labelTituloCatalogo.pack(expand=True,fill="both")
        labelTituloCatalogo.config(font=self.letra, fg="white")
        frmContenidoProductos=tk.Frame(frameProductos)
        frmContenidoProductos.pack(expand=True,fill="both")
        frmContenidoProductos.config(bg="#719ae2")
        
        self.image=self.interface_pictures("index/VISTA/imagenes/dolex.jpg",100,50)
        fProduct1=tk.Frame(frmContenidoProductos,height=40,width=40)
        fProduct1.place(relx=0.2,rely=0.05,relheight=0.25, relwidth=0.25,anchor="n")
        fProduct1.config(bg="#719ae2")
        LImagen1=tk.Label(fProduct1,image=self.image) 
        LImagen1.pack(expand=True,fill="both")
        LImagen1.config(bg="#719ae2")
        lp1=tk.Label(fProduct1,text="Medicamentos\nDolex\n $15.000",bg="white")
        lp1.config(bg="#aecef8", font=self.letra, fg="black")
        lp1.pack(expand=True,fill="both")
        self.image0=self.interface_pictures("index/VISTA/imagenes/bebe.jpg",100,50)
        fProduct2=tk.Frame(frmContenidoProductos, bg="#59baa9",height=20,width=20, )
        fProduct2.place(relx=0.5,rely=0.05,relheight=0.25, relwidth=0.25,anchor="n")
        fProduct2.config(bg="#719ae2")
        LImagen2=tk.Label(fProduct2,image=self.image0)
        LImagen2.pack(expand=True,fill="both")
        LImagen2.config(bg="#719ae2")
        lp2=tk.Label(fProduct2,text="   Cuidado del bebé\nPañales Huggies\n $50.000",bg="#ddffab")
        lp2.pack(expand=True,fill="both")
        lp2.config(bg="#aecef8", font=self.letra, fg="black")
        self.image2=self.interface_pictures("index/VISTA/imagenes/belleza.jpg",100,50)
        fProduct3=tk.Frame(frmContenidoProductos, bg="#59baa9",height=20,width=20, )
        fProduct3.place(relx=0.8,rely=0.05,relheight=0.25, relwidth=0.25,anchor="n")
        fProduct3.config(bg="#719ae2")
        LImagen3=tk.Label(fProduct3,image=self.image2)
        LImagen3.pack(expand=True,fill="both")
        LImagen3.config(bg="#719ae2")
        lp3=tk.Label(fProduct3,text="Belleza\nEsmalte+polvo\n precio $30.000",bg="#ddffab")
        lp3.pack(expand=True,fill="both")
        lp3.config(bg="#aecef8", font=self.letra, fg="black")
        self.image1=self.interface_pictures("index/VISTA/imagenes/mieltertos.jpg",100,50)
        fProduct4=tk.Frame(frmContenidoProductos, bg="#59baa9",height=20,width=20, )
        fProduct4.place(relx=0.2,rely=0.35,relheight=0.25, relwidth=0.25,anchor="n")
        fProduct4.config(bg="#719ae2")
        LImagen4=tk.Label(fProduct4,image=self.image1)
        LImagen4.pack(expand=True,fill="both")
        LImagen4.config(bg="#719ae2")
        lp4=tk.Label(fProduct4,text="Medicamentos\nMieltertos 1\\n $1.500",bg="#ddffab")
        lp4.pack(expand=True,fill="both")
        lp4.config(bg="#aecef8", font=self.letra, fg="black")
        self.image3=self.interface_pictures("index/VISTA/imagenes/benet.png",100,50)
        fProduct5=tk.Frame(frmContenidoProductos, bg="#59baa9",height=20,width=20, )
        fProduct5.place(relx=0.5,rely=0.35,relheight=0.25, relwidth=0.25,anchor="n")
        fProduct5.config(bg="#719ae2")
        LImagen5=tk.Label(fProduct5,image=self.image3)
        LImagen5.pack(expand=True,fill="both")
        LImagen5.config(bg="#719ae2")
        lp5=tk.Label(fProduct5,text="Bienestar\nBenet\n $80.000",bg="#ddffab")
        lp5.pack(expand=True,fill="both")
        lp5.config(bg="#aecef8", font=self.letra, fg="black")
        self.image4=self.interface_pictures("index/VISTA/imagenes/bebe2.png",100,50)
        fProduct6=tk.Frame(frmContenidoProductos, bg="#59baa9",height=20,width=20, )
        fProduct6.place(relx=0.8,rely=0.35,relheight=0.25, relwidth=0.25,anchor="n")
        fProduct6.config(bg="#719ae2")
        LImagen6=tk.Label(fProduct6,image=self.image4)
        LImagen6.pack(expand=True,fill="both")
        LImagen6.config(bg="#719ae2")
        lp6=tk.Label(fProduct6,text="Cuidado del bebé\nCrema N°4\n $10.000",bg="#ddffab")
        lp6.pack(expand=True,fill="both")
        lp6.config(bg="#aecef8", font=self.letra, fg="black")
        self.image5=self.interface_pictures("index/VISTA/imagenes/hogar.png",100,50)
        fProduct7=tk.Frame(frmContenidoProductos, bg="#59baa9",height=20,width=20, )
        fProduct7.place(relx=0.2,rely=0.65,relheight=0.25, relwidth=0.25,anchor="n")
        fProduct7.config(bg="#719ae2")
        LImagen7=tk.Label(fProduct7,image=self.image5)
        LImagen7.pack(expand=True,fill="both")
        LImagen7.config(bg="#719ae2")
        lp7=tk.Label(fProduct7,text="Hogar\nPapel Familia x12\n $15.000",bg="#ddffab")
        lp7.pack(expand=True,fill="both")
        lp7.config(bg="#aecef8", font=self.letra, fg="black")
        self.image6=self.interface_pictures("index/VISTA/imagenes/mieltertos2.jpg",100,50)
        fProduct8=tk.Frame(frmContenidoProductos, bg="#59baa9",height=20,width=20, )
        fProduct8.place(relx=0.5,rely=0.65,relheight=0.25, relwidth=0.25,anchor="n")
        fProduct8.config(bg="#719ae2")
        LImagen8=tk.Label(fProduct8,image=self.image6)
        LImagen8.pack(expand=True,fill="both")
        LImagen8.config(bg="#719ae2")
        lp8=tk.Label(fProduct8,text="Medicametos \nMieltertos ped\n $15.000",bg="#ddffab")
        lp8.pack(expand=True,fill="both")
        lp8.config(bg="#aecef8", font=self.letra, fg="black")
        self.image7=self.interface_pictures("index/VISTA/imagenes/bebe1.jpg",100,50)
        fProduct9=tk.Frame(frmContenidoProductos, bg="#59baa9",height=20,width=20, )
        fProduct9.place(relx=0.8,rely=0.65,relheight=0.25, relwidth=0.25,anchor="n")
        fProduct9.config(bg="#719ae2")
        LImagen9=tk.Label(fProduct9,image=self.image7)
        LImagen9.pack(expand=True,fill="both")
        LImagen9.config(bg="#719ae2")
        lp9=tk.Label(fProduct9,text="Cuidado del bebé\nLeche klim\n $80.000",bg="#ddffab")
        lp9.pack(expand=True,fill="both")
        lp9.config(bg="#aecef8", font=self.letra, fg="black")
        
        botonAdd=tk.Button(frmContenidoProductos,text="vender", command=None) #al pulsar debe generar un informe de tipo texto con ayuda del JSON
        botonAdd.place(relx=0.83,rely=0.92,relheight=0.06,relwidth=0.17,anchor="n")
        botonAdd.config( bg="#d6022a", font=("Georgia",7, "bold"), fg="white")
            
    def mostrar_informes(self,frameContenido):
        self.letra=("Georgia",10, "bold")
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
        
    def mostrar_contacto(self,frameContenido):
        frameContacto=tk.Frame(frameContenido)
        frameContacto.place(relx=0.605,rely=0.13,relheight=0.85, relwidth=0.77,anchor="n")
        frameContacto.config(bg="gray")
        self.contactoDrogueria=self.interface_pictures("index/VISTA/imagenes/contacto_drogueria.png",550,450)
        labelContacto=tk.Label(frameContacto,image=self.contactoDrogueria)
        labelContacto.pack(expand=True,fill="both")
        
    def crear_pie_pagina(self,framePrincipal):
        framePiePagina=tk.Frame(framePrincipal, bg="#8bb3e9")
        framePiePagina.config(width=800,height=100)
        framePiePagina.pack(pady=10)
        self.pastilla=self.interface_pictures("index/VISTA/imagenes/imagen_doctor.png",305,80)
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
        
    def interface_pictures(self,pic,ancho,altura):
        image= Image.open(pic).resize((ancho,altura))
        img=ImageTk.PhotoImage(image)
        return img
        
    def activar_mainloop(self):
        tk.mainloop()