print("Infrese el tipo de envio")
tipoenvio= int(input("1. Motocicleta 2. Vehículo  "))

if tipoenvio!= 1 and tipoenvio!= 2:
    print("Error, tipo de de envio no valido") 
else:
    km = int(input("Ingrese el número de kilómetros a recorrer"))
    if(km<0):
        print("Error, distancia no valida")
    else:
        if(tipoenvio == 1):
            costofijo= 10
            if (km<5):
                CostoVariable= km*3
            elif(km<10):
                CostoVariable=km*2.5
            else:
                CostoVariable=2.0
        if tipoenvio==2:
            costofijo=20
            if(km<5):
                CostoVariable=km*6
            elif (km<10):
                CostoVariable=km*4
    costototal= costofijo + CostoVariable
    print ("El total de su envio es"+ str(costototal  ))