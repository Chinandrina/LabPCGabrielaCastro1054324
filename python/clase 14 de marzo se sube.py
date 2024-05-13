try:
    numero = int(input("Ingrese un numero"))

    if numero == 0:
        print("El cero no es numero par ni impar")
    else: 
        if numero % 2 == 0 :
            print("El numero es par")
        else: 
            print("El numero es impar")

except ValueError:
    print("Por favor ingrese un valor valido")