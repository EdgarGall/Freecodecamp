from tkinter import*
root =Tk()



#Input normal
a = Entry(root, width=20, borderwidth=3, bg="#DAF7A6", cursor="xterm")
a.grid(row=0,column=0)

#Funcion con concatenacion
def nombre():
    global texto1
    texto1 = Label(root, text  ="Bienvenido " + a.get())
    texto1.grid(row=1,column=0, columnspan=2)
    
def borrar():
    texto1.config(text="")
    a.delete(0, END)
    #texto1.after(1000, texto1.destroy())
    
boton1= Button(root, text="Ingresa", bg="#FFC300", padx="10", pady="10",command=nombre, cursor="hand2")
boton1.grid(row=0, column=1, padx=5)

boton2=Button(root, text="Borrar", bg="#FFC300", padx=10, pady=10, command=borrar, cursor="hand2")
boton2.grid(row=0, column=3, padx=5)


root.mainloop()
#NOTA: Los grids son muy importantes, sino te puede dar error

#Propiedades para los Inputs

'''
borderwidth=5


'''