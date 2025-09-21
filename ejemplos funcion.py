# Función para calcular el promedio de temperaturas de varias ciudades
def calcular_promedio_temperaturas(datos):

    promedios = {}

    for ciudad, semanas in datos.items():
        suma_total = 0
        cantidad_dias = 0

        for semana in semanas:
            suma_total += sum(semana)
            cantidad_dias += len(semana)

        promedio = suma_total / cantidad_dias
        promedios[ciudad] = round(promedio, 2)
    return promedios


datos_temperaturas = {
    "Quito": [
        [18, 20, 19, 21, 22, 20, 19],
        [19, 21, 20, 22, 23, 21, 20],
        [18, 19, 20, 20, 21, 22, 19],
        [19, 20, 21, 22, 23, 24, 20]
    ],
    "Guayaquil": [
        [28, 30, 29, 31, 32, 30, 29],
        [29, 31, 30, 32, 33, 31, 30],
        [28, 29, 30, 30, 31, 32, 29],
        [29, 30, 31, 32, 33, 34, 30]
    ],
    "Cuenca": [
        [16, 18, 17, 19, 20, 18, 17],
        [17, 19, 18, 20, 21, 19, 18],
        [16, 17, 18, 18, 19, 20, 17],
        [17, 18, 19, 20, 21, 22, 18]
    ]
}


resultado = calcular_promedio_temperaturas(datos_temperaturas)
print("Promedio de temperaturas por ciudad:")
for ciudad, promedio in resultado.items():
    print(f"{ciudad}: {promedio} °C")
