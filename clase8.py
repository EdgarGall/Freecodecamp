from tkinter import *
root= Tk()

root.title("Los RadioButtoms")
root.iconbitmap("img\imagenes\icon\iconousar.ico")

js = StringVar()


def eleccion(valor):
    texto = Label(root, text=valor,font=20).pack()


# js.get() conseguir
# js.set() dar

Radiobutton(root, text="Javascript", variable=js, value="Javascript",command=lambda:eleccion(js.get())).pack()

Radiobutton(root, text="Java", variable=js, value="Java",command=lambda:eleccion(js.get())).pack()

Radiobutton(root, text="Python", variable=js , value="Python",command=lambda:eleccion(js.get())).pack()


texto = Label(root, text="Opciones:", font=18).pack()
root.mainloop()