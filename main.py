##Tkinter es una libreria que nos permite gestionar Interfaces graficas en Python
from tkinter import *
import random


if __name__ == "__main__":
    ##Interfaz gráfica en Tkinter
    raiz = Tk()
    raiz.resizable(0,0)
    raiz.config(bg="red")
    raiz.geometry('320x540')
    raiz.iconbitmap(default="layers/titleicon.ico")

    unFrame = Frame()
    unFrame.pack()
    unFrame.config(width=320, height=540)
    unFrame.config(bd=0)

    fondo = PhotoImage(file="layers/android.png")
    miLabel = Label(unFrame, image=fondo, cursor="shuttle").place(x=0,y=0)

    miLabel2=Label(unFrame, text="El Genio Virtual", bg = "black", fg="white", font=('arial', 18)).place(x=80,y=30)

    miLabel3=Label(unFrame, text="Genio quiere ayudarte a ser millonario,\n indicale tú número ganador, él te correjira. \n Solo 4 dígitos... :", bg = "black", fg="white", 
    font=('arial', 10) , anchor="center").place(x=38,y=75)

    num = StringVar ()
    cuadroEntrada = Entry(unFrame, width=6, cursor="trek", textvariable=num, font=('arial', 20)).place(x=120,y=165)


    primerDig = random.randint(0,9)
    segunDig = random.randint(0,9)
    tercerDig = random.randint(0,9)
    cuartoDig = random.randint(0,9)

    sumaDigMachine = (primerDig * 1000)+(segunDig * 100)+(tercerDig*10)+(cuartoDig*1)

    
    
    def candela():
        numero = num.get()
        print(numero)
        x = [int(a) for a in str(numero)]
        print(x)

        sumaDigUser = (x[0] * 1000) + (x[1] * 100) + (x[2] * 10) + (x[3] * 1)

        if sumaDigUser > sumaDigMachine:
            print ("¡Réstele!")
            miLabel3=Label(unFrame, text="¡Réstele!", bg = "black", fg="white", font=('arial', 18)).place(x=120,y=300)
        elif sumaDigUser < sumaDigMachine:
            print ("¡Súmele!")
            miLabel3=Label(unFrame, text="¡Súmele!", bg = "black", fg="white", font=('arial', 18)).place(x=120,y=300)
        else:
            if ( x[0] == 0 ): 
                print ("El numero ganador es: " + f'0{sumaDigMachine}' + " vaya y lo hace!!!")
                miLabel3=Label(unFrame, text="El numero ganador es: " + f'0{sumaDigMachine}' + "\n vaya y lo hace!!!", bg = "black", fg="red", font=('arial', 20)).place(x=120,y=300)       
            else: 
                print ("El numero ganador es: " + f'{sumaDigMachine}' + " vaya y lo hace!!!")
                miLabel3=Label(unFrame, text="El numero ganador es: " + f'{sumaDigMachine}' + " \n vaya y lo hace!!!", bg = "black", fg="red", font=('arial', 20)).place(x=120,y=300)


    botonEnviar = Button(unFrame, text="PÉGUELE AL CHANCE", command= candela).place(x=105,y=215)
    
    fondo2 = PhotoImage(file="layers/python.png")
    miLabel4=Label(unFrame, image=fondo2).place(x=95,y=350)

   

    raiz.mainloop()