
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
        self.homeDrogueria=None
        self.contactoDrogueria=None
        self.letra=None
        self.cargo=None
        self.categoria_seleccionada=None

    def ventana_ingreso(self):
        self.ventanaLogin=tk.Tk()
        self.ventanaLogin.geometry("600x800")
        self.ventanaLogin.maxsize(600,650)
        self.ventanaLogin.title("INICIO SESION HAYBET SALUD")
        self.letra=("Georgia", 20, "bold")
        self.images = self.interface_pictures(r"index\VISTA\imagenes\pastillas.jpg", 210, 150)

        frameInicioSesion=tk.Frame(self.ventanaLogin)
        frameInicioSesion.config(bg="#96c7e6",width=400,height=500)
        frameInicioSesion.pack(expand=True,fill="both")
        
        frameTitulo=tk.Frame(frameInicioSesion,bg="white")
        frameTitulo.place(relx=0.7,rely=0,relheight=0.237, relwidth=0.69, anchor="n")
        labelTitulo=tk.Label(frameTitulo,bg= "white", text="INICIO DE SESION")
        labelTitulo.config(font=self.letra, fg="#d6022a")
        labelTitulo.pack(expand=True,fill="both")
        
        frameLogin=tk.Frame(frameInicioSesion, bg="#96c7e6")
        frameLogin.place(relx=0.5,rely=0.25,relheight=0.7, relwidth=0.65, anchor="n")
        
        LabelImagenLogin=tk.Label(frameInicioSesion,image=self.images)
        LabelImagenLogin.grid()
        
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
            self.cargo=self.cargoUsuario.get()

            if not all(char.isalpha() or char.isspace() for char in nombre):
                raise ValueError("El nombre solo debe contener letras y espacios")
            
            if not documento.isdigit():
                raise ValueError("El documento solo debe contener números")
            
            if not nombre or not documento:
                raise ValueError("Los campos deben ser llenados correctamente")
            
            if self.cargo==None:
                raise ValueError("Por favor, seleccione un rol")  
            
            x=1
            listaUsuario=[documento,nombre,x,self.cargo]
            
            try:
                    validacion_usuario=self.objControlador.validar_inicio_sesion(listaUsuario)
                    if validacion_usuario is True:
                        self.ventanaLogin.withdraw()
                        self.ventana_home()
                    else:
                        raise ValueError("Usuario,contraseña o rol incorrecto")
                    
            except ValueError as e:
                messagebox.showerror("Error",str(e))

        except ValueError as e:
            messagebox.showerror("Error",str(e))
            
            
    def ventana_home(self):
        
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
        self.crear_contenido_lateral(self.frameContenido) 
        self.crear_pie_pagina(framePrincipal)
        
    def crear_encabezado(self,framePrincipal):
        self.letra=("Georgia",7, "bold")
        frameEncabezado=tk.Frame(framePrincipal)
        frameEncabezado.config(height=200, bg="white")
        frameEncabezado.pack(padx=10,pady=10, expand=True, fill="both")
        frameSecciones=tk.Frame(frameEncabezado, bg="white")
        frameSecciones.place(relx=0.16,rely=0.05,relheight=0.9,relwidth=0.28,anchor="n")
        boton_home=tk.Button(frameSecciones,bg="#d6022a",  text="Home",font=self.letra , fg="white", command= lambda: self.mostrar_home(self.frameContenido))
        boton_home.place(relx=0.125,rely=0.81,relheight=0.2,relwidth=0.25,anchor="n")
        boton_products=tk.Button(frameSecciones,  bg="#d6022a",text="Productos", font=self.letra , fg="white", command= lambda: self.mostrar_productos(self.frameContenido))
        boton_products.place(relx=0.37,rely=0.81,relheight=0.2,relwidth=0.25,anchor="n")
        if self.cargo=="Administrador":
            boton_informe=tk.Button(frameSecciones, bg="#d6022a", text="Informes", font=self.letra , fg="white", command=lambda: self.mostrar_informes(self.frameContenido))
            boton_informe.place(relx=0.62,rely=0.81,relheight=0.2,relwidth=0.25,anchor="n")
        
        boton_contact=tk.Button(frameSecciones, bg="#d6022a", text="Contacto", font=self.letra , fg="white", command=lambda: self.mostrar_contacto(self.frameContenido))
        if self.cargo=="Administrador":
            boton_contact.place(relx=0.87,rely=0.81,relheight=0.2,relwidth=0.25,anchor="n")
        else:
            boton_contact.place(relx=0.62,rely=0.81, relheight=0.2, relwidth=0.25, anchor="n")
        frameTituloEmpresa=tk.Frame(frameEncabezado)
        frameTituloEmpresa.place(relx=0.52,rely=0.05,relheight=0.9,relwidth=0.4,anchor="n")
        nombre=tk.Label(frameTituloEmpresa,bg="white", text="DROGUERÍA HAYBET" , font=("Georgia",20 , "bold") , fg="#d6022a")
        nombre.config(width=30,height=10)
        nombre.pack(expand=True)
        self.logo=self.interface_pictures("index/VISTA/imagenes/logo_haybet_salud.jpeg",160,150)
        LabelImagenEncabezado=tk.Label(frameEncabezado,image=self.logo)
        LabelImagenEncabezado.config(bg="white")
        LabelImagenEncabezado.place(relx=0.86,rely=0.05,relheight=0.9,relwidth=0.24,anchor="n")
    
    def crear_contenido_lateral(self,frameContenido):
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
        botonC1=tk.Button(frameCategorias, text="Medicamentos", font=("Georgia",8, "bold"),bg="white", fg="#719ae2",command=lambda:self.seleccionar_categoria("Medicamentos"))
        botonC1.place(relx=0.1,rely=0.2,relheight=0.6, relwidth=0.18,anchor="n")
        botonC2=tk.Button(frameCategorias, text="Bebés", font=("Georgia",8, "bold"),bg="white", fg="#719ae2",command=lambda:self.seleccionar_categoria("Bebés"))
        botonC2.place(relx=0.3,rely=0.2,relheight=0.6, relwidth=0.18,anchor="n")
        botonC3=tk.Button(frameCategorias, text="Belleza", font=("Georgia",8, "bold") ,bg="white", fg="#719ae2",command=lambda:self.seleccionar_categoria("Belleza"))
        botonC3.place(relx=0.5,rely=0.2,relheight=0.6, relwidth=0.18,anchor="n")
        botonC4=tk.Button(frameCategorias, text="Bienestar", font=("Georgia",8, "bold"),bg="white", fg="#719ae2",command=lambda:self.seleccionar_categoria("Bienestar"))
        botonC4.place(relx=0.7,rely=0.2,relheight=0.6, relwidth=0.18,anchor="n")
        botonC5=tk.Button(frameCategorias, text="Hogar",bg="white",  font=("Georgia",8, "bold"), fg="#719ae2",command=lambda:self.seleccionar_categoria("Hogar"))
        botonC5.place(relx=0.9,rely=0.2,relheight=0.6, relwidth=0.18,anchor="n")
        
    def seleccionar_categoria(self,categoria):
        self.categoria_seleccionada=categoria
        self.confirmar_mostrar_productos(self.frmContenidoProductos)
        
        
    def mostrar_home(self, frameContenido):
        frameHome = tk.Frame(frameContenido)
        frameHome.place(relx=0.605, rely=0.13, relheight=0.85, relwidth=0.77, anchor="n")
        frameHome.config(bg="#719ae2")
        frameImagen = tk.Frame(frameHome, bg="#719ae2")
        frameImagen.place(relx=0.5, rely=0.02, relheight=0.65, relwidth=0.96, anchor="n")
        self.homeDrogueria = self.interface_pictures("index/VISTA/imagenes/farmaceutica.png", 320, 280)
        labelImagen = tk.Label(frameImagen,bg="#719ae2", image=self.homeDrogueria)
        labelImagen.place(relx=0.5, rely=0.01, relheight=0.98, relwidth=0.98, anchor="n")
        
        frameBienvenida = tk.Frame(frameHome, bg="#719ae2")
        frameBienvenida.place(relx=0.5, rely=0.65, relheight=0.32, relwidth=0.96, anchor="n")
        labelBienvenida = tk.Label(frameBienvenida,bg="#719ae2", font=("Georgia",16, "bold"), text="BIENVENIDO AL CONTROL DE INVENTARIO\nDE LA DROGUERIA HAYBET SALUD")
        labelBienvenida.pack(pady=20, padx=10)
        labelMensaje = tk.Label(frameBienvenida,bg="#719ae2", font=("Georgia",12, "bold"), text="Aquí podrás llevar un control detallado de tu inventario y\nobtener informes de tus ventas")
        labelMensaje.pack(pady=0, padx=10)
    
    def mostrar_productos(self,frameContenido):
        self.letra=("Georgia",10, "bold")
        frameProductos=tk.Frame(frameContenido)
        frameProductos.place(relx=0.605,rely=0.13,relheight=0.85, relwidth=0.77,anchor="n")
        frameProductos.config(bg="#719ae2")
        frmTituloCatalogo=tk.Frame(frameProductos)
        frmTituloCatalogo.pack(padx=5,pady=5)
        labelTituloCatalogo=tk.Label(frmTituloCatalogo,text="PRODUCTOS", bg="#719ae2")
        labelTituloCatalogo.pack(expand=True,fill="both")
        labelTituloCatalogo.config(font=self.letra, fg="black")
        self.frmContenidoProductos=tk.Frame(frameProductos)
        self.frmContenidoProductos.pack(expand=True,fill="both")
        self.frmContenidoProductos.config(bg="#719ae2")
        self.categoria_seleccionada=None
        self.confirmar_mostrar_productos(self.frmContenidoProductos)
        
    def confirmar_mostrar_productos(self,frmContenidoProductos):
        
        for widget in frmContenidoProductos.winfo_children():
            widget.destroy()
            
        lista_productos = self.objControlador.consultar_detalles_productos()
        ruta_imagen_productos = "index/VISTA/imagenes/logo_productos.jpg"
        self.imagenes = []
        
        if self.categoria_seleccionada:
            lista_productos=[p for p in lista_productos if p[3]==self.categoria_seleccionada]

        for i, producto in enumerate(lista_productos):
            try:
                imagen = self.interface_pictures(ruta_imagen_productos, 100, 50)
                self.imagenes.append(imagen)
                fProduct = tk.Frame(frmContenidoProductos, bg="#59baa9")
                fProduct.place(relx=(i % 3) * 0.3 + 0.2, rely=(i // 3) * 0.3 + 0.05, relheight=0.25, relwidth=0.25, anchor="n")
                fProduct.config(bg="#719ae2")

                LImagen = tk.Label(fProduct, image=imagen)
                LImagen.pack(expand=True, fill="both")
                LImagen.config(bg="#719ae2")

                lp = tk.Label(fProduct, text=str(producto[0]) + "\n" + str(producto[1]) + "\n" + str(producto[2]), bg="#ddffab")
                lp.pack(expand=True, fill="both")
                letra_productos=("Georgia", 10, "bold")
                lp.config(bg="#aecef8", font=letra_productos, fg="black")
            except Exception as e:
                print(f"Error al cargar la imagen por categoria {imagen[i]}: {e}")

        if self.cargo=="Administrador":
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
        self.ventana_crear = tk.Toplevel()
        self.ventana_crear.title("CREAR PRODUCTOS")
        self.ventana_crear.geometry('600x800')
        self.ventana_crear.maxsize(600,800)
          
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
        
        
        label_nombre=tk.Label(frameAdd, bg= "#96c7e6",text="Nombre del producto")
        label_nombre.config(font=self.letra)
        label_nombre.pack(pady=0.3)
        self.nombre=tk.StringVar()
        self.entry_nombre_crear=tk.Entry(frameAdd,textvariable=self.nombre)
        self.entry_nombre_crear.pack(pady=5)
        
        labelCantidadE=tk.Label(frameAdd, bg= "#96c7e6",text="Cantidad Existencia")
        labelCantidadE.config(font=self.letra)
        labelCantidadE.pack(pady=0.3)
        self.cantidadE=tk.StringVar()
        self.entrycantidadE_crear=tk.Entry(frameAdd,textvariable=self.cantidadE)
        self.entrycantidadE_crear.pack(pady=5)
        
        label_cantidadV=tk.Label(frameAdd , bg= "#96c7e6",text="Cantidad Vendida")
        label_cantidadV.config(font=self.letra)
        label_cantidadV.pack(pady=5)
        self.cantidadV=tk.StringVar()
        self.entry_cantidadV_crear=tk.Entry(frameAdd,textvariable=self.cantidadV)
        self.entry_cantidadV_crear.pack(pady=5)
        
        label_categoria=tk.Label(frameAdd , bg= "#96c7e6",text="Categoria")
        label_categoria.config(font=self.letra)
        label_categoria.pack(pady=5)
        lista_categorias=["Medicamentos","Bebés","Belleza","Bienestar","Hogar"]
        self.categoria=tk.StringVar()
        self.categoria.set(lista_categorias[0])
        self.entry_categoria_crear=tk.OptionMenu(frameAdd,self.categoria,*lista_categorias)
        self.entry_categoria_crear.pack(pady=5)
        
        label_detalles=tk.Label(frameAdd , bg= "#96c7e6",text="Detalles")
        label_detalles.config(font=self.letra)
        label_detalles.pack(pady=5)
        self.detalles=tk.StringVar()
        self.entry_detalles_crear=tk.Entry(frameAdd,textvariable=self.detalles)
        self.entry_detalles_crear.pack(pady=5)
        
        label_precio=tk.Label(frameAdd , bg= "#96c7e6",text="Precio")
        label_precio.config(font=self.letra)
        label_precio.pack(pady=5)
        self.precio=tk.StringVar()
        self.entry_precio_crear=tk.Entry(frameAdd,textvariable=self.precio)
        self.entry_precio_crear.pack(pady=5)

        boton_crear = tk.Button(self.ventana_crear, text="REGISTRAR PRODUCTO",
                                command=lambda: self.confirmar_crear(),
                                bg="#d6022a")
        boton_crear.config(font=self.letra, fg="white")
        boton_crear.pack(pady=5)
        
    def confirmar_crear(self):
        nombre=self.entry_nombre_crear.get()
        cantidad_existencia=self.entrycantidadE_crear.get()
        cantidad_vendida=self.entry_cantidadV_crear.get()
        categoria=self.categoria.get()
        detalles=self.entry_detalles_crear.get()
        precio=self.entry_precio_crear.get()
        
        if not all([nombre, cantidad_existencia,cantidad_vendida, categoria, detalles,precio]):
            messagebox.showwarning("Entrada inválida", "Por favor, complete todos los campos.")
            return

        try:
            precio = float(precio)
            cantidad_vendida = int(cantidad_vendida)
        except ValueError:
            messagebox.showwarning("Entrada inválida", "El precio debe ser un número y los vendidos un entero.")
            return
        
        try:
            listaProductos=[nombre,cantidad_existencia,cantidad_vendida,categoria,detalles,precio]
            self.objControlador.crear_producto(listaProductos)
            self.ventana_crear.withdraw()
            self.confirmar_mostrar_productos(self.frmContenidoProductos)
            messagebox.showinfo("Éxito","Producto registrado correctamente")
        except Exception as e:
            messagebox.showerror("Error", f"Error al registrar el producto {e}")
    
    def eliminar_producto(self):
        self.letra = ("Georgia", 12, "bold")
        self.ventana_eliminar = tk.Toplevel()  # Corrección aquí
        self.ventana_eliminar.title("ELIMINAR PRODUCTOS")
        self.ventana_eliminar.geometry('500x600')

        frame_eliminar=tk.Frame(self.ventana_eliminar)
        frame_eliminar.config(bg="#96c7e6",width=400,height=600)
        frame_eliminar.pack(expand=True,fill="both")
        
        self.tabla_eliminar = ttk.Treeview(frame_eliminar, columns=("codigo", "nombre", "precio"), show='headings')
        self.tabla_eliminar.heading("codigo", text="CODIGO")
        self.tabla_eliminar.heading("nombre", text="Nombre Producto")
        self.tabla_eliminar.heading("precio", text="Precio Producto")
        self.tabla_eliminar.column("codigo", width=100)
        self.tabla_eliminar.column("nombre", width=100)
        self.tabla_eliminar.column("precio", width=100)
        self.tabla_eliminar.pack()
        self.cargar_productos_treeview_eliminar()
        

        # Botón para eliminar el producto
        boton_eliminar = tk.Button(self.ventana_eliminar, text="Eliminar Producto",
                                   command=lambda: self.confirmar_eliminar(),
                                   bg="#d6022a")
        boton_eliminar.config(font=self.letra, fg="white")
        boton_eliminar.pack(pady=15)
        
    def confirmar_eliminar(self):
        id_seleccionado = self.tabla_eliminar.selection()
        if not id_seleccionado:
            messagebox.showerror("Error", "No se ha seleccionado ningún registro")
        else:
            item= self.tabla_eliminar.item(id_seleccionado[0])
            id=item["values"][0]
            try:
                if int(id) > 0:
                    self.tabla_eliminar.delete(id_seleccionado[0])
                    self.objControlador.eliminar_producto(id)
                    self.vaciar_tabla_eliminar()
                    self.cargar_productos_treeview_eliminar()
                    self.confirmar_mostrar_productos(self.frmContenidoProductos)
                    messagebox.showinfo("Acción Realizada Exitosamente", "Producto eliminado con éxito")
                else:
                    messagebox.showerror("Error", "No se puede eliminar el producto con ID 0")
            except ValueError:
                messagebox.showerror("Error", "El ID seleccionado no es válido")

    def modificar_producto(self):
        self.letra = ("Georgia", 12, "bold")
        self.ventana_modificar = tk.Toplevel()
        self.ventana_modificar.title("MODIFICAR PRODUCTOS")
        self.ventana_modificar.geometry('800x600')

        self.crear_titulo_modificar()
        self.crear_treeview()
        self.crear_formulario_modificar()

    def actualizar_treeview(self):
        None
    
    def crear_titulo_modificar(self):
        frameTitulo = tk.Frame(self.ventana_modificar)
        frameTitulo.place(relx=0.5, rely=0, relheight=0.1, relwidth=1, anchor="n")
        labelTitulo = tk.Label(frameTitulo, bg="white", text="MODIFICAR PRODUCTO")
        labelTitulo.config(font=self.letra, fg="#d6022a")
        labelTitulo.pack(expand=True, fill="both")

    def crear_treeview(self):
        frame_treeview = tk.Frame(self.ventana_modificar, bg="white")
        frame_treeview.place(relx=0.05, rely=0.15, relheight=0.55, relwidth=0.9, anchor="nw")

        self.tabla_productos = ttk.Treeview(frame_treeview, columns=("id", "nombre_producto", "cantidad_existencia", "cantidad_vendidas", "categoria", "detalles", "precio_producto"), show='headings')
        
        headings = ["ID", "Nombre Producto", "Cantidad Existencia", "Cantidad Vendidas", "Categoría", "Detalles", "Precio"]
        for i, heading in enumerate(headings):
            self.tabla_productos.heading(self.tabla_productos["columns"][i], text=heading)

        self.tabla_productos.pack(expand=True, fill="both")
        self.cargar_productos_en_treeview()
        self.tabla_productos.bind("<<TreeviewSelect>>", self.selecciona_producto)

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
    
    def cargar_productos_treeview_eliminar(self):
        productos = self.objControlador.consultar_productos()
        if productos:
            for producto in productos:
                self.tabla_eliminar.insert("", "end", values=(
                    producto.get_id_producto(),
                    producto.get_nombre(),
                    producto.get_precio()
                ))
        
    def selecciona_producto(self, event=None):
        seleccionado = self.tabla_productos.selection()
        if seleccionado:
            item = self.tabla_productos.item(seleccionado[0])
            values = item['values']
            self.entry_nombre.delete(0, tk.END)
            self.entry_nombre.insert(0, values[1])
            self.entry_cantidadE.delete(0, tk.END)
            self.entry_cantidadE.insert(0, values[2])
            self.entry_cantidadV.delete(0, tk.END)
            self.entry_cantidadV.insert(0, values[3])
            self.aux_categoria.set(values[4])
            self.entry_detalles.delete(0, tk.END)
            self.entry_detalles.insert(0, values[5])
            self.entry_precio.delete(0, tk.END)
            self.entry_precio.insert(0, values[6])
            
    def vaciar_tabla(self):
        filas = self.tabla_productos.get_children()
        for fila in filas:
            self.tabla_productos.delete(fila)
            
    def vaciar_tabla_eliminar(self):
        filas = self.tabla_eliminar.get_children()
        for fila in filas:
            self.tabla_eliminar.delete(fila)
            

    def crear_formulario_modificar(self):
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
        lista_categorias=["Medicamentos","Bebés","Belleza","Bienestar","Hogar"]
        self.aux_categoria = tk.StringVar()
        self.aux_categoria.set(lista_categorias[0])
        #PENDIENTE POR APARECER TEXTO EN OPTION MENU
        self.entry_categoria=tk.OptionMenu(second_row,self.aux_categoria,*lista_categorias)
        self.entry_categoria.pack(side=tk.LEFT,padx=5)
        


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

    def confirmar_modificacion(self):
        seleccion=self.tabla_productos.selection()
        item=self.tabla_productos.item(seleccion[0])
        id_producto=item["values"][0]
        nombre=self.entry_nombre.get()
        cantidadesE=self.entry_cantidadE.get()
        cantidadesV=self.entry_cantidadV.get()
        categoria=self.aux_categoria.get()
        detalles=self.entry_detalles.get()
        precio=self.entry_precio.get()
        
        if not all([nombre, cantidadesE,cantidadesV, categoria, detalles,precio]):
                    messagebox.showwarning("Entrada inválida", "Por favor, complete todos los campos.")
                    return

        try:
            precio = float(precio)
            cantidadesV = int(cantidadesV)
        except ValueError:
            messagebox.showwarning("Entrada inválida", "El precio debe ser un número y los vendidos un entero.")
            return
        try:
            datos_modificados = [id_producto,nombre,cantidadesE,cantidadesV,categoria,detalles, precio ]
            resultado = self.objControlador.modificar_producto(datos_modificados)
            if resultado is True:
                self.vaciar_tabla()
                self.cargar_productos_en_treeview()
                self.confirmar_mostrar_productos(self.frmContenidoProductos)
                tk.messagebox.showinfo("Éxito", "El producto fue modificado exitosamente.")
            else:
                tk.messagebox.showerror("Error", "Hubo un problema al modificar el producto.")
        except ValueError as e:
                messagebox.showerror("Error",f"El producto no se pudo modificar: {e}")
            
            
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
        
        listaMasVendidos=self.objControlador.consultar_productos_masVendidos()
        nombre_producto1=str(listaMasVendidos[0][0])
        cantidad1=listaMasVendidos[0][1]
        nombre_producto2=str(listaMasVendidos[1][0])
        cantidad2=listaMasVendidos[1][1]
        nombre_producto3=str(listaMasVendidos[2][0])
        cantidad3=listaMasVendidos[2][1]
        nombre_producto4=str(listaMasVendidos[3][0])
        cantidad4=listaMasVendidos[3][1]
        
        f1=tk.Frame(frmMasVendidos)
        f1.place(relx=0.27,rely=0.36,relheight=0.15,relwidth=0.45,anchor="n")
        f1.config(bg="#a5ccf1")
        label1=tk.Label(f1,text=nombre_producto1,bg="#a5ccf1",font=self.letra)
        label1.pack(expand=True,fill="both")
        f2=tk.Frame(frmMasVendidos)
        f2.place(relx=0.27,rely=0.52,relheight=0.15,relwidth=0.45,anchor="n")
        f2.config(bg="#a5ccf1")
        label2=tk.Label(f2,text=nombre_producto2,bg="#a5ccf1",font=self.letra)
        label2.pack(expand=True,fill="both")
        f3=tk.Frame(frmMasVendidos)
        f3.place(relx=0.27,rely=0.68,relheight=0.15,relwidth=0.45,anchor="n")
        f3.config(bg="#a5ccf1")
        label3=tk.Label(f3,text=nombre_producto3,bg="#a5ccf1",font=self.letra)
        label3.pack(expand=True,fill="both")
        f4=tk.Frame(frmMasVendidos)
        f4.place(relx=0.27,rely=0.84,relheight=0.15,relwidth=0.45,anchor="n")
        f4.config(bg="#a5ccf1")
        label4=tk.Label(f4,text=nombre_producto4,bg="#a5ccf1",font=self.letra)
        label4.pack(expand=True,fill="both")
        f5=tk.Frame(frmMasVendidos)
        f5.place(relx=0.73,rely=0.36,relheight=0.15,relwidth=0.45,anchor="n")
        f5.config(bg="#a5ccf1")
        label5=tk.Label(f5,text=cantidad1,bg="#a5ccf1",font=self.letra)
        label5.pack(expand=True,fill="both")
        f6=tk.Frame(frmMasVendidos)
        f6.place(relx=0.73,rely=0.52,relheight=0.15,relwidth=0.45,anchor="n")
        f6.config(bg="#a5ccf1")
        label6=tk.Label(f6,text=cantidad2,bg="#a5ccf1",font=self.letra)
        label6.pack(expand=True,fill="both")
        f7=tk.Frame(frmMasVendidos)
        f7.place(relx=0.73,rely=0.68,relheight=0.15,relwidth=0.45,anchor="n")
        f7.config(bg="#a5ccf1")
        label7=tk.Label(f7,text=cantidad3,bg="#a5ccf1",font=self.letra)
        label7.pack(expand=True,fill="both")
        f8=tk.Frame(frmMasVendidos)
        f8.place(relx=0.73,rely=0.84,relheight=0.15,relwidth=0.45,anchor="n")
        f8.config(bg="#a5ccf1")
        label8=tk.Label(f8,text=cantidad4,bg="#a5ccf1",font=self.letra)
        label8.pack(expand=True,fill="both")
        
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
        
        listaMenosVendidos=self.objControlador.consultar_productos_menosVendidos()
        nombre_producto5=str(listaMenosVendidos[0][0])
        cantidad5=listaMenosVendidos[0][1]
        nombre_producto6=str(listaMenosVendidos[1][0])
        cantidad6=listaMenosVendidos[1][1]
        nombre_producto7=str(listaMenosVendidos[2][0])
        cantidad7=listaMenosVendidos[2][1]
        nombre_producto8=str(listaMenosVendidos[3][0])
        cantidad8=listaMenosVendidos[3][1]
        
        f9=tk.Frame(frmMenosVendidos)
        f9.place(relx=0.27,rely=0.36,relheight=0.15,relwidth=0.45,anchor="n")
        f9.config(bg="#a5ccf1")
        label9=tk.Label(f9,text=nombre_producto5,bg="#a5ccf1",font=self.letra)
        label9.pack(expand=True,fill="both")
        f10=tk.Frame(frmMenosVendidos)
        f10.place(relx=0.27,rely=0.52,relheight=0.15,relwidth=0.45,anchor="n")
        f10.config(bg="#a5ccf1")
        label10=tk.Label(f10,text=nombre_producto6,bg="#a5ccf1",font=self.letra)
        label10.pack(expand=True,fill="both")
        f11=tk.Frame(frmMenosVendidos)
        f11.place(relx=0.27,rely=0.68,relheight=0.15,relwidth=0.45,anchor="n")
        f11.config(bg="#a5ccf1")
        label11=tk.Label(f11,text=nombre_producto7,bg="#a5ccf1",font=self.letra)
        label11.pack(expand=True,fill="both")
        f12=tk.Frame(frmMenosVendidos)
        f12.place(relx=0.27,rely=0.84,relheight=0.15,relwidth=0.45,anchor="n")
        f12.config(bg="#a5ccf1")
        label12=tk.Label(f12,text=nombre_producto8,bg="#a5ccf1",font=self.letra)
        label12.pack(expand=True,fill="both")
        f13=tk.Frame(frmMenosVendidos)
        f13.place(relx=0.73,rely=0.36,relheight=0.15,relwidth=0.45,anchor="n")
        f13.config(bg="#a5ccf1")
        label13=tk.Label(f13,text=cantidad5,bg="#a5ccf1",font=self.letra)
        label13.pack(expand=True,fill="both")
        f14=tk.Frame(frmMenosVendidos)
        f14.place(relx=0.73,rely=0.52,relheight=0.15,relwidth=0.45,anchor="n")
        f14.config(bg="#a5ccf1")
        label14=tk.Label(f14,text=cantidad6,bg="#a5ccf1",font=self.letra)
        label14.pack(expand=True,fill="both")
        f15=tk.Frame(frmMenosVendidos)
        f15.place(relx=0.73,rely=0.68,relheight=0.15,relwidth=0.45,anchor="n")
        f15.config(bg="#a5ccf1")
        label15=tk.Label(f15,text=cantidad7,bg="#a5ccf1",font=self.letra)
        label15.pack(expand=True,fill="both")
        f16=tk.Frame(frmMenosVendidos)
        f16.place(relx=0.73,rely=0.84,relheight=0.15,relwidth=0.45,anchor="n")
        f16.config(bg="#a5ccf1")
        label16=tk.Label(f16,text=cantidad8,bg="#a5ccf1",font=self.letra)
        label16.pack(expand=True,fill="both")
        
        botonGenerar=tk.Button(frameEstadisticas,text="Generar informe", command=lambda:self.crear_archivo())
        botonGenerar.place(relx=0.83,rely=0.92,relheight=0.06,relwidth=0.17,anchor="n")
        botonGenerar.config( bg="#d6022a", font=("Georgia",7, "bold"), fg="white")
        
    def crear_archivo(self):
        self.objControlador.crear_archivo()
        messagebox.showinfo("Archivo creado", "Tu informe ha sido generado correctamente")
        
    def mostrar_contacto(self,frameContenido):
        frameContacto = tk.Frame(frameContenido)
        frameContacto.place(relx=0.605, rely=0.13, relheight=0.85, relwidth=0.77, anchor="n")
        frameContacto.config(bg="#719ae2")
        
        self.contactoDrogueria = self.interface_pictures("index/VISTA/imagenes/contacto_haybet_salud.jpeg", 550, 450)
        labelImagen = tk.Label(frameContacto,bg="#719ae2", image=self.contactoDrogueria)
        labelImagen.place(relx=0.5, rely=0.01, relheight=0.98, relwidth=0.98, anchor="n")
        
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