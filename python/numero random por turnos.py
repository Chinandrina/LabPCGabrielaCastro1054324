import random

secreto =random.randint(1,100)
Ganador=False
Turnos=0
jugador1= input("Ingresa tu nombre")
jugador2= input("Ingresa tu nombre")

turnosjug1=0
turnosjug2=0

 
Ganador= False

while not Ganador:
    ingresado=int(input("Ingrese un número (1, 100)"))
    Turnos=Turnos+1
    if (Turnos%2==0):
        turnosjug2=turnosjug2+1
    else:
        turnosjug1=turnosjug1+1


    if ingresado == secreto:
        print("Ganaste :)")
        Ganador = True
        print("Tomó"+str(Turnos)+ "turnos")

        if(Turnos%2==0):
            print("El ganador es "+jugador2)
            print("Tomó "+ str(turnosjug2)+"turnos")
        else:
            print("El ganador es "+ jugador1)
            print("Tomó "+ str(turnosjug1)+"turnos")

    else:
        print("No ganaste :(")
        if ingresado< secreto:
            print("El número ingresado es menor")
        else:
            print("El número ingresado es mayor")