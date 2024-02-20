from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("clase 11")
root.iconbitmap("img\imagenes\icon\iconousar.ico")

#Crear una nueva ventana

#   Ventana 1
titulo = Label(root, text="Bienvenido Edgar Gallardo", font=15, fg="#2980B9").grid(row=0, column=0, columnspan=2)
img = ImageTk.PhotoImage(Image.open("img\imagenes\cantantes\jackne.jpg"))
text_imag = Label(image = img)
text_imag.grid(row=1, column=0, columnspan=2)

def window():
    #ventana 2
    window_two = Toplevel()
    window_two.title("ventana 2")
    window_two.iconbitmap("img\imagenes\icon\iconousar.ico")
    
    titulo = Label(window_two, text="Bienvenido a la ventana 2", font=15, fg="#2980B9").grid(row=0, column=0, columnspan=2)
    
    #Volver variable('donde se almacena la imagen') local para mostrar dicha imagen
    global img
    
    img = ImageTk.PhotoImage(Image.open("img\imagenes\cantantes\contratar-a-eladio-carrion-onnix.jpg"))
    imagen = Label(window_two, image=img)
    
    imagen.grid(row=1, column=0, columnspan=2)
    return
info = Label(root, text="Salto de pagina =>", font=20, fg="red",pady=5).grid(row=2, column=0)
bton = Button(root, text="Presioname", bg="#C70039",fg="#FFC300", command=window).grid(row=2, column=1,padx=5)





root.mainloop()