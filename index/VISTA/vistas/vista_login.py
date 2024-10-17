import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image

class Login:
        
    def __init__(self):
        None
    
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