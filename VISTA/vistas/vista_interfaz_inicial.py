import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image
from VISTA.vistas.vista_contenido import Contenido

class Interfaz:
    def __init__(self,objControlador,cargo):
        self.logo=None
        self.reproducir=None
        self.pastilla=None
        self.frameContenido=None
        self.letra=None
        self.cargo=cargo
        self.objControlador=objControlador
        self.objContenido=Contenido(self.objControlador,self.cargo)
            
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
        boton_home=tk.Button(frameSecciones,bg="#d6022a",  text="Home",font=self.letra , fg="white", command= lambda: self.objContenido.mostrar_home(self.frameContenido))
        boton_home.place(relx=0.125,rely=0.81,relheight=0.2,relwidth=0.25,anchor="n")
        boton_products=tk.Button(frameSecciones,  bg="#d6022a",text="Productos", font=self.letra , fg="white", command= lambda: self.objContenido.mostrar_productos(self.frameContenido))
        boton_products.place(relx=0.37,rely=0.81,relheight=0.2,relwidth=0.25,anchor="n")
        if self.cargo=="Administrador":
            boton_informe=tk.Button(frameSecciones, bg="#d6022a", text="Informes", font=self.letra , fg="white", command=lambda: self.objContenido.mostrar_informes(self.frameContenido))
            boton_informe.place(relx=0.62,rely=0.81,relheight=0.2,relwidth=0.25,anchor="n")
        
        boton_contact=tk.Button(frameSecciones, bg="#d6022a", text="Contacto", font=self.letra , fg="white", command=lambda: self.objContenido.mostrar_contacto(self.frameContenido))
        if self.cargo=="Administrador":
            boton_contact.place(relx=0.87,rely=0.81,relheight=0.2,relwidth=0.25,anchor="n")
        else:
            boton_contact.place(relx=0.62,rely=0.81, relheight=0.2, relwidth=0.25, anchor="n")
        frameTituloEmpresa=tk.Frame(frameEncabezado)
        frameTituloEmpresa.place(relx=0.52,rely=0.05,relheight=0.9,relwidth=0.4,anchor="n")
        nombre=tk.Label(frameTituloEmpresa,bg="white", text="DROGUERÍA HAYBET" , font=("Georgia",20 , "bold") , fg="#d6022a")
        nombre.config(width=30,height=10)
        nombre.pack(expand=True)
        self.logo=self.interface_pictures("VISTA/imagenes/logo_haybet_salud.jpeg",160,150)
        LabelImagenEncabezado=tk.Label(frameEncabezado,image=self.logo)
        LabelImagenEncabezado.config(bg="white")
        LabelImagenEncabezado.place(relx=0.86,rely=0.05,relheight=0.9,relwidth=0.24,anchor="n")
    
    def crear_contenido_lateral(self,frameContenido):
        frameContenido.config(width=800,height=550, bg="#719ae2")
        frameContenido.pack(pady=10,padx=10,expand=True, fill="both")
        frameLateral=tk.Frame(frameContenido, bg="#8bb3e9")
        frameLateral.place(relx=0.11,rely=0.02,relheight=0.96,relwidth=0.2,anchor="n")
        self.reproducir=self.interface_pictures("VISTA/imagenes/imagen_play.png",145,140)
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
        botonC1=tk.Button(frameCategorias, text="Medicamentos", font=("Georgia",8, "bold"),bg="white", fg="#719ae2",command=lambda:self.objContenido.seleccionar_categoria("Medicamentos"))
        botonC1.place(relx=0.1,rely=0.2,relheight=0.6, relwidth=0.18,anchor="n")
        botonC2=tk.Button(frameCategorias, text="Bebés", font=("Georgia",8, "bold"),bg="white", fg="#719ae2",command=lambda:self.objContenido.seleccionar_categoria("Bebés"))
        botonC2.place(relx=0.3,rely=0.2,relheight=0.6, relwidth=0.18,anchor="n")
        botonC3=tk.Button(frameCategorias, text="Belleza", font=("Georgia",8, "bold") ,bg="white", fg="#719ae2",command=lambda:self.objContenido.seleccionar_categoria("Belleza"))
        botonC3.place(relx=0.5,rely=0.2,relheight=0.6, relwidth=0.18,anchor="n")
        botonC4=tk.Button(frameCategorias, text="Bienestar", font=("Georgia",8, "bold"),bg="white", fg="#719ae2",command=lambda:self.objContenido.seleccionar_categoria("Bienestar"))
        botonC4.place(relx=0.7,rely=0.2,relheight=0.6, relwidth=0.18,anchor="n")
        botonC5=tk.Button(frameCategorias, text="Hogar",bg="white",  font=("Georgia",8, "bold"), fg="#719ae2",command=lambda:self.objContenido.seleccionar_categoria("Hogar"))
        botonC5.place(relx=0.9,rely=0.2,relheight=0.6, relwidth=0.18,anchor="n")
        
    def crear_pie_pagina(self,framePrincipal):
        framePiePagina=tk.Frame(framePrincipal, bg="#8bb3e9")
        framePiePagina.config(width=800,height=100)
        framePiePagina.pack(pady=10)
        self.pastilla=self.interface_pictures("VISTA/imagenes/imagen_doctor.png",305,80)
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