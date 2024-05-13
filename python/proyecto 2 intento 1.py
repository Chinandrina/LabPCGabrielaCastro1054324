class Pieza:
    def __init__(self, tipo, color, posicion):
        self.tipo = tipo
        self.color = color
        self.posicion = posicion

def crear_tablero():
    # Inicializa un tablero de 8x8 con None
    return [[None for _ in range(8)] for _ in range(8)]

def agregar_piezas(tablero, piezas):
    for pieza in piezas:
        col, fila = convertir_notacion(pieza.posicion)
        if tablero[fila][col] is None:
            tablero[fila][col] = pieza
        else:
            raise ValueError("Ya hay una pieza en esa posición")

def convertir_notacion(notacion):
    letras = 'abcdefgh'
    col = letras.index(notacion[0])
    fila = 8 - int(notacion[1])
    return col, fila

def movimientos_caballo(tablero, posicion):
    movimientos = [
        (-2, -1), (-1, -2), (1, -2), (2, -1),
        (-2, 1), (-1, 2), (1, 2), (2, 1)
    ]
    col, fila = convertir_notacion(posicion)
    posibles_movimientos = []
    for dx, dy in movimientos:
        nueva_fila, nueva_col = fila + dy, col + dx
        if 0 <= nueva_fila < 8 and 0 <= nueva_col < 8:
            pieza_destino = tablero[nueva_fila][nueva_col]
            if pieza_destino is None or pieza_destino.color != tablero[fila][col].color:
                posibles_movimientos.append((nueva_col, nueva_fila))
    return posibles_movimientos

def imprimir_tablero(tablero):
    for fila in tablero:
        print(fila)

# Ejemplo de uso:
tablero = crear_tablero()
piezas = [
    Pieza('alfil', 'blanco', 'c4'),
    Pieza('peon', 'negro', 'd4'),
    # Agrega más piezas según sea necesario
]
agregar_piezas(tablero, piezas)
caballo = Pieza('caballo', 'blanco', 'e5')
agregar_piezas(tablero, [caballo])
movimientos = movimientos_caballo(tablero, caballo.posicion)
print("Movimientos válidos del caballo:", movimientos)
imprimir_tablero(tablero)
