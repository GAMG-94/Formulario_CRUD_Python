from tkinter import *

aplicacion = Tk()
aplicacion.title("Formulario de Prueba")
aplicacion.geometry("1050x494+0+0")
aplicacion.config(bg="#2E4053")

title = Label(aplicacion, text="Sistema de gestión, Front en Python con TKinter", bd=14, relief=RIDGE, font=("Arial Black", 20), background="#85929E", fg="white").pack(fill=X)

informacion = LabelFrame(aplicacion, text="Datos del cliente", bd="10", relief=GROOVE, font=("Arial Black", 14), background="#85929E", fg="white")

informacion.place(x=6, y=80, height=265, width=500)

ClienteId = Label(informacion, text="Cliente ID", background="#85929E" ,font=("Arial Black", 16), fg="white").grid(row=0,column=0, padx=14)
Cliente_entry = Entry(informacion, borderwidth=4, width=24, font=("Arial Black", 12)).grid(row=0,column=1)

Nombre = Label(informacion, text="Nombre", background="#85929E" ,font=("Arial Black", 16), fg="white").grid(row=1,column=0, padx=14)
Nombre_entry = Entry(informacion, borderwidth=4, width=24, font=("Arial Black", 12)).grid(row=1,column=1)

Apellido = Label(informacion, text="Apellido", background="#85929E" ,font=("Arial Black", 16), fg="white").grid(row=2,column=0, padx=14)
Apellido_entry = Entry(informacion, borderwidth=4, width=24, font=("Arial Black", 12)).grid(row=2,column=1)

Direccion = Label(informacion, text="Dirección", background="#85929E" ,font=("Arial Black", 16), fg="white").grid(row=3,column=0, padx=14)
Direccion_entry = Entry(informacion, borderwidth=4, width=24, font=("Arial Black", 12)).grid(row=3,column=1)

Correo = Label(informacion, text="Correo", background="#85929E" ,font=("Arial Black", 16), fg="white").grid(row=4,column=0, padx=14)
Correo_entry = Entry(informacion, borderwidth=4, width=24, font=("Arial Black", 12)).grid(row=4,column=1)

Celular = Label(informacion, text="Celular", background="#85929E" ,font=("Arial Black", 16), fg="white").grid(row=5,column=0, padx=14)
Celular_entry = Entry(informacion, borderwidth=4, width=24, font=("Arial Black", 12)).grid(row=5,column=1)

fr1 = Frame(aplicacion, bd=10, relief=GROOVE, background="#85929E")
fr1.place(x=587,y=76, width=450, height=268)

lbl = Label(fr1, text="Datos", font=("Arial Black", 16), bd=8, relief=GROOVE, background="#85929E", fg="white").pack(fill=X)

Scrol = Scrollbar(fr1, orient=VERTICAL)
Area = Text(fr1, yscrollcommand=Scrol.set)
Scrol.pack(side=RIGHT, fill=Y)
Scrol.config(command=Area.yview)
Area.pack(fill=BOTH, expand=1)

Botones = LabelFrame(aplicacion, text="Botones", font=("Arial Black", 12), relief=GROOVE, bd=10, background="#85929E", fg="white")
Botones.place(x=0,y=354, relwidth=1, height=138)
Boton_frame = Frame(Botones, bd=8, relief=GROOVE, bg="#2E4053")
Boton_frame.place(x=0, width=1010, height=96)

Btn_Agregar = Button(Boton_frame, text="Agregar", font=("Arial Black",16), background="#2E4053", fg="white").grid(row=0,column=1,padx=16, pady=12)

Btn_Modificar = Button(Boton_frame, text="Modificar", font=("Arial Black",16), background="#2E4053", fg="white").grid(row=0,column=2,padx=16, pady=12)

Btn_Eliminar = Button(Boton_frame, text="Eliminar", font=("Arial Black",16), background="#2E4053", fg="white").grid(row=0,column=3,padx=16, pady=12)

Btn_Buscar = Button(Boton_frame, text="Buscar", font=("Arial Black",16), background="#2E4053", fg="white").grid(row=0,column=4,padx=16, pady=12)

Btn_Nuevo = Button(Boton_frame, text="Nuevo", font=("Arial Black",16), background="#2E4053", fg="white").grid(row=0,column=5,padx=16, pady=12)

Btn_Limpiar = Button(Boton_frame, text="Limpiar", font=("Arial Black",16), background="#2E4053", fg="white").grid(row=0,column=6,padx=16, pady=12)

Btn_Salir = Button(Boton_frame, text="Salir", font=("Arial Black",16), background="#2E4053", fg="white").grid(row=0,column=7,padx=16, pady=12)











aplicacion.mainloop()

