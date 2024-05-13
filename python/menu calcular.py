def sumar(num1, num2):
    total = num1 + num2
    return total

def resta(num1, num2):
    total = num1 - num2
    return total

def dividir(num1, num2):
    if num2 == 0:
        return ("Error: no se puede dividir entre cero")
    else:
        total = num1 / num2
        return total

def multiplicar(num1, num2):
    total = num1 * num2
    return total

def raiz(num3):
    if num3 < 0:
        return ("Error, ingrese un número positivo")
    else:
        total = num3**0.5
        return total

def potencia(num4, num5):
    total = num4**num5
    return total

def factorial(num6):
    facto = 1
    for x in range (1, num6+1):
        facto *= x 
    if x == num6:
        return facto

print("Menú", 
"1. sumatoria", 
"2. resta", 
"3. multiplicar",
"4. división",
"5. raíz",
"6. potencia",
"7. factorial",
sep = "\n")

opcion = input("Ingrese su opción: ")

match opcion:
    case "1":
        numero1 = int(input("Ingrese un número: "))
        numero2 = int(input("Ingrese un número: "))
    
        print("La sumatoria es de: " + str(sumar(numero1, numero2)))
    
    case "2":
        numero1 = int(input("Ingrese un número: "))
        numero2 = int(input("Ingrese un número: "))

        print("La resta es de: " + str(resta(numero1, numero2)))
    
    case "3":
        numero1 = int(input("Ingrese un número: "))
        numero2 = int(input("Ingrese un número: "))

        print("La multiplicación es de: " + str(multiplicar(numero1, numero2)))

    case "4":
        numero1 = int(input("Ingrese un número: "))
        numero2 = int(input("Ingrese un número: "))

        print("La división es de: " + str(dividir(numero1, numero2)))

    case "5":
        numero3 = int(input("Ingrese un número positivo: "))

        print("La raíz es de: " + str(raiz(numero3)))

    case "6":
        numero4 = int(input("Ingrese un número que será la base: "))
        numero5 = int(input("Ingrese un número que será el exponente: "))

        print("La potencia es de: " + str(potencia(numero4, numero5)))

    case "7":
        numero6 = int(input("Ingrese un número: "))

        print("El factorial es: " + str(factorial(numero6)))
        
    case _:
        print("Opción no válida, ingresa una del menú")