from tkinter import *
from PIL import Image, ImageTk

root = Tk()

root.title("Clase 14")
root.iconbitmap("img\imagenes\icon\iconousar.ico")
root.geometry("600x600")

        #Uso de Checkboxes

#Crear variables para almacenar los valores
var = IntVar()
var2 = StringVar()
var3 = StringVar()



Label(root, text="A tu parecer ¿cual de estos lenguajes de programacion fue creado primero?").pack()
check = Checkbutton(root, text="C++", variable=var).pack()
check2 = Checkbutton(root, text="Python", variable=var2, offvalue="Rechazado", onvalue="Aceptado").pack()
check3 = Checkbutton(root, text="Javascript", variable=var3, onvalue="Aceptado", offvalue="Rechazado").pack()

def retornar():
    if var.get() == 1:  
        Label(root, text="VERDADERO!", font=18,fg="red").pack()
        
        Label(root, text="C++ es un lenguaje de programación diseñado en 1979 por\n Bjarne Stroustrup.", font=15, bg="orange").pack(pady=10)
        
        Label(root,text="La intención de su creación fue extender al lenguaje de programación C y añadir mecanismos que\n permiten la manipulación de objetos. En ese sentido, desde el punto de vista de los lenguajes\n orientados a objetos, C++ es un lenguaje híbrido.",padx=10, bg="skyblue").pack(padx=20, pady=10)
        
    else:
        Label(root, text=" Error la respuesta es incorrecta", font=18, fg="red", bg="Skyblue", padx=10).pack(pady=10)
        
    if var2.get() == "Aceptado":
        Label(root, text="VERDADERO!", font=18,fg="red").pack()
        
        Label(root, text=" Python se remonta hacia finales de los 80s y principio de los 90s", font=15, bg="orange").pack(pady=10)
        
        Label(root,text="su implementación comenzó en diciembre de 1982​ cuando en Navidad \nGuido Van Rossum que trabajaba en el (CWI) (un centro de investigación holandés de carácter oficial que,\n entre otras cosas, actualmente alberga la oficina central del W3C)",padx=10, bg="skyblue").pack(padx=20, pady=10)
    
    else: 
        Label(root, text=" Error la respuesta es incorrecta", font=18, fg="red", bg="Skyblue", padx=10).pack(pady=10)
        
    if var3.get() == "Aceptado":
        Label(root, text="VERDADERO!", font=18,fg="red").pack()
        
        Label(root, text=" Python se remonta hacia finales de los 80s y principio de los 90s", font=15, bg="orange").pack(pady=10)
        
        Label(root,text="su implementación comenzó en diciembre de 1982​ cuando en Navidad \nGuido Van Rossum que trabajaba en el (CWI) (un centro de investigación holandés de carácter oficial que,\n entre otras cosas, actualmente alberga la oficina central del W3C)",padx=10, bg="skyblue").pack(padx=20, pady=10)
    
    else: 
        Label(root, text=" Error la respuesta es incorrecta", font=18, fg="red", bg="Skyblue", padx=10).pack(pady=10)

bton = Button(root, text="Respuesta", command=retornar).pack()

#check2 = Checkbutton(root, text="Checkboxes 2", variable=var)
#check2.pack()

#check3 = Checkbutton(root, text="Checkboxes 3", variable=var)
#check3.pack()


    

#Button(root, text="Presioname!", command=lambda:personas.get())





root.mainloop()