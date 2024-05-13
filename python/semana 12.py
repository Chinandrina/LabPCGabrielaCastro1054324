print("Semana No. 12: Ejercicio 1")

print("Menú", "8. Sumatoria "
"b. Factorial", 
"c. Tablas de mulltiplicar",
"d. Número perfecto", 
sep= "/n")

opcion = input("Ingrese su opción")

match opcion:
    case "a":
        n = int(input("Ingrese un número entero positivo:  "))

        if(n<= 0):
            print("Error, ingrese un número entero positivo")
        else:

            sumatoria = 0
            for contador in range (1, n+1):
                sumatoria += contador 

            print(f"La sumatoria es: {sumatoria}")
    case "b":
        print("tarea")
    case "c":
        tituloCol = "\t"
        #Imprimir titulo de columna
        for col in range(1,11):
            tituloCol += str(col)+ "\t"
           
        print(tituloCol)

        #Imprimir filas
        textoFila = ""
        for fila in range(1,11):
            textoFila += str(fila) + "\t"
        
            for col in range(1,11):
                textoFila += str(fila *col) + "\t"   
           
            print(textoFila)


