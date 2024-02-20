from tkinter import *
from PIL import Image,ImageTk

#importar libreria para usar base de datos
import sqlite3
root = Tk()
root.iconbitmap("img\imagenes\icon\iconousar.ico")
root.title("Base de datos")

root.geometry("400x550")

#base de Datos

#Paso 1: crear o conectarse a una base de datos
conexion = sqlite3.connect("prueba.db")

#Crear un cursor
navegar = conexion.cursor()


#Creamos las tablas de la  base de datos
'''
navegar.execute("""CREATE TABLE alumno(
    nombre text,
    apellido text,
    cedula integer,
    direccion text,
    anio text
    )""")
'''

#Crear cambios en la base de datos
conexion.commit()

#Cerrar conexion
conexion.close()




Label(root, text="BIENVENIDO A LA BASE DE DATOS", font=("Arial", 15, "italic")).grid(row=1, columnspan=2, column=0)

Label(root, text="Ingresa tu nombre:").grid(row=2, column=0)
nombre = Entry(root, width=20, cursor="xterm", bg="#2E86C1")
nombre.grid(row= 2, column=1, pady=5)

Label(root, text="Ingresa tu apellido:").grid(row=3, column=0)
apellido = Entry(root, width=20, cursor="xterm", bg="#2E86C1")
apellido.grid(row= 3, column=1, pady=5)

Label(root, text="Ingresa tu contraseña:").grid(row=4, column=0)
contraseña = Entry(root, width=20, cursor="xterm", bg="#2E86C1")
contraseña.grid(row= 4, column=1, pady=5)




#Interfaz

def enviar():
    
    conexion = sqlite3.connect("edificio.db")
    navegar = conexion.cursor()

    
    navegar.execute("INSERT INTO personal VALUES (:nombre, :apellido, :contraseña)",
                   {
                       'nombre': nombre.get(),
                       'apellido': apellido.get(),
                       'contraseña': contraseña.get() 
                   })
    
    nombre.delete(0, END)
    apellido.delete(0,END)
    contraseña.delete(0, END)
    
    conexion.commit()
    conexion.close()

    
boton_enviar = Button(root, text="Enviar datos", command=enviar, width=20, bg="#C70039",fg="#1F618D", font=("Arial",16,"bold", "italic"), cursor="hand2").grid(row=5, column=0, columnspan=2, pady=10, ipadx=70)




root.mainloop()