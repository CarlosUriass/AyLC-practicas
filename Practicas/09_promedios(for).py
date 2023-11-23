# Datos generales sobre la materia, carrera y grupo
num_alumnos = int(input("¿Cuantos alumnos se han de evaluar? "))
carrera = input("Ingrese la carrera: ")
grupo = input("Ingrese el grupo: ")
materia = input("Ingrese el nombre de la materia: ")

prom_grupo = 0  # Inicializar promedio del grupo en 0

# Preguntar cuántos parciales son en el curso a evaluar
parciales = int(input("¿Cuantos parciales a evaluar son? "))

print("Promedios del grupo", grupo, "en la materia de", materia, "de la carrera", carrera)

for i in range(1, num_alumnos + 1):
    prom_alumno = 0  # En cada iteracion resetear el promedio del alumno

    # Pedir los datos del alumno 1 -> num_alumnos
    print("Ingrese los datos del alumno", i)
    apellido_paterno = input("Ingrese el apellido paterno: ")
    apellido_materno = input("Ingrese el apellido materno: ")
    nombre = input("Ingrese nombre(s): ")

    # Pedir la calificación del parcial desde 1 a parciales
    for j in range(1, parciales + 1):
        calf_parcial = float(input("Ingrese la calificacion del parcial {}: ".format(j)))
        prom_alumno += calf_parcial  # En cada iteración se le suma el parcial al "promedio"

    prom_alumno /= parciales  # Sacar la media
    prom_grupo += prom_alumno  # Agregar la media del alumno a un "Promedio" del grupo
    prom_alumno = round(prom_alumno)  # Redondeo del promedio del alumno

    # Escribir promedio y si está aprobado o reprobado
    print("El promedio de {} {} {} es: {}".format(apellido_paterno, apellido_materno, nombre, prom_alumno))
    
    if prom_alumno < 6:
        print("{} {} {} está reprobado".format(apellido_paterno, apellido_materno, nombre))
    else:
        print("{} {} {} está aprobado".format(apellido_paterno, apellido_materno, nombre))

# Una vez acabadas las iteraciones se imprime el promedio del grupo

# Validar si el promedio del grupo es aprobatorio
promedio_grupo = prom_grupo / num_alumnos
print("El promedio del grupo {} en la materia de {} es: {}".format(grupo, materia, round(promedio_grupo)))

if promedio_grupo < 6:
    print("El promedio del grupo es reprobatorio")
else:
    print("El promedio del grupo es aprobatorio")