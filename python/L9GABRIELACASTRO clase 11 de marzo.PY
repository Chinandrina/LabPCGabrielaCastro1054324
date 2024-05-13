print("Ejercicio 1: operaciones aritméticas")

numero1 = int (input("Ingrese un número:  "))
numero2 = int (input("Ingrese un segundo número:  "))

divisionReal = numero1/numero2
divisionEntera = numero1// numero2
mod = numero1 % numero2

print(numero1, "/", numero2, "=", divisionReal) 
print(numero1, "//", numero2, "=", divisionEntera) 
print(numero1,  "%", numero2, "=", mod)


print("Ejercicio 1: operaciones aritméticas suma")

numero1 = int (input("Ingrese un número:  "))
numero2 = int (input("Ingrese un segundo número:  "))

Suma = numero1+numero2


print(numero1, "+", numero2, "=", Suma) 


print("Ejercicio 1: operaciones aritméticas resta")

numero1 = int (input("Ingrese un número:  "))
numero2 = int (input("Ingrese un segundo número:  "))

Suma = numero1-numero2


print(numero1, "-", numero2, "=", Suma) 



print("Ejercicio 1: operaciones aritméticas multiplicación")

numero1 = int (input("Ingrese un número:  "))
numero2 = int (input("Ingrese un segundo número:  "))

Suma = numero1*numero2

print(numero1, "*", numero2, "=", Suma) 




print("Ejercicio 2: operaciones booleanas")

igualdad = numero1==numero2
diferentes = numero1!= numero2
menorque = numero1 < numero2
mayorque= numero1 > numero2

print(numero1, "==", numero2, "=", igualdad)
print(numero1, "!=", numero2, "=", diferentes)
print(numero1, "<", numero2, "=", menorque)
print(numero1, ">", numero2, "=", mayorque)



print("Actividad 3")
print("Ejercicio 3: conversion")
metros1 = int(input("Ingrese Metros: "))
km= metros1 /1000
print (f"km= {km}")

metros2 = int(input("Ingresse MetrosM"))
yardas =metros2 // 0.9144
modYardas = metros2 % 0.9144
pies= modYardas // 0.3333333
print("yardas: ", yardas, "pies", pies)

