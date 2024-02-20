from tkinter import*
from PIL import Image, ImageTk

root = Tk()
root.title("Clase 6")
#agregarle un icono
root.iconbitmap("img\imagenes\icon\iconousar.ico")

#salir por medio de un boton
boton_salir = Button(root, text="SALIR",padx=20, pady=20, font=22, fg="#2980B9", bg="#20272C", command=root.quit)

boton_salir.pack()



mi_imagen = ImageTk.PhotoImage(Image.open("img\imagenes\cantantes\capturadepantall-936faa4a40ccece.jpg"))

mi_texto = Label(image = mi_imagen)

mi_texto.pack()
#Haciendo uso de iconos, imagenes y botones 






















root.mainloop()