import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image

class BotonesProducto:
    
    def __init__(self,objControlador,cargo,frmContenidoProductos):
        self.ventana_crear=None
        self.ventana_eliminar=None
        self.ventana_modificar=None
        self.frmContenidoProductos=frmContenidoProductos
        self.cargo=cargo
        self.objControlador=objControlador
        
    def confirmar_mostrar_productos(self,categoria_seleccionada):
        
        self.categoria_seleccionada=categoria_seleccionada
        
        for widget in self.frmContenidoProductos.winfo_children():
            widget.destroy()
            
        lista_productos = self.objControlador.consultar_detalles_productos()
        ruta_imagen_productos = "VISTA/imagenes/logo_productos.jpg"
        self.imagenes = []
        
        if self.categoria_seleccionada:
            lista_productos=[p for p in lista_productos if p[3]==self.categoria_seleccionada]

        for i, producto in enumerate(lista_productos):
            try:
                imagen = self.interface_pictures(ruta_imagen_productos, 100, 50)
                self.imagenes.append(imagen)
                fProduct = tk.Frame(self.frmContenidoProductos, bg="#59baa9")
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
            botonAdd=tk.Button(self.frmContenidoProductos,text="Agregar Producto", command=lambda:self.crear_producto()) 
            botonAdd.place(relx=0.5,rely=0.92,relheight=0.06,relwidth=0.17,anchor="n")
            botonAdd.config( bg="#d6022a", font=("Georgia",7, "bold"), fg="white")
            
            botonActualizar=tk.Button(self.frmContenidoProductos,text="Actualizar producto", command=lambda: self.modificar_producto()) 
            botonActualizar.place(relx=0.67,rely=0.92,relheight=0.06,relwidth=0.17,anchor="n")
            botonActualizar.config( bg="#d6022a", font=("Georgia",7, "bold"), fg="white")
            
            botonDelete=tk.Button(self.frmContenidoProductos,text="Eliminar Producto", command=lambda: self.eliminar_producto()) 
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
            self.confirmar_mostrar_productos(self.categoria_seleccionada)
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
                    self.confirmar_mostrar_productos(self.categoria_seleccionada)
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
                self.confirmar_mostrar_productos(self.categoria_seleccionada)
                self.ventana_modificar.withdraw()
                tk.messagebox.showinfo("Éxito", "El producto fue modificado exitosamente.")
            else:
                tk.messagebox.showerror("Error", "Hubo un problema al modificar el producto.")
        except ValueError as e:
                messagebox.showerror("Error",f"El producto no se pudo modificar: {e}")
                
    def interface_pictures(self,pic,ancho,altura):
            image= Image.open(pic).resize((ancho,altura))
            img=ImageTk.PhotoImage(image)
            return img