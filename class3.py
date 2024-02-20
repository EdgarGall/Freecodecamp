#Creando botones

from tkinter import *
root = Tk()

#Funciones para mis objetos
def saludar():
    print("Holas Mundo")
    
def textoSalud():
    texto = Label(root, text="Tu presionaste el boton 1").grid(row="1",column="0")

#Objeto llamado boton1
boton = Button(root, text="Presioname", command=textoSalud, padx="10", pady="20", fg="black", bg="#C70039", font=22).grid(row="0", column="0")

#Objeto llamado boton2
boton2 = Button(root, text="Boton 2", padx=10, pady="20", fg="red", bg="#0B71B4", command=saludar).grid(row="0", column="1")

#Algunas formas para dar apariencia a los widgets
'''
padx="10"
pady="20"
fg="blue"
bg="yellow"

'''
   

    
root.mainloop()