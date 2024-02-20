 #Usando Frames

from tkinter import*

root=Tk()
root.title("Frames")
root.iconbitmap("img\imagenes\icon\iconousar.ico")

texto = Label(root, text="VISTE MI FRAME", font=22, pady=10, padx=5).grid(row=0, column=0, columnspan=3)

frame = LabelFrame(root, text="Frame nuevo", padx=50, pady=50,  bg="#FFC300")    #Dentro del frame
frame.grid(row=1, column=0, padx=20, pady=20) #Fuera del frame

texto = Label(frame, text="Bienvenidos a la Jungla", bg="#FFC300", fg="black",font=20, padx=10, pady=10).grid(row=0, column=0, columnspan=2)


boton = Button(frame, text="Boton", cursor="hand2").grid(row=1, column=0, pady=10)
boton = Button(frame, text="Boton", cursor="hand2").grid(row=2, column=0, pady=10)

boton = Button(frame, text="Boton", cursor="hand2").grid(row=1, column=1)
boton = Button(frame, text="Boton", cursor="hand2").grid(row=2, column=1)




root.mainloop()