from tkinter import*

root =Tk()
#Establecer titulo a la ventana
root.title("Calculadora")

barra= Entry(root, width=50, borderwidth=5)

barra.grid(row="0", column="0", columnspan=3, padx=10, pady=10)


#Agregar funciones a los botones

def usar_boton(numero):
    #ingresa 
    numero_principal = barra.get()
    barra.delete(0,END)
    barra.insert(0, str(numero) + str(numero_principal))
    return

def boton_borrar():
    barra.delete(0,END)

def boton_suma():
    #pedir el primer numero de la calculadora
    primer_numero = barra.get()
    
    #Declarar una variable global para que pueda ser utilizada en el boton de igual
    global num1
    
    global operacion
    operacion= "suma"
    #Guardar el valor del 1er numero dentro de la variable global
    num1 = int(primer_numero)
    
    #Borrar la barra de ingreso para al dar igual o cambiar la funcion el numero desaparezca
    barra.delete(0,END)    
    
def boton_resta():
    primer_numero = barra.get()
    global num1
    global operacion
    operacion = "resta"
    num1 =int(primer_numero)
    barra.delete(0, END)
    
def boton_igual():
    if operacion =="resta":
        
        segundo_numero = barra.get()
        barra.delete(0,END)
        barra.insert(0, num1 - int(segundo_numero))
        
    if operacion =="suma":
        
        segundo_numero = barra.get()
        barra.delete(0,END)
        barra.insert(0, num1 + int(segundo_numero))

#Definir los botones

bton_1 = Button(root, text="1", font=22, padx=40, pady=20, command= lambda:usar_boton(1))

bton_2 = Button(root, text="2", font=22, padx=40, pady=20, command= lambda:usar_boton(2))

bton_3 = Button(root, text="3", font=22, padx=40, pady=20, command= lambda:usar_boton(3))

bton_4 = Button(root, text="4", font=22, padx=40, pady=20, command=lambda:usar_boton(4))

bton_5 = Button(root, text="5", font=22, padx=40, pady=20, command=lambda:usar_boton(5))

bton_6 = Button(root, text="6", font=22, padx=40, pady=20, command=lambda:usar_boton(6))

bton_7 = Button(root, text="7", font=22, padx=40, pady=20, command=lambda:usar_boton(7))

bton_8 = Button(root, text="8", font=22, padx=40, pady=20, command=lambda:usar_boton(8))

bton_9 = Button(root, text="9", font=22, padx=40, pady=20, command=lambda:usar_boton(9))

bton_0 = Button(root, text="0", font=22, padx=40, pady=20, command=lambda:usar_boton(0))

bton_suma = Button(root, text="+", font=22, padx=40, pady=20, command= lambda:boton_suma())

bton_resta = Button(root, text="-", font=22, padx=42, pady=20, command= lambda:boton_resta())

bton_igual = Button(root, text="=",bg="#2980B9", font=22, padx=40, pady=60, command=boton_igual)

bton_clean = Button(root, text="Clear", font=22, padx=22, pady=60, command=boton_borrar)

#Posicionar los botones en la calculadora

bton_1.grid(row=3,column=0)
bton_2.grid(row=3,column=1)
bton_3.grid(row=3,column=2)



bton_4.grid(row=2,column=0)
bton_5.grid(row=2,column=1)
bton_6.grid(row=2,column=2)


bton_7.grid(row=1,column=0)
bton_8.grid(row=1,column=1)
bton_9.grid(row=1,column=2)


bton_0.grid(row=4,column=0)
bton_suma.grid(row=4,column=1)
bton_resta.grid(row=4,column=2)

bton_clean.grid(row=1,column=3,rowspan=2)
bton_igual.grid(row=3,column=3,rowspan=2)










root.mainloop()


