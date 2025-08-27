import statistics

estudiantes = [
    {"nombre": "Ana", "notas": [6.5, 7.0, 5.8]},
    {"nombre": "Luis", "notas": [4.2, 5.1, 6.0]},
    {"nombre": "Sofia", "notas": [3.9, 4.0, 4.5]}, #
    {"nombre": "Pedro", "notas": [5.5, 6.0, 6.3]},
    {"nombre": "Maria", "notas": [7.0, 6.8, 6.5]},
    {"nombre": "Diego", "notas": [4.8, 5.2, 5.0]},
    {"nombre": "Camila", "notas": [6.9, 6.7, 7.0]},
    {"nombre": "Andrés", "notas": [5.0, 4.7, 5.3]},
    {"nombre": "Valentina", "notas": [6.2, 6.5, 6.9]},
    {"nombre": "Javier", "notas": [3.8, 4.1, 4.0]}, #
    {"nombre": "Fernanda", "notas": [5.9, 6.0, 6.1]},
    {"nombre": "Tomás", "notas": [4.5, 5.0, 5.2]},
    {"nombre": "Carolina", "notas": [6.7, 6.8, 6.9]},
    {"nombre": "Matías", "notas": [5.1, 5.3, 5.7]},
    {"nombre": "Ignacio", "notas": [4.9, 5.2, 5.4]},
    {"nombre": "Constanza", "notas": [6.8, 6.9, 7.0]},
    {"nombre": "Felipe", "notas": [5.0, 5.5, 5.9]},
    {"nombre": "Isidora", "notas": [6.1, 6.3, 6.7]},
    {"nombre": "Sebastián", "notas": [4.6, 5.0, 5.1]},
    {"nombre": "Paula", "notas": [6.4, 6.5, 6.6]},
    {"nombre": "Claudio", "notas": [5.7, 5.8, 6.0]},
    {"nombre": "Josefa", "notas": [6.9, 6.8, 7.0]},
    {"nombre": "Cristóbal", "notas": [4.3, 4.8, 5.1]},
    {"nombre": "Alejandra", "notas": [6.2, 6.4, 6.6]},
    {"nombre": "Rodrigo", "notas": [5.3, 5.6, 5.8]},
    {"nombre": "Gabriela", "notas": [6.7, 7.0, 6.9]},
    {"nombre": "Mauricio", "notas": [4.0, 4.5, 4.8]},
    {"nombre": "Daniela", "notas": [5.8, 6.0, 6.2]},
    {"nombre": "Vicente", "notas": [5.1, 5.4, 5.6]},
    {"nombre": "Francisca", "notas": [6.5, 6.7, 6.8]},
    {"nombre": "Alonso", "notas": [4.7, 5.0, 5.2]},
    {"nombre": "Antonia", "notas": [6.3, 6.5, 6.9]},
    {"nombre": "Nicolás", "notas": [5.2, 5.6, 5.9]},
]

promedio_estudiante = 0
promedios = []
aprobados = 0
notas_curso = []
promedios_des = []
aux = 0
reprobados = 0

for estudiante in estudiantes:
    notas = estudiante["notas"]
    nombre = estudiante["nombre"]
    promedio_estudiante = round(sum(notas) / len(notas), 2)
    promedios.append((nombre, promedio_estudiante))

    #1.Muestra el promedio de cada estudiante
    #print(f"{nombre} tiene un promedio de: {promedio_estudiante}")
    
    #2. Comprueba si todas las notas cumplen con la condicion y con el all() returna un valor de True
    if all(nota >= 4.0 for nota in notas):
        aprobados += 1

    #3. Recorre todas las notas de la lista de notas de cada estudiante y las almacena en las notas del curso, luego las ordena con sort y de la libreria statistics, se llama a mode() que busca el valor mas comun.
    for nota in notas:
        notas_curso.append(nota)
    
    notas_curso.sort()
    moda = statistics.mode(notas_curso) 

    #4.
    if any(nota < 4.0 for nota in notas):
        reprobados += 1

    bajo_cuatro = round((reprobados / len(promedios)) * 100, 2)

#5.Listado Ordenado (Mayor a Menos) de los estudiantes segun su promedio
i = 1
for nombre, promedio in sorted(promedios, key=lambda x: x[1], reverse=True):
    print(f"{i}. Nombre: {nombre}, Promedio: {promedio}")
    i += 1

maximo = max(promedios, key=lambda x: x[1])
minimo = min(promedios, key=lambda x: x[1])
 

#1.Muestra el proemdio mas bajo y mas alto
#print(f"El promedio más alto es {maximo[1]} y corresponde a {maximo[0]}")
#print(f"El promedio más bajo es {minimo[1]} y corresponde a {minimo[0]}")

#2. Muestra el numero de alumnos aprobados
#print(f"El numero de alumnos aprobados es de: {aprobados}")

#3.Muestra la nota que mas se repite de los estudiantes
#print(f"La moda es: {moda}")

#4.Muestra el porcentaje de almunos que tienen almenos una nota menor a 4.0
#print(f"El porcentaje de estudiantes que tiene almenos una nota menor a 4.0 es del: {bajo_cuatro}%")



