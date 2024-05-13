n= int(input("Ingrese un número mayor a 0  "))

if(n <= 0):
        print("Error, debe ser mayor a 0")

#Definición de variables
a = 0
b = 1
c = 0
i = 2
resultado = ""

if (n > 0):
    resultado = str(a)

    if(n>1) : 
        resultado += "," + str (b)

    while (i < n):
        c = a + b
        resultado += "," + str(c)
        a = b
        b = c
        i = i + 1
        #print ("Adentro ciclo:, resultado")

    print (resultado)
else:
    print(resultado)



print("Semana No. 11: Ejercicio 2")
n2 = int(input("Ingrese un número mayor a 0  "))
if(n2 <= 0):
    print("Error, debe ser mayor a 0")


#Inciso a 
resultadoA = 0
for x in range(1, n2 + 1):
    resultadoA += 1/x

print("Inciso A:" , resultadoA)