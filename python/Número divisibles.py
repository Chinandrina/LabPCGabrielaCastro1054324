print("Números por los que es divisible")
número = int(input("Ingrese un numero:  "))
contador=0
turno1 = 0
turno2 = 0
if (número<=0):
    print("Error, número no valido")

else:
    turno1 = 0
    suma = 0
    for x in range (1, número):
        if número % x == 0:
            suma += x
    turno2 = 0
    if suma == número:
        print("El número es perfecto")      
    else: 
        print("No es un número perfecto")
        if turno1 == turno2:
            print("Son números amigos")