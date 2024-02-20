from tkinter import *
from PIL import Image, ImageTk

root = Tk()

root.title("CheckBox 2")
root.iconbitmap("img\imagenes\icon\iconousar.ico")

#hacemos una lista con los elementos que formaran a ser el Radiobuttom
lista = [
    ('Lenguaje 1','Javascript'),
    ('Lenguaje 2','Java' ),
    ('Lenguaje 3','Python' ),
    ('Lenguaje 4','C++' )
]

Estudiante = StringVar()
Estudiante.set("Javacript")
#Estudiante.set("Edgar") 



# Radiobutton(root, text="Python", variable=js , value="Python",command=lambda:eleccion(js.get())).pack()

#   Al realizar el recorrido por el for, primero obtiene a persona(nombre), la variable siempre es constante por lo tanto, nunca cambia por eso es Estudiante, y el value sera el elemento que usamos para viajar por la lista
for persona, listado in lista:
    Radiobutton(root, text=persona, variable=Estudiante, value=listado).pack(anchor=W)

#   mandamos a llamar la funcion Estudiante(variable)todas, conseguimos segun el radiobutton seleccionado
boton = Button(root, text="Presioname!", command=lambda:eleccion(Estudiante.get())).pack()

#   Generara un Label (con el valor de eleccion( obtenido por el get(sconseguir), poco despues lo imprime en pantalla))
def eleccion(valor):
    texto = Label(root, text=valor, font=18).pack()

root.mainloop()