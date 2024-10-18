import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image
from VISTA.vistas.botones_productos import BotonesProducto

class Contenido:
    
    def __init__(self,objControlador,cargo):
        self.homeDrogueria=None
        self.contactoDrogueria=None
        self.objControlador=objControlador
        self.cargo=cargo
        self.categoria_seleccionada=None
        
    def seleccionar_categoria(self,categoria):
            self.objBotonesProducto.confirmar_mostrar_productos(categoria)
        
    def mostrar_home(self, frameContenido):
        frameHome = tk.Frame(frameContenido)
        frameHome.place(relx=0.605, rely=0.13, relheight=0.85, relwidth=0.77, anchor="n")
        frameHome.config(bg="#719ae2")
        frameImagen = tk.Frame(frameHome, bg="#719ae2")
        frameImagen.place(relx=0.5, rely=0.02, relheight=0.65, relwidth=0.96, anchor="n")
        self.homeDrogueria = self.interface_pictures("VISTA/imagenes/farmaceutica.png", 320, 280)
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
        self.objBotonesProducto=BotonesProducto(self.objControlador,self.cargo,self.frmContenidoProductos)
        self.objBotonesProducto.confirmar_mostrar_productos(self.categoria_seleccionada)
        
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
        
        self.contactoDrogueria = self.interface_pictures("VISTA/imagenes/contacto_haybet_salud.jpeg", 550, 450)
        labelImagen = tk.Label(frameContacto,bg="#719ae2", image=self.contactoDrogueria)
        labelImagen.place(relx=0.5, rely=0.01, relheight=0.98, relwidth=0.98, anchor="n")
        
    def interface_pictures(self,pic,ancho,altura):
            image= Image.open(pic).resize((ancho,altura))
            img=ImageTk.PhotoImage(image)
            return img