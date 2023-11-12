https://replit.com/join/zxxxyjgtgt-cesar-tomastom2

def calcular_porcentaje_error(lecturas):
    lecturas_correctas = 0

    for i in range(1, lecturas + 1):
        temperatura = float(input(f"Inserta la temperatura {i}: "))

        # Verificar si la temperatura está dentro del rango esperado (10 a 40 grados Celsius)
        if 10 <= temperatura <= 40:
            lecturas_correctas += 1

    # Calcular el porcentaje de error
    porcentaje_error = ((lecturas - lecturas_correctas) / lecturas) * 100

    return lecturas_correctas, porcentaje_error

# Pedir al usuario la cantidad de lecturas
num_lecturas = int(input("¿Cuántas lecturas de temperatura tienes?: "))

# Calcular y mostrar resultados
lecturas_correctas, porcentaje_error = calcular_porcentaje_error(num_lecturas)

print(f"El sensor se equivocó {num_lecturas - lecturas_correctas} veces.")
print(f"El porcentaje de error del sensor es del {porcentaje_error}%.")
