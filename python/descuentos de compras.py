monto = int(input("Ingrese su monto de compra"))
descuento= 0

if(monto<0):
    print ("Error, monto no válido")
else:
    if(monto<=400):
        descuento=0
    elif 400< monto<=1000:
        descuento = 0.07
    elif 1000< monto<=5000:
        descuento = 0.1
    elif 5000< monto<=15000:    
        descuento = 0.15
    else:
        descuento = 0.25 
    res= input("Tiene un código de descuento (s/n)")
    if(res=="si") or res=="si" or res == "s":
        descuento=descuento+0.05

    monto = monto*(1-descuento)
    print("El precio final es"+ str (monto))
    print("Sel le aplica escuento de ", str(descuento))