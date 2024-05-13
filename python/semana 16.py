import random

print("Semana No. 16: Ejercicio 1")

list=[]

for x in range(10):
    list.append(random.randint(0,10))

opcion = "a"

while (opcion != "e"):
    print("Menú")
    print("a. Mostrar números","b. Promedio","c. Longitud", "d. Posicion pares e impares","e. Salir")
    opcion = input ("ingrese su opción:  ")

    match opcion: 
        case "a": #opción mostrar numeros
            for x in range(len(list)):
                print (f"No.{x}: {list[x]}")
        case "b": 
            print("PROMEDIO")
            sumatoria = 0
            for x in range(len(list)):
                sumatoria += list [x]
            promedio = sumatoria / len(list)
            print(f"----Promedio: {promedio}")

        case "c":
            print("Longitud")
        case "d":
            print("Pares e impares")

print("Semana No. 12: Ejercicio 2")

cantfilas= int(input("Ingrese la cantidad de filas"))
cantcols= int(input("Ingrese la cantidad de columnas"))

matriz = [[0 for x in range (cantcols)]for y in range(cantfilas)]
mayor = 0

for x filas in range (cantfilas):
    for x Cols in range(cantcols):
        matriz [xfilas][xcols] = random.randint(0,1000)

        #Comparacion Mayor
        if (matriz[xfilas][xcols]> mayor):
            mayor = matriz [xfilas][xcols]

print(matriz)
print(f"El numero mayor es:  ")


import random

print("Semana No. 16: Ejercicio 1")

lista = []

for x in range(10):
    lista.append(random.randint(0,10))

opcion = "a"

while opcion != "e":
    print("Menú: ")
    print("a. mostrar números", "b. promedio", "c. longitud", "d. Posicion pares e impares", "e. salir", sep = "\n")
    
    opcion = input("Ingrese su opción: ")

    match opcion:
        case "a": 
            for x in range(len(lista)):
                print(f"No. {x}: {lista[x]}")
        
        case "b":
            print("PROMEDIO")
            sumatoria = 0
            for x in range(len(lista)):
                sumatoria += lista[x]
            promedio = sumatoria / len(lista)

            print(f"Promedio: {promedio}")

        case "c": 
            print(len(lista))

        case "d":
            suma_par = 0
            suma_impar = 0
            for x in range(len(lista)):
                if x % 2 == 0:
                    suma_par += lista[x]
                else:
                    suma_impar += lista[x]
                
print("Ejercicio 2")

filas = int(input("Ingrese la cantidad de filas: "))
columnas = int(input("Ingrese la cantidad de columnas: "))

matriz = [[0 for y in range(columnas)] for z in range(filas)]

mayor = 0
menor = 1001
pares = 0
impares = 0
for xfilas in range (filas):
    for xcolumnas in range (columnas):
        matriz[xfilas][xcolumnas] = random.randint(0, 1000)
        numero = matriz[xfilas][xcolumnas]
        numero2 = matriz[xfilas][xcolumnas]

        if matriz[xfilas][xcolumnas] > mayor:
            mayor = matriz[xfilas][xcolumnas]
        
        if matriz[xfilas][xcolumnas] < menor:
            menor = matriz[xfilas][xcolumnas]

        if numero % 2 == 0:
            pares += 1
        else: 
            impares += 1

print(matriz)
print(f"El numero mayor es: {mayor}")

print(matriz)
print(f"El numero menor es: {menor}")

print(matriz)
print("La cantidad de numeros pares es de: ", str(pares))

print(matriz)
print("La cantidad de numeros impares es de: ", str(impares))