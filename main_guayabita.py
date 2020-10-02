import tkinter as tk
import tkinter.font as tkFont
from tkinter import *

ventana = tk.Tk()
ventana.title("Guayabita uwu")
ventana.geometry("1280x720")

fondo = PhotoImage(file = "fondo_guayabita.png")
label_fondo = Label(ventana, image=fondo)
label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

estilo = tkFont.Font(size=50)
titulo = Label(ventana, text="🅖🅤🅐🅨🅐🅑🅘🅣🅐", font=estilo, relief=RAISED)
titulo.pack()




ventana.mainloop()

