# Definimos tuplas para estudiantes y sus respectivas calificaciones
estudiante1 = ("Evelyn", 95)
estudiante2 = ("Mia", 89)
estudiante3 = ("Omar", 85)
estudiante4 = ("Sergio", 97)
estudiante5 = ("Oscar", 88)
estudiante6 = ("Kaleb", 92)

# Creamos una lista de estudiantes
lista_de_estudiantes = [estudiante1, estudiante2, estudiante3, estudiante4, estudiante5, estudiante6]

# Creamos una función para calcular el promedio de calificaciones
def calcular_promedio(calificaciones):
    total = sum(calificaciones)
    promedio = total / len(calificaciones)
    return promedio

# Se muestra la información de cada estudiante y su promedio
for estudiante, calificacion in lista_de_estudiantes:
    print(f"Estudiante: {estudiante}")
    print(f"Calificación: {calificacion}")
    print("----")

# Aqui se calcula el promedio de calificaciones de todos los estudiantes
calificaciones = [calificacion for _, calificacion in lista_de_estudiantes]
promedio_total = calcular_promedio(calificaciones)
print(f"Promedio de calificaciones total: {promedio_total}")