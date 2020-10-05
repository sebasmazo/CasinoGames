import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
import Juegos.Class_Guayabita as Guayaba

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
        
        #TITULO
        estilo = tkFont.Font(size=50)
        titulo = Label(ventana, text="🅖🅤🅐🅨🅐🅑🅘🅣🅐", font=estilo, relief=RAISED, borderwidth=3).place(x=200,y=25)
        #TITULO

        #INGRESO USUARIO 
        marco = Frame(ventana, relief=RAISED, borderwidth=3)
        marco.place(x=35, y=30)
        usuario_actual = Label(marco, text="Ingrese su nombre")#.grid(row=0)
        usuario_actual.pack()
        name_user = Entry(marco)#.grid(row=1, column=1)
        name_user.pack()

        #SALDO
        marco_saldo = Frame(ventana, relief = RAISED, borderwidth=3)
        marco_saldo.place(x=665,y=30)
        texto_saldo = Label(marco_saldo, text="Su saldo actual es de:")
        texto_saldo.pack()
        estilo_saldo = tkFont.Font(size=15)
        texto_saldo_num = Label(marco_saldo, text="",font=estilo_saldo)
        texto_saldo_num.pack()
        #SALDO

        def clicked():
            usuario = name_user.get()
            usuario_actual.configure(text="Bienvenid@, " + usuario)
            saldito = GetSaldoUsuario(1)  
            texto_saldo_num["text"] = saldito
            

        btn_usuario = Button(marco, text="Agregar usuario", command=clicked)
        btn_usuario.pack()
        #INGRESO USUARIO
        
        #MESA
        marco_mesa = Frame(ventana,relief=RAISED, borderwidth=3)
        marco_mesa.place(x=320,y=575)
        estilo_mesa = tkFont.Font(size=20)
        txt_mesa = Label(marco_mesa, text="En la mesa hay:",font=estilo_mesa)
        txt_mesa.pack()
        valor_inicial_mesa = 10000
        valor_entrada = 10000
        txt_saldo_mesa = Label(marco_mesa,text=valor_inicial_mesa, font=estilo_mesa)
        txt_saldo_mesa.pack()
        
  
        #MESA

        #IMG DADO 1
        marco_img_1 = Frame(ventana, width=250, height=250)
        marco_img_1.place(x=35, y=300)
        img_dado_0 = PhotoImage(file="dado_0.png")
        img_dado_1 = PhotoImage(file="dado_1.png")
        img_dado_2 = PhotoImage(file="dado_2.png")
        img_dado_3 = PhotoImage(file="dado_3.png")
        img_dado_4 = PhotoImage(file="dado_4.png")
        img_dado_5 = PhotoImage(file="dado_5.png")
        img_dado_6 = PhotoImage(file="dado_6.png")
        img_1 = Label(marco_img_1, image=img_dado_0)
        img_1.pack()
        #IMG DADO 1

        #DADO 1
        marco_dado_1 = Frame(ventana, relief=RAISED, borderwidth=3)
        marco_dado_1.place(x=100, y=200)
        dado_1_titulo = Label(marco_dado_1, text="Dado 1")
        dado_1_titulo.pack()
        dado_1_ans = Label(marco_dado_1, text="")
        dado_1_ans.pack()

        var_no_spam = [True, True]


        def dado_1():
            lbl_saldote = texto_saldo_num["text"]
            saldote = GetSaldoUsuario(1)
              
            if(lbl_saldote == ""):
                dado_1_ans["text"] = "Ingresa tu usuario"
            elif(saldote<10000):
                dado_1_ans["text"] = "Saldo insuficiente"
            
            elif(var_no_spam[0] == True):
                txt_saldo_mesa["text"] = valor_entrada + valor_inicial_mesa
                ans = Guayaba.Guayabita.PrimerLanzamiento()  
                       
                dado_1_ans["text"] = ans
                if(ans == 1):
                    img_1["image"] = img_dado_1
                elif(ans == 2):
                    img_1["image"] = img_dado_2
                elif(ans == 3):
                    img_1["image"] = img_dado_3
                elif(ans == 4):
                    img_1["image"] = img_dado_4
                elif(ans == 5):
                    img_1["image"] = img_dado_5
                elif(ans == 6):
                    img_1["image"] = img_dado_6
                var_no_spam[0] = False
            
            elif(var_no_spam[0] == False):
                dado_1_ans["text"] == "Tire el otro dado"

        dado_1_boton = Button(marco_dado_1, text="Lanza el primer dado", command=dado_1)
        dado_1_boton.pack()
        #DADO 1

        #ELECCION
        marco_eleccion = Frame(ventana, relief=RAISED, borderwidth=3)
        marco_eleccion.place(x=300, y=200)

        elecciones = ['Voy por todo', 'Solo voy por la entrada']
        variable = StringVar(marco_eleccion)
        variable.set('Voy por todo')

        tit_eleccion = Label(marco_eleccion, text="Elija una opción antes de tirar el segundo dado")
        tit_eleccion.pack()

        panel_eleccion = OptionMenu(marco_eleccion, variable, *elecciones)
        panel_eleccion.pack()

        lab_prueba = Label(marco_eleccion, text="")         #Esto irá en marco resultados
        lab_prueba.pack()
        #ELECCION

        #IMG DADO 2
        marco_img_2 = Frame(ventana, width=250, height=250)
        marco_img_2.place(x=565, y=300)
        img_2 = Label(marco_img_2, image=img_dado_0)
        img_2.pack()
        #IMG DADO 2

        #DADO 2
        marco_dado_2 = Frame(ventana,width=250,height=250, relief=RAISED, borderwidth=3)
        marco_dado_2.place(x=630, y=200)
        dado_2_titulo = Label(marco_dado_2, text="Dado 2")
        dado_2_titulo.pack()
        dado_2_ans = Label(marco_dado_2, text="")
        dado_2_ans.pack()

        def dado_2():
            val_1 = dado_1_ans["text"]       
            if(val_1 == "" or val_1 == "Ingresa tu usuario" or val_1 == "Saldo insuficiente"):
                dado_2_ans["text"] = "Primero tire el dado 1"
            elif((int(val_1) > 1 or int(val_1) < 6) and var_no_spam[1] == True):
                val_eleccion = variable.get()
                if(val_eleccion == elecciones[0]):
                    lab_prueba["text"] = "Fuiste por todo"
                    ans_2 = Guayaba.Guayabita.SegundoLanzamiento()         
                    dado_2_ans["text"] = ans_2
                    if(ans_2 == 1):
                        img_2["image"] = img_dado_1
                    elif(ans_2 == 2):
                        img_2["image"] = img_dado_2
                    elif(ans_2 == 3):
                        img_2["image"] = img_dado_3
                    elif(ans_2 == 4):
                        img_2["image"] = img_dado_4
                    elif(ans_2 == 5):
                        img_2["image"] = img_dado_5
                    elif(ans_2 == 6):
                        img_2["image"] = img_dado_6
                    var_no_spam[1] == False
                    dado_1_ans["text"] = ""
                    
                elif(val_eleccion == elecciones[1]):
                    lab_prueba["text"] = "Fuiste solo por la entrada"
                    ans_2 = Guayaba.Guayabita.SegundoLanzamiento()         
                    dado_2_ans["text"] = ans_2
                    if(ans_2 == 1):
                        img_2["image"] = img_dado_1
                    elif(ans_2 == 2):
                        img_2["image"] = img_dado_2
                    elif(ans_2 == 3):
                        img_2["image"] = img_dado_3
                    elif(ans_2 == 4):
                        img_2["image"] = img_dado_4
                    elif(ans_2 == 5):
                        img_2["image"] = img_dado_5
                    elif(ans_2 == 6):
                        img_2["image"] = img_dado_6
                    var_no_spam[1] == False
                    dado_1_ans["text"] = ""
                    
            else:
                dado_2_ans["text"] = "Perdiste lo de la entrada"
      
        dado_2_boton = Button(marco_dado_2, text="Lanza el segundo dado", command=dado_2)
        dado_2_boton.pack()
        #DADO 2

        #LIMPIAR DADOS
        def limpiar_dados():
            valor_d2 = int(dado_2_ans["text"])
            if(valor_d2 >= 1 or valor_d2 <= 6):
                print(var_no_spam[0])
                img_1["image"] = img_dado_0
                img_2["image"] = img_dado_0
                dado_2_ans["text"] = ""
                var_no_spam[0] == True
                print(var_no_spam[0])

        
        boton_limpiar = Button(marco_mesa, text="LIMPIAR DADOS", command=limpiar_dados)
        boton_limpiar.pack()


        #LIMPIAR DADOS

        #INSTRUCCIONES
        marco_der = Frame(ventana, width = 430, height=720, cursor="dotbox")
        marco_der.pack(side=RIGHT)
        estilo2 = tkFont.Font(size=30)
        titulo_inst = Label(marco_der,text="¿𝘾𝙤𝙢𝙤 𝙟𝙪𝙜𝙖𝙧 𝙜𝙪𝙖𝙮𝙖𝙗𝙞𝙩𝙖?", font=estilo2)
        titulo_inst.pack()
        estilo3=tkFont.Font(size=15)
        primero = Label(marco_der,text="\n1. 𝙄𝙣𝙜𝙧𝙚𝙨𝙖𝙨 𝙩𝙪 𝙪𝙨𝙪𝙖𝙧𝙞𝙤", font=estilo3).pack()
        segundo = Label(marco_der,text="\n2. 𝙏𝙞𝙧𝙖𝙨 𝙪𝙣 𝙙𝙖𝙙𝙤, 𝙥𝙖𝙜𝙖𝙣𝙙𝙤 𝙡𝙖 𝙚𝙣𝙩𝙧𝙖𝙙𝙖", font=estilo3).pack()
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
        #INSTRUCCIONES
             
        #Esta clase re confirma que se ríe de las variables en array   
 
        ventana.mainloop()
    if __name__ == "__main__":
        Juego()
except Exception:
    print("error")
