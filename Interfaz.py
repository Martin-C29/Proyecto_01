from tkinter import *

raiz= Tk()

raiz.title("Desarrollo de problemas de Engranes")

raiz.iconbitmap("logo upiiz.ico") #Imagen de fondo

raiz.geometry("800x600") # Tamaño de ventana por defecto

miFrame=Frame(raiz, width=800, height=600, bg="gray")

miFrame.pack()
MiImagen=PhotoImage(file="logo ipn (2).png")
MiImagen2=PhotoImage(file="logo upiiz.png")

Label(miFrame, text="UPIIZ", fg="#5e2129", font=("Serif", 30), bg="gray").place(x=350,y=20)

Label(miFrame, text="Desarrollo de problemas de engranes", fg="#5e2129", font=("Serif", 20), bg="gray").place(x=150,y=80)

Label(image=MiImagen, bg="gray").place(x=650,y=10)

Label(image=MiImagen2, bg="gray").place(x=5,y=10)

Label(miFrame, text="Resolver problema 1", font=("Serif", 14), bg="gray").place(x=50,y=150)

Label(miFrame, text="Resolver problema 2", font=("Serif", 14), bg="gray").place(x=300,y=150)

Label(miFrame, text="Resolver problema 3", font=("Serif", 14), bg="gray").place(x=600,y=150)

Label(miFrame, text="Resolver problema 4", font=("Serif", 14), bg="gray").place(x=50,y=300)

Label(miFrame, text="Resolver problema 5", font=("Serif", 14), bg="gray").place(x=300,y=300)

Label(miFrame, text="Resolver problema 6", font=("Serif", 14), bg="gray").place(x=600,y=300)

raiz.mainloop()