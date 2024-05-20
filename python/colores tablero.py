
colores_validos = ['blanco', 'negro']

def solicitar_color():
    while True:
        color = input("Color (blanco o negro): ").lower()
        if color not in colores_validos:
            print("Error: ese color no existe. Intente de nuevo.")
        else:
            return color

# Continuar con el resto del programa...
# Por ejemplo, para agregar una pieza:
tipo = input("Tipo de pieza (alfil, peón, caballo, torre, etc.): ").lower()
color = solicitar_color()
posicion = input("Posición (notación del juego, ej. a1, e4, f8): ").lower()
# Asegúrate de validar también el tipo de pieza y la posición antes de continuar.
