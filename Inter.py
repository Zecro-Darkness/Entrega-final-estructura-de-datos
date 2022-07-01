from tkinter import *
from tkinter import ttk, font
#importar tkinter as tk
 
def send_data():
  id_info = id.get()
  Nombre_info = Nombre.get()
  Apellido_info = Apellido.get()
  Edad_info = str(Edad.get())
  Correo_info = str(Correo.get())
  Ciudad_info = str(Ciudad.get())
  Gamer_info = str(Gamer.get())
  Series_info = str(Series.get())
  print(id_info,"\t", Nombre_info,"\t", Apellido_info,"\t", Edad_info,"\t", Correo_info,"\t", Ciudad_info,"\t",Gamer_info,"\t",Series_info)

#  Open and write data to a file
  file = open("user.txt", "a")
  file.write(id_info)
  file.write("\t")
  file.write(Nombre_info)
  file.write("\t")
  file.write(Apellido_info)
  file.write("\t")
  file.write(Edad_info)
  file.write("\t")
  file.write(Correo_info)
  file.write("\t")
  file.write(Ciudad_info)
  file.write("\t")
  file.write(Gamer_info)
  file.write("\t")
  file.write(Series_info)
  file.write("\t\n")

  file.close()
  print(" Usuario Registrado. ID: {} | Nombre: {}  | Apellido:{} | Edad:{}  | Correo:{}  | Ciudad:{}  | Gamer:{} | Series:{}".format(id_info,Nombre_info, Apellido_info, Edad_info,Correo_info, Ciudad_info,Gamer_info,Series_info))
 
#  Elimina los datos anteriores
  id_entry.delete(0, END)
  Nombre_entry.delete(0, END)
  Apellido_entry.delete(0, END)
  Edad_entry.delete(0, END)
  Correo_entry.delete(0,END)
  Ciudad_entry.delete(0,END)
  Gamer_entry.delete(0,END)
  Series_entry.delete(0,END)

# Creamos una nueva instancia 
formulario = Tk()
formulario.geometry("550x750")
formulario.title("Tu amigo UN")
formulario.resizable(False,False)
formulario.config(background = "#213141")
main_title = Label(text = "Tu amigo UN", font = ("Cambria", 14), bg = "#56CD63", fg = "black", width = "500", height = "2")
main_title.pack()


# Define Label Fields 
id_label = Label(text = "ID", bg = "#FFEEDD")
id_label.place(x = 22, y = 70)
Nombre_label = Label(text = "Nombre", bg = "#FFEEDD")
Nombre_label.place(x = 22, y = 130)
Apellido_label = Label(text = "Apellido", bg = "#FFEEDD")
Apellido_label.place(x = 22, y = 190)
Edad_label = Label(text = "Edad", bg = "#FFEEDD")
Edad_label.place(x = 22, y = 250)
Correo_label = Label(text = "Correo", bg = "#FFEEDD")
Correo_label.place(x = 22, y = 310)
Ciudad_label = Label(text = "Ciudad", bg = "#FFEEDD")
Ciudad_label.place(x = 22, y = 370)
Gamer_label = Label(text = "Gamer", bg = "#FFEEDD")
Gamer_label.place(x = 22, y = 430)
Series_label = Label(text = "Series", bg = "#FFEEDD")
Series_label.place(x = 22, y = 490)


# Definir las variables
id = StringVar()
Nombre = StringVar()
Apellido = StringVar()
Edad = StringVar()
Correo = StringVar()
Ciudad = StringVar()
Gamer = StringVar()
Series = StringVar()


id_entry = Entry(textvariable = id, width = "40")
Nombre_entry = Entry(textvariable = Nombre, width = "40")
Apellido_entry = Entry(textvariable = Apellido, width = "40")
Edad_entry = Entry(textvariable = Edad, width = "40")
Correo_entry = Entry(textvariable = Correo, width = "40")
Ciudad_entry = Entry(textvariable = Ciudad, width = "40")
Gamer_entry = Entry(textvariable = Gamer, width = "40")
Series_entry = Entry(textvariable = Series, width = "40")


id_entry.place(x = 30, y = 100)
Nombre_entry.place(x = 30, y = 160)
Apellido_entry.place(x = 30, y = 220)
Edad_entry.place(x = 30, y = 280)
Correo_entry.place(x=30, y=340)
Ciudad_entry.place(x=30, y=400)
Gamer_entry.place(x=30, y=460)
Series_entry.place(x=30, y=520)

# Registro
submit_btn = Button(formulario,text = "Registrar", width = "30", height = "2", command = send_data, bg = "#00CD63")
submit_btn.place(x = 22, y = 580)

formulario.mainloop() 