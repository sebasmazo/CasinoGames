import numpy.random as rnd
class Ruleta():
    estado_ruleta = False
    def __init__(self, saldo_actual, nombrejugador):
        if(saldo_actual > 500):
            self.saldo_actual = saldo_actual
            self.nombrejugador = nombrejugador
            self.estado_ruleta = True
            
    def EstadoRuleta(self):
        if(self.estado_ruleta == True):
            return "Ruleta activada"
        else:
            return "Dinero insuficiente"
    def JugarRuleta(self):
        if(self.saldo_actual >= 500):
            u = rnd.rand()
            if(u <= 0.01):
                self.saldo_actual += 1000000
                return  1000000
            elif(u <= 0.05):
                JugarRuleta()
            elif(u <= 0.11):
                self.saldo_actual += 500000
                return  500000
            elif(u <= 0.19):
                self.saldo_actual += 250000
                return  250000
            elif(u <= 0.28):
                self.saldo_actual += 200000
                return  200000
            elif(u <= 0.38):
                self.saldo_actual -= 1000
                return  -1000
            elif(u <= 0.51):
                self.saldo_actual -= 250000
                return  -250000
            elif(u <= 0.66):
                self.saldo_actual -= 120000
                return  -120000
            elif(u <= 0.80):
                self.saldo_actual -= 500000
                return  -500000
            elif(u <= 1):
                self.saldo_actual -= 300000
                return  -300000
        else:
            self.estado_ruleta = False
            raise Exception
