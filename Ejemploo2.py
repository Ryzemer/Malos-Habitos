# Definición de la función calcular
def calcular(a, b, c):
    res = a * b + c
    return res

# Función principal
def principal():
    # Definición de las variables
    x = 5
    y = 3
    z = 7

    # Llamada a la función calcular con los valores de x, y, z
    resultado = calcular(x, y, z)

    # Impresión del resultado
    print(f"El resultado es:", resultado)

# Llamada a la función principal para iniciar el programa
principal()
