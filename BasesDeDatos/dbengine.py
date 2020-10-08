import matplotlib.pyplot as plt

mov = []
moneyrec = []
charges = []
chargemov = []

#Funcion usada para adicionar un nuevo valor al historial de dinero
def addRecord(newmoney):
    try:
        mov.append(len(mov)+1);
        moneyrec.append(newmoney);
        print("Record added succesfully!");
    except:
        print("Error addRecord");

#Funcion usada para adicionar un valor de carga
def charge(newmoney):
    try:
        addRecord(newmoney);
        charges.append(newmoney);
        chargemov.append(mov[len(mov)-1]);
        print("Charged succesfully!");
    except:
        print("Error Charge");

#Funcion usada para mostrar el histograma, unicamente con fines de testing
def showPlot():
    plt.bar(mov,moneyrec,align='center', width=.2);
    plt.xlabel('Movimiento');
    plt.ylabel('Dinero');
    plt.bar(chargemov,charges,align='center', width=.2);
    plt.show();

#Funcion para guardar los cambios, debe realizarse siempre luego de hacerle cambios a la base de datos
def save():
    try:
        file = open("moneyrec.txt", "w");
        file.write(str(moneyrec));
        file.close();
        file = open("charges.txt", "w");
        file.write(str(charges));
        file.close();
        file = open("chargemov.txt", "w");
        file.write(str(chargemov));
        file.close();
        print("Record saved succesfully!");
    except:
        print("Error Save");

#Funcion para cargar los valores guardados en los archivos a los arrays en la base de datos
def load():
    try:
        file = open("moneyrec.txt", "r");
        allnumbers = file.read().split(',');
        for i in range(len(allnumbers)):
            number = allnumbers[i].replace('[', '')
            number = number.replace(' ', '')
            number = number.replace(']', '')
            number = int(number)
            moneyrec.append(number)
            mov.append(i+1)
        file = open("charges.txt", "r");
        allnumbers = file.read().split(',');
        for i in range(len(allnumbers)):
            number = allnumbers[i].replace('[', '')
            number = number.replace(' ', '')
            number = number.replace(']', '')
            number = int(number)
            charges.append(number)
        file = open("chargemov.txt", "r");
        allnumbers = file.read().split(',');
        for i in range(len(allnumbers)):
            number = allnumbers[i].replace('[', '')
            number = number.replace(' ', '')
            number = number.replace(']', '')
            number = int(number)
            chargemov.append(number)

        print("Record loaded succesfully!");
    except:
        print("Error Load");

#Funcion para eliminar todo el contenido de la base de datos
def clear():
    try:
        moneyrec.clear();
        mov.clear();
        charges.clear();
        chargemov.clear();
        print("Record cleared succesfully!");
    except:
        print("Error Clear");

#Funcion que retorna el ultimo valor de la base de datos (Saldo Actual)
def actualmoney():
    try:
        return moneyrec[len(moneyrec) -1];
    except:
        print("Error actualmoney()");
    
    finally:
        db.save()
