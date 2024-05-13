import.math

numero=int(input("Ingrese la cantidad de números"))
list=[]
cantidad=0

numero=int(input("Ingrese la cantidad de mínima"))

while cantidad< numero:
numero2=int(input("Ingrese una edad"))
if numero2>0:
    list.append(numero2)
    cantidad=cantidad+1
else:
    print("Numero inválido")

    edades=0 
    for x in(list):
    if x >numero:

        edades +=1
        print("Las edades válidas son:", edades)
    
    list.append 