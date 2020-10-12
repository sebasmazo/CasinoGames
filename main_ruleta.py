import tkinter as tK
from tkinter import *
import Juegos.Class_Ruleta as Ruleta
import dbengine as db


try:
    
    def Juego():
        try:
            
            puede = [False]
            resultados = [1]
            movimientos = [0]
            window = Tk()
            window.title("CASINOFRESCO")
            window.geometry("1280x720")
            
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
            movimiento_actual = Label(window, text = " Movimiento actual = {}".format(movimientos[0]))
            movimiento_actual.pack()
            resultado_ruleta.pack()
            #Grafica
            mostrar_grafica = Button(window, text = "Mostrar histograma", command=lambda: Grafica())
            mostrar_grafica.pack()
            def Grafica():
                db.showPlot()
                
            def GetSaldoUsuario(NombreUsuario):
                #Aqui va la conexion con el saldo de la base de datos
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
                        movimientos[0] += 1
                        movimiento_actual.configure(text = "Movimiento actual = {}".format(movimientos[0]))
                        saldo1 = GetSaldoUsuario(name_user.get())
                        res1 = name_user.get()
                        ruleta = Ruleta.Ruleta(saldo1, res1)
                        estado_ruleta.configure(text = ruleta.EstadoRuleta())
                        resultados[0] = ruleta.JugarRuleta()
                        db.addRecord(ruleta.saldo_actual)
                        db.load()
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
    Juego()

except Exception:
    print("Dinero insuficiente")
finally:
    db.save()
    print("Fin del programa")

