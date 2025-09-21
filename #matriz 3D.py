#matriz 3D

ciudades = ["Quito", "Guayaquil", "Cuenca"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
num_semanas = 2

import random

temperaturas = [
    [  
        [random.randint(15, 30) for _ in dias]  
        for _ in range(num_semanas)  
    ]
    for _ in ciudades
]

for i, ciudad in enumerate(ciudades):  
    print(f"\nPromedio de temperaturas en {ciudad}:")
    for s in range(num_semanas):      
        suma = 0
        for d in range(len(dias)):     
            suma += temperaturas[i][s][d]
        promedio = suma / len(dias)
        print(f"  Semana {s+1}: {promedio:.2f} °C")
