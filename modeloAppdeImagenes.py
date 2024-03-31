from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("APP_IMAGENES")
root.iconbitmap("img\imagenes\icon\iconousar.ico")

def ir(numero_imagen):
    #volver global a la variable para guardar los cambios
    global estado
    global mi_imagen
    global boton_derecha
    global boton_izquierda

    
    #borrar la imagen
    mi_imagen.grid_forget()
    
    #Crear la nueva imagen usando label y su nueva posicion
    mi_imagen= Label(image=lista_imagenes[numero_imagen-1])
    mi_imagen.grid(row=0, column=0, columnspan=3)
    
    #Para que continue lanzando mas imagenes le daremos una nueva funcion
    boton_derecha = Button(root, text=">>", fg="black", bg="#3650A6", padx=20, pady=20, font=22, command=lambda:ir(numero_imagen+1))
    
    boton_izquierda = Button(root, text="<<", fg="black", bg="#3650A6", padx=20, pady=20, font=22,command=lambda:ir(numero_imagen-1))
    
    boton_derecha.grid(row=1, column=2)
    boton_izquierda.grid(row=1, column=0)
    
    
    # if numero_imagen == 1:
    #     texto.grid_forget()
    #     texto = Label(root, text="texto1", font=22, fg="#20272C").grid(row=2, column=1)
    
    # if numero_imagen == 2:
    #     texto = Label(root, text="text2", font=22, fg="#20272C").grid(row=2, column=1)
        
    # if numero_imagen == 3:
    #     texto = Label(root, text="text3", font=22, fg="#20272C").grid(row=2, column=1)
    
    # if numero_imagen == 4:
    #     texto = Label(root, text="text4", font=22, fg="#20272C").grid(row=2, column=1)
        
    if numero_imagen == 5:
        boton_derecha = Button(root, text=">>", fg="black", bg="grey", padx=20, pady=20, font=22, state=DISABLED)
        boton_derecha.grid(row=1, column=2)

    estado = Label(root, text="Imagen "+ str(numero_imagen) + " de " + str(len(lista_imagenes)), bd=1, relief=SUNKEN, anchor=E, padx=10)    
    estado.grid(row=3,column=0, columnspan=3, sticky=W+E)
        
    
def atras(numero_imagen):
      #volver global a la variable para guardar los cambios
    global estado
    global mi_imagen
    global boton_derecha
    global boton_izquierda

    #Crear la nueva imagen usando label y su nueva posicion
    mi_imagen= Label(image=lista_imagenes[numero_imagen-1])
    mi_imagen.grid(row=0, column=0, columnspan=3)
    
    #Para que continue lanzando mas imagenes le daremos una nueva funcion
    boton_derecha = Button(root, text=">>", fg="black", bg="#3650A6", padx=20, pady=20, font=22, command=lambda:ir(numero_imagen+1))
    
    boton_izquierda = Button(root, text="<<", fg="black", bg="#3650A6", padx=20, pady=20, font=22,command=lambda:ir(numero_imagen-1))
    
    boton_derecha.grid(row=1, column=2)
    boton_izquierda.grid(row=1, column=0)
    
    
    # if numero_imagen == 1:
    #     texto.grid_forget()
    #     texto = Label(root, text="texto1", font=22, fg="#20272C").grid(row=2, column=1)
    
    # if numero_imagen == 2:
    #     texto = Label(root, text="text2", font=22, fg="#20272C").grid(row=2, column=1)
        
    # if numero_imagen == 3:
    #     texto = Label(root, text="text3", font=22, fg="#20272C").grid(row=2, column=1)
    
    # if numero_imagen == 4:
    #     texto = Label(root, text="text4", font=22, fg="#20272C").grid(row=2, column=1)
        
    if numero_imagen == 5:
        boton_derecha = Button(root, text=">>", fg="black", bg="grey", padx=20, pady=20, font=22, state=DISABLED)
        boton_derecha.grid(row=1, column=2)
    

    estado = Label(root, text="Imagen "+ str(numero_imagen) + " de " + str(len(lista_imagenes)), bd=1, relief=SUNKEN, anchor=E, padx=10)    
    estado.grid(row=3,column=0, columnspan=3, sticky=W+E)
        


imagen1 = ImageTk.PhotoImage(Image.open("img\imagenes\cantantes\contratar-a-eladio-carrion-onnix.jpg"))
imagen2 = ImageTk.PhotoImage(Image.open("img\imagenes\cantantes\Bad-Bunny-first-best-last-worst-.jpg"))
imagen3 = ImageTk.PhotoImage(Image.open("img\imagenes\cantantes\capturadepantall-936faa4a40ccece.jpg"))
imagen4 = ImageTk.PhotoImage(Image.open("img\imagenes\cantantes\imagenes-de-anuel-aa-2.jpg"))
imagen5 = ImageTk.PhotoImage(Image.open("img\imagenes\cantantes\Shakira - Closeup.jpg"))

lista_imagenes = [imagen1, imagen2, imagen3, imagen4, imagen5]

estado = Label(root, text="Imagen 1 de " + str(len(lista_imagenes)), bd=1, relief=SUNKEN, anchor=E, padx=10)


boton_derecha = Button(root, text=">>", fg="black", bg="#3650A6", padx=20, pady=20, font=22, command=lambda:ir(2))

boton_izquierda = Button(root, text="<<", fg="black", bg="#3650A6", padx=20, pady=20, font=22, command=lambda:atras(2))

boton_salir = Button(root,text="Exit", fg="white", bg="black", font=20, padx=31,pady=10, command=root.quit)

mi_imagen = Label(image = imagen1)
mi_imagen.grid(row=0,column=0, columnspan=3)

boton_derecha.grid(row=1, column=2)
boton_salir.grid(row=1, column=1)
boton_izquierda.grid(row=1, column=0)


texto = Label(root, text="Bienvenidos a mi app", font=22, fg="#20272C").grid(row=2, column=1)
estado.grid(row=3,column=0, columnspan=3, sticky=W+E)

root.mainloop()

