from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox


#Tipos de messagebox

#   showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

root = Tk()
root.title("Message Box")
root.iconbitmap("img\imagenes\icon\iconousar.ico")

def funcion2():
    res = messagebox.askokcancel("investigar", "Bienvenido")
    Label(root, text=res, font=12).pack()

Button(root,text="Cliqueame", font=15, fg="red", command=funcion2).pack()

'''
def funcion():
    respuesta = messagebox.askyesno("Leeme", "Felicitaciones te reiste!")
    if (respuesta == 1):
        Label(root, text="continuo", font=17).pack()

    else:
        messagebox.showwarning("Fin del programa", "Eres un aguafiestas")
        root.quit()
        
bton = Button(root, text="Presioname", font=18, command=funcion).pack()

'''
root.mainloop()