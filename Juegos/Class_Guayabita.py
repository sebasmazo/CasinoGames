#CORNEJO
#Hola lic mazo, cuando leas esto seguramente tengas que organizar mi codigo tkm

#Esta clase se rie de las variables con array de mazo

import numpy.random as rnd
class Guayabita:
    #Metodo para el lanzamiento del primer dado 
    def PrimerLanzamiento(self):
        dado_1 = rnd.rand()                                                         #Genera un num aleatorio del 0 al 1
        self.valor_dado_1 = 0                                                       #Variable que almacena la cara en la que cae el dado 1
        #Condicionales para asignar el valor del dado 1
        if(dado_1 <= 1/6):
            self.valor_dado_1 = 1
        elif(dado_1 <= 2/6):
            self.valor_dado_1 = 2
        elif(dado_1 <= 3/6):
            self.valor_dado_1 = 3
        elif(dado_1 <= 4/6):
            self.valor_dado_1 = 4
        elif(dado_1 <= 5/6):
            self.valor_dado_1 = 5
        else:
            self.valor_dado_1 = 6
        print("El resultado del dado 1 fue {}".format(self.valor_dado_1))
    #Metodo para el lanzamiento del dado 2
    def SegundoLanzamiento(self):  
        #Si el valor del dado 1 es igual a 1 o 6, no se ejecuta el resto del codigo porque ya no se lanza el 2do dado
        if(self.valor_dado_1 == 1 or self.valor_dado_1 == 6):
            print("Perdio el valor de la entrada")
        #De otra forma, se hace el lanzamiento del segundo dado      
        else:
            #Entrada de datos para definir si va a por todo o si va solo a por el valor de la entrada
            va_por_todo = input("Ingrese el num 1 si va a por todo, ingrese cualquier otra cosa si solo va por el valor de la entrada: \n")
            if(int(va_por_todo) == 1):
                va_por_todo = True
            else:
                va_por_todo = False
            print(bool(va_por_todo))                                                #para verificar el valor de la variable (verdadero o falso)
            dado_2 = rnd.rand()                                                     #Genera un num alatorio del 0 al 1 
            valor_dado_2 = 0                                                        #Variable que almacena la cara en la que cae el dado 2
            #Condicionales para asignar el valor del dado 2
            if(dado_2 <= 1/6):
                valor_dado_2 = 1
            elif(dado_2 <= 2/6):
                valor_dado_2 = 2
            elif(dado_2 <= 3/6):
                valor_dado_2 = 3
            elif(dado_2 <= 4/6):
                valor_dado_2 = 4
            elif(dado_2 <= 5/6):
                valor_dado_2 = 5
            else:
                valor_dado_2 = 6
            print("El resultado del dado 2 fue {}".format(valor_dado_2))
            #Si el valor del dado es 1 o 6  no se tiene que ejecutar lo otro 
            if(self.valor_dado_1 == 1 or self.valor_dado_1 == 6):
                print("Perdio el valor de la entrada")
            #De otra forma, se ejecuta este codigo prron
            else:
                #Si la variable booleana es verdadera, va a por todo lo que hay en la mesa 
                if(bool(va_por_todo) == True):
                    #Si saca un num mayor en el 2do lanzamiento, gana todo lo que hay en la mesa 
                    if(valor_dado_2 > self.valor_dado_1):
                        print("Ganaste todo lo que hay en la mesa")
                    #De otro modo, si en la mesa hay 50, debe poner otros 50
                    else:
                        print("Perdiste la cantidad total de lo que hay en la mesa")
                #Si no va a por todo, va solo por el valor de la entrada 
                else:
                    #Si saca un num mayor en el 2do lanzamiento, gana lo que vale la entrada
                    if(valor_dado_2 > self.valor_dado_1):
                        print("Ganaste el valor de la entrada")
                    #De otro modo, debe poner en la mesa el valor de la entrada (pierde)
                    else:
                        print("Perdiste el valor de la entrada")
               
#Esta clase re confirma que se ríe e las variables en array     
g = Guayabita()
g.PrimerLanzamiento()
g.SegundoLanzamiento()