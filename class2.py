from tkinter import *

root = Tk()

texto1 = Label(root, text="Bienvenidos a mi programa").grid(row="0", column="0")

texto2 = Label(root, text="Encantado de conocerte").grid(row="1", column="1")

texto3 = Label(root, text="Mi nombre es Edgar").grid(row="2", column="2")

#texto1.grid(row=0, column=0)
#texto2.grid(row=1, column=1)
#texto3.grid(row=2, column=2)
root.mainloop()