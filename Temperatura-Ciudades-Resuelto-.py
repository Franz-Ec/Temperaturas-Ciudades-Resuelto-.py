# Definir la matriz 3D con datos de temperaturas
# Dimensiones: [ciudades][semanas][días de la semana]
temperaturas = [
    # Ciudad 1
    [
        # Semana 1
        [20, 22, 21, 19, 18, 20, 21],
        # Semana 2
        [21, 23, 22, 20, 19, 21, 22]
    ],
    # Ciudad 2
    [
        # Semana 1
        [25, 26, 24, 23, 22, 24, 25],
        # Semana 2
        [26, 27, 25, 24, 23, 25, 26]
    ]
]

# Nombres de las ciudades
ciudades = ["Ciudad 1", "Ciudad 2"]

# Calcular y mostrar el promedio de temperaturas para cada ciudad y semana
for ciudad_index, ciudad in enumerate(temperaturas):
    print(f"Promedios de temperaturas para {ciudades[ciudad_index]}:")
    for semana_index, semana in enumerate(ciudad):
        promedio = sum(semana) / len(semana)
        print(f"  Semana {semana_index + 1}: {promedio:.2f}°C")
