import random 

secreto = random.randint(1,100)
Ganador = False 
turnos = 0
Jugador1 = 0
Jugador2 = 0
TurnosJug1= 0
TurnosJug2= 0

Jugador1 = input("Ingresa tu nombre: ")
Jugador2 = input("Ingresa tu nombre: ")
while not Ganador:
    ingresado = int(input("Ingrese un número (1-100)"))
    turnos=turnos+ 1
    if(turnos%2==0):
        TurnosJug2=TurnosJug2+1 
    else:
        TurnosJug1= TurnosJug1+1
    if ingresado == secreto:
        print ("Ganaste!!! Adivinaste el número")
        Ganador = True 

        if(turnos%2==0):
            print("El ganador es" + jugador2)
            print("Tomó" + str(TurnosJug1)+ "turnos")
        else:
            print("El ganador es " + Jugador1)
            print("tomó "+ str(TurnosJug1)+ "turnos")
    else:
        print("No adivinaste, gracias por participar")
        if ingresado < secreto:
            print("El número ingresado es menor")

        else:
            print("El número ingresado es mayor")
