from tkinter import *
from PIL import Image, ImageTk
from tkinter.font import Font
from color import texto,fondo_logo,fondo_texto,boton_color


root = Tk()
root.config(bg="#34495E")
root.title("Login con tkinter")
root.iconbitmap("img\imagenes\icon\iconousar.ico")
root.geometry("400x550")

img = ImageTk.PhotoImage(Image.open("proyectos\img\logouso.png"))
mi_img = Label(image=img, anchor="center", bg="#34495E")
mi_img.pack( pady=10)


#frame1 = LabelFrame(root, bg="#34495E",padx=50, pady=50).pack()

Label(root, text="Usuario",font=("Courier",14,"bold")).pack(pady=15)
entrada1 = Entry(root,text="Ingresa tu nombre",borderwidth=2, cursor="xterm").pack()

Label(root, text="Contraseña",font=("Courier",14,"bold")).pack(pady=15)
entrada2 = Entry(root,text="Ingresa tu contraseña",borderwidth=2, cursor="xterm").pack()


Button(root, text="Ingresar",font=("Arial",15,"italic"), cursor="hand2").pack(pady=20)
Button(root, text="Salir",font=("Courier",12,"bold"), cursor="hand2").pack(pady=20)



root.mainloop()