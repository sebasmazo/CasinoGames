import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
import Juegos.Class_Guayabita as Guayaba
import dbengine as db


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
                    return int(db.actualmoney())
            
        def GetValorMesa(x):
            if(x==1):
                valor_mesa = 10000
            return valor_mesa

        
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
            if(btn_usuario['state'] == tk.NORMAL):
                btn_usuario['state'] = tk.DISABLED
                dado_1_boton['state'] = tk.NORMAL
            else:
                btn_usuario['state'] = tk.NORMAL
                
                dado_1_boton['state'] = tk.DISABLED

            
            

        btn_usuario = Button(marco, text="Agregar usuario", command=clicked)
        btn_usuario.pack()
        #INGRESO USUARIO
        
        #MESA              
        marco_mesa = Frame(ventana,relief=RAISED, borderwidth=3)
        marco_mesa.place(x=200,y=580)
        estilo_mesa = tkFont.Font(size=40)
        huecoxd = Label(marco_mesa,text="\t\t\t\t\t\t",font="estilo_mesa")
        huecoxd.pack()
        txt_mesa = Label(marco_mesa, text="Resultados",font=estilo_mesa)
        txt_mesa.pack()
        
        valor_entrada = 10000
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
            saldote = texto_saldo_num["text"]
            #val_mesa = GetValorMesa(1)
            
            if(saldote >= 10000):
                saldote = saldote - valor_entrada
                db.addRecord(saldote)
                db.save()
                db.load()
                texto_saldo_num["text"] = saldote

                #val_mesa = val_mesa + valor_entrada
                #txt_saldo_mesa["text"] = val_mesa 

                ans = Guayaba.Guayabita.PrimerLanzamiento()
                dado_1_ans["text"] = ans

                if(ans == 1):
                    img_1["image"] = img_dado_1
                    saldote = saldote - valor_entrada
                    db.addRecord(saldote)
                    db.save()
                    db.load()
                    texto_saldo_num["text"] = saldote
                    txt_mesa["text"] = "Perdiste 10000"
                    #val_mesa = val_mesa + valor_entrada
                    #txt_saldo_mesa["text"] = val_mesa

                elif(ans == 2):
                    img_1["image"] = img_dado_2
                    var_no_spam[0] = False
                    dado_1_boton['state'] = tk.DISABLED
                    dado_2_boton['state'] = tk.NORMAL
                            
                elif(ans == 3):
                    img_1["image"] = img_dado_3
                    var_no_spam[0] = False
                    dado_1_boton['state'] = tk.DISABLED
                    dado_2_boton['state'] = tk.NORMAL               
                    
                elif(ans == 4):
                    img_1["image"] = img_dado_4
                    var_no_spam[0] = False
                    dado_1_boton['state'] = tk.DISABLED     
                    dado_2_boton['state'] = tk.NORMAL            
                    
                elif(ans == 5):
                    img_1["image"] = img_dado_5
                    var_no_spam[0] = False
                    dado_1_boton['state'] = tk.DISABLED
                    dado_2_boton['state'] = tk.NORMAL
                                
                elif(ans == 6):
                    img_1["image"] = img_dado_6
                    saldote = saldote - valor_entrada
                    db.addRecord(saldote)
                    db.load()
                    db.save()
                    texto_saldo_num["text"] = saldote
                    txt_mesa["text"] = "Perdiste 10000"
                    #val_mesa = val_mesa + valor_entrada
                    #txt_saldo_mesa["text"] = val_mesa

        dado_1_boton = Button(marco_dado_1, text="Lanza el primer dado", state=tk.DISABLED, command=dado_1)
        dado_1_boton.pack()
        #DADO 1

        #ELECCION
        marco_eleccion = Frame(ventana, relief=RAISED, borderwidth=3)
        marco_eleccion.place(x=300, y=200)

        elecciones = ['ALTO', 'MEDIO', 'BAJO']
        variable = StringVar(marco_eleccion)
        variable.set('ALTO')

        tit_eleccion = Label(marco_eleccion, text="Elija una opción antes de tirar el segundo dado")
        tit_eleccion.pack()

        panel_eleccion = OptionMenu(marco_eleccion, variable, *elecciones)
        panel_eleccion.pack()

        lab_prueba = Label(marco_eleccion, text="")         
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
            dado_2_boton['state'] = tk.DISABLED
            saldito = texto_saldo_num["text"]
            v_dado_1 = dado_1_ans["text"]

            ans_2 = Guayaba.Guayabita.SegundoLanzamiento()
            dado_2_ans["text"] = ans_2

            val_eleccion = variable.get()

            if(val_eleccion == elecciones[0]):

                if(ans_2 > v_dado_1):
                    saldito = saldito + 50000
                    db.addRecord(saldito)
                    db.save()
                    db.load()
                    texto_saldo_num["text"] = saldito
                    txt_mesa["text"] = "GANASTE 40000"

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

                elif(ans_2 <= v_dado_1):
                    saldito = saldito - 80000
                    db.addRecord(saldito)
                    db.save()
                    db.load()
                    texto_saldo_num["text"] = saldito
                    txt_mesa["text"] = "PERDISTE 80000"

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

            elif(val_eleccion == elecciones[1]):

                if(ans_2 > v_dado_1):
                    saldito = saldito + 30000
                    db.addRecord(saldito)
                    db.save()
                    db.load()
                    texto_saldo_num["text"] = saldito
                    txt_mesa["text"] = "GANASTE 20000"

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

                elif(ans_2 <= v_dado_1):

                    saldito = saldito - 40000
                    db.addRecord(saldito)
                    db.save()
                    db.load()
                    texto_saldo_num["text"] = saldito
                    txt_mesa["text"] = "PERDISTE 40000"

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

            elif(val_eleccion == elecciones[2]):

                if(ans_2 > v_dado_1):
                    saldito = saldito + 20000
                    db.addRecord(saldito)
                    db.save()
                    db.load()
                    texto_saldo_num["text"] = saldito
                    txt_mesa["text"] = "GANASTE 10000"

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

                elif(ans_2 <= v_dado_1):

                    saldito = saldito - 20000
                    db.addRecord(saldito)
                    db.save()
                    db.load()
                    texto_saldo_num["text"] = saldito
                    txt_mesa["text"] = "PERDISTE 20000"

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
            
        dado_2_boton = Button(marco_dado_2, text="Lanza el segundo dado",state=tk.DISABLED, command=dado_2)
        dado_2_boton.pack()
        #DADO 2

        #JUGAR DE NUEVO
        def limpiar():      #Dejemos ese boton siempre activo pero que solo funcione cuando haya contenido 
            if(txt_mesa != "RESULTADOS"):
                img_1["image"] = img_dado_0
                img_2["image"] = img_dado_0
                dado_1_ans["text"] = ""
                dado_2_ans["text"] = ""
                dado_1_boton['state'] = tk.NORMAL
            else:
                txt_mesa["text"] = "Termine la ronda"

        estilo_btn_mesa = tkFont.Font(size=15)
        btn_limpiar = Button(marco_mesa, text="Volver a jugar", font=estilo_btn_mesa, command=limpiar)
        btn_limpiar.pack()
        #JUGAR DE NUEVO
        
        #INSTRUCCIONES
        marco_der = Frame(ventana, width = 430, height=720, cursor="dotbox")
        marco_der.pack(side=RIGHT)
        estilo2 = tkFont.Font(size=30)
        titulo_inst = Label(marco_der,text="¿𝘾𝙤𝙢𝙤 𝙟𝙪𝙜𝙖𝙧 𝙜𝙪𝙖𝙮𝙖𝙗𝙞𝙩𝙖?", font=estilo2)
        titulo_inst.pack()
        estilo3=tkFont.Font(size=15)
        primero = Label(marco_der,text="\n1. 𝙄𝙣𝙜𝙧𝙚𝙨𝙖𝙨 𝙩𝙪 𝙪𝙨𝙪𝙖𝙧𝙞𝙤", font=estilo3).pack()
        segundo = Label(marco_der,text="\n\n2. 𝙏𝙞𝙧𝙖𝙨 𝙪𝙣 𝙙𝙖𝙙𝙤, 𝙥𝙖𝙜𝙖𝙣𝙙𝙤 𝙡𝙖 𝙚𝙣𝙩𝙧𝙖𝙙𝙖", font=estilo3).pack()
        tercero = Label(marco_der,text="\n\n3. 𝘿𝙚𝙘𝙞𝙙𝙚𝙨 𝙚𝙡 𝙣𝙞𝙫𝙚𝙡 𝙙𝙚 𝙧𝙞𝙚𝙨𝙜𝙤, 𝙢𝙞𝙚𝙣𝙩𝙧𝙖𝙨 𝙢𝙖𝙨 𝙖𝙡𝙩𝙤 \n𝙢𝙖𝙨 𝙥𝙪𝙚𝙙𝙚𝙨 𝙜𝙖𝙣𝙖𝙧 𝙥𝙚𝙧𝙤 𝙩𝙖𝙢𝙗𝙞𝙚𝙣 𝙥𝙪𝙚𝙙𝙚𝙨 𝙥𝙚𝙧𝙙𝙚𝙧 𝙢𝙖𝙨", font=estilo3).pack()
        cuarto =  Label(marco_der,text="\n\n4. 𝙑𝙪𝙚𝙡𝙫𝙚𝙨 𝙖 𝙩𝙞𝙧𝙖𝙧 𝙚𝙡 𝙙𝙖𝙙𝙤", font=estilo3).pack()
        #todo =  Label(marco_der,text="\n𝙎𝙞 𝙛𝙪𝙞𝙨𝙩𝙚 𝙥𝙤𝙧 𝙩𝙤𝙙𝙤", font=estilo3).pack()
        quinto_todo = Label(marco_der,text="\n\n5. 𝙎𝙞 𝙨𝙖𝙘𝙖𝙨 𝙪𝙣 𝙣𝙪𝙢𝙚𝙧𝙤 𝙢𝙖𝙮𝙤𝙧 𝙦𝙪𝙚 𝙚𝙡 𝙙𝙚 𝙩𝙪 𝙥𝙧𝙞𝙢𝙚𝙧 \n𝙡𝙖𝙣𝙯𝙖𝙢𝙞𝙚𝙣𝙩𝙤, 𝙜𝙖𝙣𝙖𝙨 𝙙𝙞𝙣𝙚𝙧𝙤", font=estilo3).pack()
        sexto_todo = Label(marco_der,text="\n\n6. 𝙎𝙞𝙣𝙤, 𝙥𝙞𝙚𝙧𝙙𝙚𝙨 𝙙𝙞𝙣𝙚𝙧𝙤", font=estilo3).pack()
        #entrada =  Label(marco_der,text="\n\n𝙎𝙞 𝙛𝙪𝙞𝙨𝙩𝙚 𝙥𝙤𝙧 𝙡𝙤 𝙙𝙚 𝙡𝙖 𝙚𝙣𝙩𝙧𝙖𝙙𝙖", font=estilo3).pack()
        final = Label(marco_der,text="\n\n𝙎𝙞 𝙚𝙣 𝙡𝙤𝙨 𝙥𝙧𝙞𝙢𝙚𝙧𝙤𝙨 𝙡𝙖𝙣𝙯𝙖𝙢𝙞𝙚𝙣𝙩𝙤𝙨 𝙨𝙖𝙘𝙖𝙨 𝙪𝙣𝙤 𝙤 𝙨𝙚𝙞𝙨, \n𝙥𝙞𝙚𝙧𝙙𝙚𝙨 𝙚𝙡 𝙥𝙧𝙚𝙘𝙞𝙤 𝙙𝙚 𝙡𝙖 𝙚𝙣𝙩𝙧𝙖𝙙𝙖", font=estilo3).pack()
        otro = Label(marco_der,text="\n\n𝘾𝙤𝙣 𝙚𝙡 𝙗𝙤𝙩𝙤𝙣 𝙙𝙚 𝙖𝙗𝙖𝙟𝙤 𝙥𝙪𝙚𝙙𝙚𝙨 𝙧𝙚𝙞𝙣𝙞𝙘𝙞𝙖𝙧 𝙚𝙡 𝙟𝙪𝙚𝙜𝙤\n", font=estilo3).pack()
        
        #INSTRUCCIONES
    


        ventana.mainloop()
    if __name__ == "__main__":
        Juego()
except Exception:
    print("error")
finally:
    db.save()
    print("Fin del programa")
