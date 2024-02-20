from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Clase 13")
root.iconbitmap("img\imagenes\icon\iconousar.ico")



#aprender a hacer sliders (barritas)

vertical = Scale(from_=0, to=400, orient=VERTICAL,bg="blue", fg="#17202A")
vertical.pack()

horizontal = Scale(from_=0, to=400, orient=HORIZONTAL,bg="red", fg="#17202A")
horizontal.pack()

def slider():
    tamano_horiz = Label(root, text=horizontal.get(), font=10).pack()
    tamano_vert = Label(root, text=vertical.get(),font=10).pack()
    
    '''Usar aproposito un string en 'comillas' '''
    root.geometry(str(horizontal.get())+"x"+str(vertical.get()))

    
boton = Button(root, text="Pincha aqui!", command=slider).pack()
root.mainloop()