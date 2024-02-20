from tkinter import *
from PIL import Image, ImageTk

#Debes importar
from tkinter import filedialog

root = Tk()
root.title("Importar imagenes")
root.iconbitmap("img\imagenes\icon\iconousar.ico")
#Aprendiendo a abrir archivos externos de los archivos

'''Abrir archivo = abrir ventana.con archivos( iniciar desde el directorio = ' *** ', titulo de la ventana, tipos de archivos por ver (('archivo png','* .png'),('Todos los archivos', '* .* ')))'''

def buscar():

    root.filename = filedialog.askopenfilename(initialdir="img\imagenes\cantantes", title="Seleccionar el archivo", filetypes=(("Archivos jpg", "*.jpg"),("Todos los archivos", "*.*")))
    
    #Ubicar archivos con directorio
        #descr = Label(root,text=root.filename, fg="#900C3F").pack(pady=10).pack()

    direct = root.filename
    
    global img, mi_imagen
    img = ImageTk.PhotoImage(Image.open(direct))
    mi_imagen = Label(image = img)
    mi_imagen.pack()
    
    
    return

def borrar():
    global mi_imagen

    
    mi_imagen.grid_forget()
    
    
    return
    
texto = Label(root,text="Bienvenido", font=15, fg="#900C3F").pack(pady=10)

boton = Button(root, text="buscar", width=10, pady=10, bg="#2E86C1", fg="#17202A", command=buscar).pack(pady=5)
boton = Button(root, text="Borrar", width=10, pady=10, bg="#2E86C1", fg="#17202A", command=borrar).pack(pady=5)
boton = Button(root, text="Salir", width=10, pady=10,bg="#2E86C1",fg="#17202A", command=root.quit).pack(pady=10)




root.mainloop()