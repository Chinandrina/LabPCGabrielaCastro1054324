print("Meses del año en ingles y español")

meses = {
    'enero': 'January',
    'febrero': 'February',
    'marzo': 'March',
    'abril': 'April',
    'mayo': 'May',
    'junio': 'June',
    'julio': 'July',
    'agosto': 'August',
    'septiembre': 'September',
    'octubre': 'October',
    'noviembre': 'November',
    'diciembre': 'December'
}


mes_espanol = input("Ingrese un mes del año en español: ").lower()
mes_ingles = meses.get(mes_espanol, "Mes no válido")
print(f"El mes en inglés es: {mes_ingles}")