import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
import Juegos.Class_Guayabita

try:
    def Juego():
        ventana = tk.Tk()
        ventana.title("Guayabita uwu")
        ventana.geometry("1280x720")
        fondo = PhotoImage(file = "fondo_guayabita.png")
        label_fondo = Label(ventana, image=fondo)
        label_fondo.place(x=0, y=0, relwidth=1, relheight=1)
        estilo = tkFont.Font(size=50)
        titulo = Label(ventana, text="🅖🅤🅐🅨🅐🅑🅘🅣🅐", font=estilo, relief=RAISED)
        titulo.pack()
        usuario_actual = Label(ventana, text = " ")
        usuario_actual.pack()
        
        name_user = Entry(ventana, width=10)
        name_user.pack()
        btn_usuario = Button(ventana, text="Agregar usuario", command=lambda: clicked())
        btn_usuario.pack()
        
        def clicked():
            usuario = name_user.get()
            usuario_actual.configure(text="Bienvenid@, " + usuario)
        
        ventana.mainloop()
    if __name__ == "__main__":
        Juego()
except Exception:
    print("error")
