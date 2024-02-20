
from tkinter import*
import tkinter.font as tkfont
from PIL import Image, ImageTk
import sqlite3

root = Tk()
root.title("Aplicando base de datos")
root.iconbitmap("img\imagenes\icon\iconousar.ico")
root.geometry("400x400")

#usando base de datos


titulo = Label(root, text="Base de Datos",font=("Arial",18,"bold")).grid(row=0, column=0, columnspan=2,padx=20)


busqueda = Entry(root, width=20, borderwidth=3, bg="#DAF7A6").grid(row=1,column=0)
buscar = Button(root, text="Buscar", font=14, pady=3, padx=3).grid(row=1, column=1)




root.mainloop()