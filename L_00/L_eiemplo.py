import tkinter as tk
from tkinter import *

class VentanaPrincipal(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        
        self.contenedor_principal = tk.Frame(self)
        self.contenedor_principal.pack(side="top", fill="both", expand=True)
        
        self.frame1 = Frame1(self.contenedor_principal, self)
        self.frame2 = Frame2(self.contenedor_principal, self)
        
        self.mostrar_frame1()
        
    def mostrar_frame1(self):
        self.frame2.pack_forget()
        self.frame1.pack()
        
    def mostrar_frame2(self):
        self.frame1.pack_forget()
        self.frame2.pack()

class Frame1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.controller = controller

    
        self.label = tk.Label(self, text="UPIIZ")
        self.label.pack(pady=10, padx=10)
        
        self.boton_siguiente = tk.Button(self, command=self.controller.mostrar_frame2)
        self.boton_siguiente.pack()
        
class Frame2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.controller = controller
        
        self.label = tk.Label(self, text="Frame 2")
        self.label.pack(pady=10, padx=10)
        
        self.boton_anterior = tk.Button(self, text="Anterior", command=self.controller.mostrar_frame1)
        self.boton_anterior.pack()

if __name__ == "__main__":
    ventana = VentanaPrincipal()
    ventana.mainloop()
