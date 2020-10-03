import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
import Juegos.Class_Guayabita

try:
    def Juego():

        ventana = tk.Tk()
        ventana.title("Guayabita uwu")
        ventana.geometry("1280x720")
        fondo = PhotoImage(file = "fondo_guay.png")
        label_fondo = Label(ventana, image=fondo)
        label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

        def GetSaldoUsuario(y):
                #EN ESTA FUNCION VA LA COMUNICACION CON LA BASE DE DATOS PARA CONSEGUIR EL SALDO ACTUAL DEL USUARIO, ESTA FUNCION DEBE RETORNAR EL SALDO ACTUAL
                if(y==1):
                    saldo = 200000
                return saldo   
        
        estilo = tkFont.Font(size=50)
        titulo = Label(ventana, text="🅖🅤🅐🅨🅐🅑🅘🅣🅐", font=estilo, relief=RAISED, borderwidth=3).place(x=200,y=25)
        
        
        marco = Frame(ventana, relief=RAISED, borderwidth=3)
        marco.place(x=35, y=30)
        usuario_actual = Label(marco, text="Ingrese su nombre")#.grid(row=0)
        usuario_actual.pack()
        name_user = Entry(marco)#.grid(row=1, column=1)
        name_user.pack()

        marco_saldo = Frame(ventana, relief = RAISED, borderwidth=3)
        marco_saldo.place(x=665,y=30)
        texto_saldo = Label(marco_saldo, text="Su saldo actual es de:")
        texto_saldo.pack()
        estilo_saldo = tkFont.Font(size=15)
        texto_saldo_num = Label(marco_saldo, text=" ",font=estilo_saldo)
        texto_saldo_num.pack()

        def clicked():
            usuario = name_user.get()
            usuario_actual.configure(text="Bienvenid@, " + usuario)
            saldito = GetSaldoUsuario(1)  
            texto_saldo_num["text"] = saldito
            

        btn_usuario = Button(marco, text="Agregar usuario", command=clicked)
        btn_usuario.pack()
        

        marco_der = Frame(ventana, width = 430, height=720, cursor="dotbox")
        marco_der.pack(side=RIGHT)
        estilo2 = tkFont.Font(size=30)
        titulo_inst = Label(marco_der,text="¿𝘾𝙤𝙢𝙤 𝙟𝙪𝙜𝙖𝙧 𝙜𝙪𝙖𝙮𝙖𝙗𝙞𝙩𝙖?", font=estilo2)
        titulo_inst.pack()
        estilo3=tkFont.Font(size=15)
        primero = Label(marco_der,text="\n1. 𝙋𝙖𝙜𝙖𝙨 𝙚𝙡 𝙥𝙧𝙚𝙘𝙞𝙤 𝙙𝙚 𝙡𝙖 𝙚𝙣𝙩𝙧𝙖𝙙𝙖", font=estilo3).pack()
        segundo = Label(marco_der,text="\n2. 𝙏𝙞𝙧𝙖𝙨 𝙪𝙣 𝙙𝙖𝙙𝙤", font=estilo3).pack()
        tercero = Label(marco_der,text="\n3. 𝘿𝙚𝙘𝙞𝙙𝙚𝙨 𝙨𝙞 𝙫𝙖𝙨 𝙥𝙤𝙧 𝙩𝙤𝙙𝙤 𝙡𝙤 𝙦𝙪𝙚 𝙝𝙖𝙮 𝙚𝙣 𝙡𝙖 \n𝙢𝙚𝙨𝙖 𝙤 𝙥𝙤𝙧 𝙚𝙡 𝙥𝙧𝙚𝙘𝙞𝙤 𝙙𝙚 𝙡𝙖 𝙚𝙣𝙩𝙧𝙖𝙙𝙖", font=estilo3).pack()
        cuarto =  Label(marco_der,text="\n4. 𝙑𝙪𝙚𝙡𝙫𝙚𝙨 𝙖 𝙩𝙞𝙧𝙖𝙧 𝙚𝙡 𝙙𝙖𝙙𝙤", font=estilo3).pack()
        todo =  Label(marco_der,text="\n𝙎𝙞 𝙛𝙪𝙞𝙨𝙩𝙚 𝙥𝙤𝙧 𝙩𝙤𝙙𝙤", font=estilo3).pack()
        quinto_todo = Label(marco_der,text="- 𝙎𝙞 𝙨𝙖𝙘𝙖𝙨 𝙪𝙣 𝙣𝙪𝙢𝙚𝙧𝙤 𝙢𝙖𝙮𝙤𝙧 𝙦𝙪𝙚 𝙚𝙡 𝙙𝙚 𝙩𝙪 𝙥𝙧𝙞𝙢𝙚𝙧 \n𝙡𝙖𝙣𝙯𝙖𝙢𝙞𝙚𝙣𝙩𝙤, 𝙩𝙚 𝙡𝙡𝙚𝙫𝙖𝙨 𝙩𝙤𝙙𝙤 𝙡𝙤 𝙦𝙪𝙚 𝙝𝙖𝙮 𝙚𝙣 𝙡𝙖 𝙢𝙚𝙨𝙖", font=estilo3).pack()
        sexto_todo = Label(marco_der,text=" - 𝙎𝙞𝙣𝙤, 𝙥𝙞𝙚𝙧𝙙𝙚𝙨 𝙪𝙣𝙖 𝙘𝙖𝙣𝙩𝙞𝙙𝙖𝙙 𝙞𝙜𝙪𝙖𝙡 𝙖 𝙡𝙤 𝙦𝙪𝙚 𝙝𝙖𝙮 \n𝙚𝙣 𝙡𝙖 𝙢𝙚𝙨𝙖", font=estilo3).pack()
        entrada =  Label(marco_der,text="\n𝙎𝙞 𝙛𝙪𝙞𝙨𝙩𝙚 𝙥𝙤𝙧 𝙡𝙤 𝙙𝙚 𝙡𝙖 𝙚𝙣𝙩𝙧𝙖𝙙𝙖", font=estilo3).pack()
        quinto_entrada = Label(marco_der,text="- 𝙎𝙞 𝙨𝙖𝙘𝙖𝙨 𝙪𝙣 𝙣𝙪𝙢𝙚𝙧𝙤 𝙢𝙖𝙮𝙤𝙧 𝙦𝙪𝙚 𝙚𝙡 𝙙𝙚 𝙩𝙪 𝙥𝙧𝙞𝙢𝙚𝙧 \n𝙡𝙖𝙣𝙯𝙖𝙢𝙞𝙚𝙣𝙩𝙤, 𝙩𝙚 𝙡𝙡𝙚𝙫𝙖𝙨 𝙚𝙡 𝙥𝙧𝙚𝙘𝙞𝙤 𝙙𝙚 𝙡𝙖 𝙚𝙣𝙩𝙧𝙖𝙙𝙖 𝙙𝙚 𝙡𝙖 𝙢𝙚𝙨𝙖", font=estilo3).pack()
        sexto_entrada = Label(marco_der,text="- 𝙎𝙞𝙣𝙤, 𝙥𝙞𝙚𝙧𝙙𝙚𝙨 𝙡𝙤 𝙦𝙪𝙚 𝙫𝙖𝙡𝙚 𝙡𝙖 𝙚𝙣𝙩𝙧𝙖𝙙𝙖", font=estilo3).pack()
        final = Label(marco_der,text="\n𝙎𝙞 𝙚𝙣 𝙡𝙤𝙨 𝙥𝙧𝙞𝙢𝙚𝙧𝙤𝙨 𝙡𝙖𝙣𝙯𝙖𝙢𝙞𝙚𝙣𝙩𝙤𝙨 𝙨𝙖𝙘𝙖𝙨 𝙪𝙣𝙤 𝙤 𝙨𝙚𝙞𝙨, \n𝙥𝙞𝙚𝙧𝙙𝙚𝙨 𝙚𝙡 𝙥𝙧𝙚𝙘𝙞𝙤 𝙙𝙚 𝙡𝙖 𝙚𝙣𝙩𝙧𝙖𝙙𝙖", font=estilo3).pack()
        final2 = Label(marco_der,text="𝘾𝙖𝙙𝙖 𝙘𝙞𝙣𝙘𝙤 𝙧𝙤𝙣𝙙𝙖𝙨 𝙨𝙚 𝙧𝙚𝙞𝙣𝙞𝙘𝙞𝙖 𝙡𝙤 𝙦𝙪𝙚 𝙝𝙖𝙮 𝙚𝙣 𝙡𝙖 𝙢𝙚𝙨𝙖\n\n", font=estilo3).pack()

        
        
        #Esta clase re confirma que se ríe de las variables en array   
                


        ventana.mainloop()
    if __name__ == "__main__":
        Juego()
except Exception:
    print("error")
