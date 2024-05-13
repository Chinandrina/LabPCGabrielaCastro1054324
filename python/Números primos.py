print("Número Primos")

valor = int(input("Ingrese un numero"))
contador=0

if (valor<=0):
        print("Error, número no valido")

else: 
    for i in range(1, valor+1):
        if(valor%i==0):
             contador=contador+1
    if contador==2:
         print("El número es primo")
    else:
         print("El número no es primo")