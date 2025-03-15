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
def calcular_promedio_temperaturas(temperaturas, ciudades):
    """
    Calcula el promedio de temperaturas para cada ciudad y semana.
    
    :param temperaturas: Lista 3D con datos de temperaturas [ciudades][semanas][días de la semana]
    :param ciudades: Lista con los nombres de las ciudades
    :return: Diccionario con los promedios de temperaturas por ciudad y semana
    """
    promedios = {}
    
    for ciudad_index, ciudad in enumerate(temperaturas):
        promedios[ciudades[ciudad_index]] = []
        for semana_index, semana in enumerate(ciudad):
            promedio = sum(semana) / len(semana)
            promedios[ciudades[ciudad_index]].append(promedio)
    
    return promedios

# Datos de ejemplo
temperaturas = [
    [
        [20, 22, 21, 19, 18, 20, 21],
        [21, 23, 22, 20, 19, 21, 22]
    ],
    [
        [25, 26, 24, 23, 22, 24, 25],
        [26, 27, 25, 24, 23, 25, 26]
    ]
]

ciudades = ["Ciudad 1", "Ciudad 2"]

# Calcular promedios
promedios = calcular_promedio_temperaturas(temperaturas, ciudades)

# Mostrar resultados
for ciudad, promedios_semanales in promedios.items():
    print(f"Promedios de temperaturas para {ciudad}:")
    for semana_index, promedio in enumerate(promedios_semanales):
        print(f"  Semana {semana_index + 1}: {promedio:.2f}°C")
