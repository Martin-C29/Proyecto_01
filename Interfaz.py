from tkinter import *
import tkinter as tk
from tkinter import ttk

raiz= tk.Tk()

raiz.title("Desarrollo de problemas de Engranes")

raiz.iconbitmap("logo upiiz.ico") #Imagen de fondo

raiz.geometry("800x600") # Tamaño de ventana por defecto

miFrame=Frame(raiz, width=1920, height=1060)
MiImagen=PhotoImage(file="logo ipn (2).png")
MiImagen2=PhotoImage(file="logo upiiz.png")
miFrame.pack()

Label(miFrame, text="UPIIZ", fg="#440c29", font=("Serif", 30)).place(x=350,y=20)
Label(miFrame, text="Desarrollo de problemas de engranes",fg="#440c29", font=("Serif", 20)).place(x=150,y=80)
Label(image=MiImagen).place(x=650,y=10)
Label(image=MiImagen2).place(x=5,y=10)
Label(miFrame, text="Escoge para que tipos de engranes quieres resolver el problema:", font=("Bell MT", 20)).place(x= 50,y=180)
Label(miFrame, text="Engranes rectos", font=("Georgia", 16)).place(x= 150,y=250)
Label(miFrame, text="Engranes Helicoidales", font=("Georgia", 16)).place(x= 500,y=250)

img_boton =tk.PhotoImage(file="Rectos.png")
boton = ttk.Button(image=img_boton)
boton.place(x=100, y=300)

img_boton1 =tk.PhotoImage(file="Helicoidales.png")
boton1 = ttk.Button(image=img_boton1)
boton1.place(x=500, y=300)

raiz.mainloop()