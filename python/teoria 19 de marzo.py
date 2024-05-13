import math

monto=int(input("Ingrese el valor de su cuota: "))

if (monto<400): 
     print("No hay descuento")

elif (monto>400 or monto>1000):
    print("Se aplica un descuento del 7%.")

monto= float(monto)
D1= monto*0.07
print(f"El valor del descuento del 7% es: {D1:.2f}")

if (monto<1000 and monto>5000):
    print("Se aplica un descuento del 10%.")

monto= float(monto)
D2= monto*0.10
print(f"El valor del descuento del 10% es: {D1:.2f}")

elif (monto<5000 or monto>1000):
    print("Se aplica un descuento del 7%.")