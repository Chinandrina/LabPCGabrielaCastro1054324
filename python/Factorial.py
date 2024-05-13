print("Números Factoriales")

valor = int(input("Ingrese un numero"))
num = int(input("Ingrese un número positivo: "))

if num <= 0:
    print("Error: ingrese un número positivo")

factorial = 1
for x in range (1, num+1):
    factorial *= x
if x == num: 
    print("El factorial es de: "+str(factorial))






def sumar(num1, num2):
    Total1 = num1+num2
    return Total1

num1 = int(input("Ingrese un número:  "))
num2 = int(input("Ingrese un número:  "))

print("La suma es: "+ str(sumar(num1, num2)))


def restar(num1, num2):
    Total1 = num1-num2
    return Total1

num1 = int(input("Ingrese un número:  "))
num2 = int(input("Ingrese un número:  "))

print("La suma es: "+ str(restar(num1, num2)))


def división (num1, num2):
    Total1 = num1/num2
    return Total1

num1 = int(input("Ingrese un número:  "))
num2 = int(input("Ingrese un número:  "))

print("La suma es: "+ str(división(num1, num2)))


def multiplicar(num1, num2):
    Total1 = num1*num2
    return Total1

num1 = int(input("Ingrese un número:  "))
num2 = int(input("Ingrese un número:  "))

print("La suma es: "+ str(multiplicar(num1, num2)))


else:
    factorial = 1 
for x in range (1, num)