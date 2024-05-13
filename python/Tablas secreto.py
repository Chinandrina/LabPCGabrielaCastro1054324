import random 

secreto = random.randint(1,100)
Ganador = False 
turnos = 0

while not Ganador:
    ingresado = int(input("Ingrese un número (1-100)"))
    turnos += 1 
    if ingresado == secreto:
        print ("Ganaste!!! Adivinaste el número")
        Ganador = True 
        print ("Toma "+ str(turnos)+ "turnos")
    else:
        print("No adivinaste, gracias por participar")
        if ingresado < secreto:
            print("El número ingresado es menor")
        else:
            print("El número ingresado es mayor")
