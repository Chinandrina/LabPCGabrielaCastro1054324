# Definición de la matriz del tablero de ajedrez
tablero = [['' for _ in range(8)] for _ in range(8)]

# Función para agregar piezas al tablero
def agregar_piezas(n):
    for _ in range(n):
        while True:
            pieza = input("Ingrese el tipo de pieza (alfil, peón, caballo, torre, etc.): ")
            color = input("Ingrese el color de la pieza (blanco o negro): ")
            posicion = input("Ingrese la posición de la pieza (ejemplo: a1, e4, f8, etc.): ")
            columna = ord(posicion[0]) - ord('a')
            fila = 8 - int(posicion[1])
            
            # Validar posición y si está vacía
            if 0 <= columna < 8 and 0 <= fila < 8 and not tablero[fila][columna]:
                tablero[fila][columna] = f"{pieza[0].upper()}{color[0].upper()}"
                break
            else:
                print("Posición inválida o ya ocupada. Intente de nuevo.")

# Función para obtener los movimientos válidos del caballo
def movimientos_caballo(posicion, color):
    movimientos = [
        (-2, -1), (-1, -2), (1, -2), (2, -1),
        (-2, 1), (-1, 2), (1, 2), (2, 1)
    ]
    columna = ord(posicion[0]) - ord('a')
    fila = 8 - int(posicion[1])
    movimientos_validos = []
    
    for m in movimientos:
        nueva_fila = fila + m[0]
        nueva_columna = columna + m[1]
        if 0 <= nueva_fila < 8 and 0 <= nueva_columna < 8:
            casilla = tablero[nueva_fila][nueva_columna]
            if not casilla or casilla[1] != color[0].upper():
                movimientos_validos.append((nueva_fila, nueva_columna))
    
    return movimientos_validos

# Función para imprimir el tablero
def imprimir_tablero():
    print("Tablero de ajedrez:")
    for fila in tablero:
        print(' '.join(['[ ]' if casilla == '' else f'[{casilla}]' for casilla in fila]))

# Ejecución del programa
n = int(input("Ingrese la cantidad de piezas a agregar: "))
agregar_piezas(n)

caballo = input("Ingrese la posición del caballo a evaluar: ")
color = input("Ingrese el color del caballo (blanco o negro): ")
mov_validos = movimientos_caballo(caballo, color)

print("Movimientos válidos del caballo:")
for m in mov_validos:
    fila, columna = m
    casilla = tablero[fila][columna]
    if casilla:
        print(f"En {chr(columna + ord('a'))}{8 - fila} hay una pieza del equipo contrario: {casilla}")
    else:
        print(f"En {chr(columna + ord('a'))}{8 - fila} la casilla está vacía")

imprimir_tablero()
