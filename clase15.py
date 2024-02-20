from tkinter import *
from tkinter import Button
from tkinter import PhotoImage


window = Tk()
window.title ("Prototipo")

instrumento = StringVar(window)
genero = StringVar(window)
compas = StringVar(window)
duracion = StringVar(window)
velnegra = StringVar(window)
instrumento.set("Instrumento Musical")
genero.set("Género Musical")
compas.set("Compás")
duracion.set("Duración")
velnegra.set("Velocidad Negra")

#listas
    #Instrumentos
ins = ["Guitarra","Piano"]

gener = [ "POP","R&B"]

comp = ["4/4","2/4"]

ritmo = ["30 segundos","60 segundos"]

ele = ["72","100"]


btn_elegirIns = OptionMenu(window,instrumento,*ins)
btn_elegirIns.config(font=("Century Gothic",10),height=2, width=20)
btn_elegirIns.place(x=40,y=100)

btn_generoMus = OptionMenu(window,genero,*gener)
btn_generoMus.config(font=("Century Gothic",10),height=2, width=20)
btn_generoMus.place(x=40,y=150)

btn_elegirCompas = OptionMenu(window,compas, *comp)
btn_elegirCompas.config(font=("Century Gothic",10),height=2, width=20)
btn_elegirCompas.place(x=40,y=200)

btn_elegirDuracion = OptionMenu(window,duracion, *ritmo)
btn_elegirDuracion.config(font=("Century Gothic",10),height=2, width=20)
btn_elegirDuracion.place(x=40,y=250)

btn_elegirVelNe = OptionMenu(window,velnegra, *ele)
btn_elegirVelNe.config(font=("Century Gothic",10),height=2, width=20)
btn_elegirVelNe.place(x=40,y=300)

window.geometry('950x550') #Definir tamaño de la ventana.
window.resizable(0,0)
window.mainloop()