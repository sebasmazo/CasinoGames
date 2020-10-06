import tkinter as tK
from tkinter import *
import Juegos.Class_Ruleta as Ruleta
import BasesDeDatos.dbengine as db


try:
    def Juego():
        try:
            puede = [False]
            resultados = [1]
            window = Tk()
            window.title("CASINOFRESCO")
            window.geometry("1280x720")
            #Recursos
            try:
                imagen_fichas = PhotoImage(file = "pngegg1.png")
                imagen_ruleta = PhotoImage(file = "imageonline-co-transparentimage.png")    
                imagen_marca = PhotoImage(file = "marca.png")
                
            except FileNotFoundError:
                print("Imagen no encontrada")
            fondo = Label(window, image = imagen_fichas).place(x=0,y=0)
            ruleta = Label(window, image = imagen_ruleta).place(x = 840, y = 50)    #IMAGEN DE LA RULETA QUE ESTA EN DISPLAY DE LA APP
            
            marca = Label(window, image = imagen_marca).place(x=540,y=600)
            #////
            #Usuario
            usuario_actual = Label(window, text=" ")
            usuario_actual.pack()
            saldo_actual = Label(window, text = " ")
            saldo_actual.pack()
            name_user = Entry(window, width=10)
            name_user.pack()
            btn_usuario = Button(window, text="Agregar usuario", command=lambda: clicked())
            btn_usuario.pack()
            btn_jugar = Button(window, text = "Jugar ruleta", command=lambda: InitRuleta())
            btn_jugar.pack()
            estado_ruleta = Label(window, text = " ")
            estado_ruleta.pack()
            resultado_ruleta = Label(window, text = " ")
            resultado_ruleta.pack()
            #Grafica
            mostrar_grafica = Button(window, text = "Mostrar histograma", command=lambda: Grafica())
            mostrar_grafica.pack()
            def Grafica():
                db.showPlot()
            def GetSaldoUsuario(NombreUsuario):
                return int(db.actualmoney())

            def clicked():
                btn_usuario['state'] = tK.DISABLED
                res = name_user.get()
                usuario_actual.configure(text="Bienvenido, " + res)
                saldo = GetSaldoUsuario(res)
                saldo_actual.configure(text="Saldo actual de " + res + ": {}" .format(saldo))
                if saldo >= 500:
                    puede[0] = True
                    
                
            
            #///////
            
            #Inicia script de ruleta
            def InitRuleta():
                    if(puede[0] == True):
                        saldo1 = GetSaldoUsuario(name_user.get())
                        res1 = name_user.get()
                        ruleta = Ruleta.Ruleta(saldo1, res1)
                        estado_ruleta.configure(text = ruleta.EstadoRuleta())
                        resultados[0] = ruleta.JugarRuleta()
                        db.addRecord(ruleta.saldo_actual)
                        db.load()
                        db.save()
                        resultado_ruleta.configure(text = "Resultado: {} ".format(resultados[0]))
                        saldo2 = ruleta.saldo_actual
                        saldo_actual.configure(text = "Saldo restante: {}".format(saldo2))
                        if(saldo2 < 500):
                            puede[0] = False
                            estado_ruleta.configure(text = "Desactivada")
                            btn_jugar['state'] = tK.DISABLED
                    else:
                        estado_ruleta.configure(text = "Dinero insuficiente")
                        
            #/////////////
            
            
            integrantes = Label(window, text="Integrantes: Gabriel Cornejo, Sebastian Mazo, Juan Sebastian Serna", font=("Helvetica", 12)).place(x=0,y=700)
            
            window.mainloop()
            
            
                

            
        except NotImplementedError:
            print("En desarrollo")
        except InterruptedError:
            print("Error en el juego")
    if __name__ == "__main__":
        Juego()
    else:
        raise ConnectionRefusedError

except ConnectionRefusedError:
    print("Por favor inicie el juego como programa principal")

except Exception:
    print("Dinero insuficiente")
finally:
    db.save()
    print("Fin del programa")

