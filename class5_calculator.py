from tkinter import*

root =Tk()
#Establecer titulo a la ventana
root.title("Calculadora")

barra= Entry(root, width=50, borderwidth=5)

barra.grid(row="0", column="0", columnspan=3, padx=10, pady=10)


#Agregar funciones a los botones



def usar_boton(numero):
    primer_numero = barra.get()
    barra.delete(0, END)
    barra.insert(0,str(primer_numero) + str(numero))

def usar_limpiar():
    barra.delete(0, END)

def usar_suma():
    primer_num = barra.get()
    global num1
    
    global opcion
    opcion = "suma"
    
    num1 = int(primer_num)
    barra.delete(0,END)
    
def usar_resta():
    primer_num = barra.get()
    global num1
    
    global opcion
    opcion = "resta"
    
    num1 = int(primer_num)
    barra.delete(0,END)
    
def usar_multi():
    primer_num = barra.get()
    
    global num1
    global opcion
    opcion == "multi"
    
    num1 = int(primer_num)
    
    barra.delete(0, END)
    
def usar_divi():
    primer_num = barra.get()
    
    global num1
    global opcion
    opcion="divi"
    
    num1 = int(primer_num)
    barra.delete(0, END)
    
    
    
def boton_igual():
    segundo_numero = barra.get()
    num2 = int(segundo_numero)
    barra.delete(0, END)
    
    if (opcion == "suma"):
        barra.insert(0, num1 + int(num2))
        
    if (opcion == "resta"):
        barra.insert(0, num1 - int(num2))
    
    if (opcion == "multi"):
        barra.insert(0, (num1 * int(num2)))
    
    if (opcion == "divi"):
        barra.insert(0, num1 / int(num2))
        


#Definir los botones

bton_1 = Button(root, text="1", font=22, padx=40, pady=20, command= lambda:usar_boton(1))

bton_2 = Button(root, text="2", font=22, padx=40, pady=20, command= lambda:usar_boton(2))

bton_3 = Button(root, text="3", font=22, padx=40, pady=20,command= lambda:usar_boton(3))

bton_4 = Button(root, text="4", font=22, padx=40, pady=20, command= lambda:usar_boton(4))

bton_5 = Button(root, text="5", font=22, padx=40, pady=20, command= lambda:usar_boton(5))

bton_6 = Button(root, text="6", font=22, padx=40, pady=20, command= lambda:usar_boton(6))

bton_7 = Button(root, text="7", font=22, padx=40, pady=20, command= lambda:usar_boton(7))

bton_8 = Button(root, text="8", font=22, padx=40, pady=20, command= lambda:usar_boton(8))

bton_9 = Button(root, text="9", font=22, padx=40, pady=20, command= lambda:usar_boton(9))

bton_0 = Button(root, text="0", font=22, padx=40, pady=20, command= lambda:usar_boton(0))


bton_suma = Button(root, text="+", font=22, padx=38, pady=20, command=usar_suma)

bton_resta = Button(root, text="-", font=22, padx=40, pady=20, command=usar_resta)

bton_multi = Button(root, text="x", font=22, padx=40, pady=20, command=usar_multi)

bton_divi = Button(root, text="/", font=22, padx=40, pady=20, command=usar_divi)

bton_igual = Button(root, text="=",bg="#2980B9", font=22, padx=40, pady=20, command=boton_igual)

bton_clean = Button(root, text="Clear", font=22, padx=22, pady=20, command=usar_limpiar)

#Posicionar los botones en la calculadora

bton_1.grid(row=3,column=0)
bton_2.grid(row=3,column=1)
bton_3.grid(row=3,column=2)

bton_suma.grid(row=3,column=3)



bton_4.grid(row=2,column=0)
bton_5.grid(row=2,column=1)
bton_6.grid(row=2,column=2)

bton_resta.grid(row=2,column=3)

bton_7.grid(row=1,column=0)
bton_8.grid(row=1,column=1)
bton_9.grid(row=1,column=2)

bton_multi.grid(row=1,column=3)

bton_0.grid(row=4,column=0)
bton_clean.grid(row=4,column=1)
bton_igual.grid(row=4,column=2)

bton_divi.grid(row=4,column=3)








root.mainloop()



# boton1 = Button(root, text="1", font=22, padx=40, pady=20).grid(row="1", column="0")

# boton2 = Button(root, text="2", font=22, padx=40, pady=20).grid(row="1", column="1")

# boton3 = Button(root, text="3", font=22,padx=40, pady=20).grid(row="1", column="2")

# boton4 = Button(root, text="4", font=22, padx=40, pady=20).grid(row="2", column="0")

# boton5 = Button(root, text="5", font=22, padx=40, pady=20).grid(row="2", column="1")

# boton6 = Button(root, text="6", font=22, padx=40, pady=20).grid(row="2", column="2")

# boton7 = Button(root, text="7", font=22, padx=40, pady=20).grid(row="3", column="0")

# boton8 = Button(root, text="8", font=22, padx=40, pady=20).grid(row="3", column="1")

# boton9 = Button(root, text="9", font=22, padx=40, pady=20).grid(row="3", column="2")

# boton0 = Button(root, text="0", font=22, padx=40, pady=20).grid(row="4", column="0")

# suma = Button(root, text="+", font=22, padx=40, pady=20).grid(row="4", column="1")

# resta = Button(root, text="-", font=22, padx=40, pady=20).grid(row="4", column="2")


# multiplicar = Button(root, text="x", font=22, padx=40, pady=20).grid(row="5", column="0")

# dividir = Button(root, text="/", font=22, padx=40, pady=20).grid(row="5", column="1")

# igual = Button(root, text="/", font=22, padx=40, pady=20).grid(row="5", column="2")