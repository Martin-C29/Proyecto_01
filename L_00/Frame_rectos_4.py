from tkinter import *
import tkinter as tk
from tkinter import ttk

raiz= tk.Tk()
raiz.title("Desarrollo de problemas de Engranes")
raiz.iconbitmap("logo upiiz.ico") #Imagen de fondo
raiz.geometry("800x600") # Tamaño de ventana por defecto

miFrame2=Frame(raiz, width=1920, height=1060)
MiImagen=PhotoImage(file="logo ipn (2).png")
MiImagen2=PhotoImage(file="logo upiiz.png")
miFrame2.pack()

Label(miFrame2, text="UPIIZ", fg="#440c29", font=("Serif", 45)).place(x=300,y=20)
Label(image=MiImagen).place(x=650,y=10)
Label(image=MiImagen2).place(x=5,y=10)
Label(miFrame2, text="Desarrollo de problemas de engranes",fg="#440c29", font=("Serif", 20)).place(x=150,y=80)
Label(miFrame2, text="Engranes Rectos",fg="black", font=("Serif", 22)).place(x=280,y=150)
Label(miFrame2, text="Problema 34",fg="black", font=("Serif", 18)).place(x=20,y=250)
Boton=tk.Button(text="Clic aqui")
Boton.place(x=50,y=300)
Label(miFrame2, text="Problema 35",fg="black", font=("Serif", 18)).place(x=200,y=250)
Boton=tk.Button(text="Clic aqui")
Boton.place(x=250,y=300)
Label(miFrame2, text="Problema 36",fg="black", font=("Serif", 18)).place(x=400,y=250)
Boton=tk.Button(text="Clic aqui")
Boton.place(x=450,y=300)
Label(miFrame2, text="Problema 37",fg="black", font=("Serif", 18)).place(x=20,y=450)
Boton=tk.Button(text="Clic aqui")
Boton.place(x=650,y=700)
Label(miFrame2, text="Problema 38",fg="black", font=("Serif", 18)).place(x=200,y=450)
Boton=tk.Button(text="Clic aqui")
Boton.place(x=50,y=500)
Label(miFrame2, text="Problema 39",fg="black", font=("Serif", 18)).place(x=400,y=450)
Boton=tk.Button(text="Clic aqui")
Boton.place(x=250,y=500)

raiz.mainloop()