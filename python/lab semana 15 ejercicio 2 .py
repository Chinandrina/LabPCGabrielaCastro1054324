x=0
y=0

def MoverPosicion(cantX, cantY):
    global x, y 
    x += cantX
    y += cantY

opcion="a"
while(opcion != "e"):
    print("Menú")
    print("a. Sube", "b. Baja", "c. Izquierda", "d. Derecha", "e. Salir", sep= "\t\n")
    opcion= input("Ingrese su opción:  ")

    match opcion:
        case "a":
            MoverPosicion(0,1)
        case "b":
            MoverPosicion(0,-1)
        case "c":
            MoverPosicion(-1,0)
        case "d":
            MoverPosicion(1,0)
        case "x":
            x=0
            y=0

    print(f"La posición actual es: [{x}][{y}]")y

print("Actividad No. 1")

def triangulo (base, altura):
    calculo1 = base * altura
    area = calculo1 / 2
    return area

def rectangulo (base, altura):
    area2 = base * altura
    return area2

def cuadrado (lado):
    area4 = lado**2

def circulo (radio):
    pi = 3.14159
    radio1 = radio**2
    area3 = radio1 * pi
    return area3

print("Menú:", 
"a. área de un circulo", 
"b. área de un tringulo", 
"c. área de un cuadrado",
"d. área de un rectangulo",
sep = "\n")

opcion = input("Ingrese su opción: ")

match opcion:

    case "a":
        numero1 = int(input("Ingrese el radio: "))

        print("El área del circulo es de: " + str(circulo(numero1)))

    case "b":
        numero1 = int(input("Ingrese la base: "))
        numero2 = int(input("Ingrese la altura: "))
    
        print("El área del triangulo es de: " + str(triangulo(numero1, numero2)))

    case "c":
        numero1 = int(input("Ingrese el lado: "))
           
        print("El área del cuadrado es de: " + str(cuadrado(numero1)))
    
    case "d":
        numero1 = int(input("Ingrese la base: "))
        numero2 = int(input("Ingrese la altura: "))
    
        print("La sumatoria es de: " + str(rectangulo(numero1, numero2)))

    case _:
        print("Opción no válida, ingresa una del menú")