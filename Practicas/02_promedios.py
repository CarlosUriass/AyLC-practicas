# Solicitar datos generales de la materia
carrera = input("Ingrese la carrera: ")
grupo = input("Ingrese el grupo: ")
materia = input("Ingrese el nombre de la materia: ")

# Inicializar variables del grupo
promedioGrupo = 0
sumaCalificacionesGrupo = 0

# Capturar datos del primer alumno
print("Datos del primer alumno")
apellidoPaterno1 = input("Ingrese el apellido paterno: ")
apellidoMaterno1 = input("Ingrese el apellido materno: ")
nombres1 = input("Ingrese el nombre(s): ")
calificacion1_1 = float(input("Ingrese la calificación parcial 1: "))
calificacion2_1 = float(input("Ingrese la calificación parcial 2: "))
calificacion3_1 = float(input("Ingrese la calificación parcial 3: "))
promedio1 = round((calificacion1_1 + calificacion2_1 + calificacion3_1) / 3, 2)

# Capturar datos del segundo alumno
print("Datos del segundo alumno")
apellidoPaterno2 = input("Ingrese el apellido paterno: ")
apellidoMaterno2 = input("Ingrese el apellido materno: ")
nombres2 = input("Ingrese el nombre(s): ")
calificacion1_2 = float(input("Ingrese la calificación parcial 1: "))
calificacion2_2 = float(input("Ingrese la calificación parcial 2: "))
calificacion3_2 = float(input("Ingrese la calificación parcial 3: "))
promedio2 = round((calificacion1_2 + calificacion2_2 + calificacion3_2) / 3, 2)

# Capturar datos del tercer alumno
print("Datos del tercer alumno")
apellidoPaterno3 = input("Ingrese el apellido paterno: ")
apellidoMaterno3 = input("Ingrese el apellido materno: ")
nombres3 = input("Ingrese el nombre(s): ")
calificacion1_3 = float(input("Ingrese la calificación parcial 1: "))
calificacion2_3 = float(input("Ingrese la calificación parcial 2: "))
calificacion3_3 = float(input("Ingrese la calificación parcial 3: "))
promedio3 = round((calificacion1_3 + calificacion2_3 + calificacion3_3) / 3, 2)

# Escribir promedios de la materia, grupo y carrera
print(f"Promedios de la materia {materia} del grupo {grupo} de la carrera {carrera}")

# Escribir promedio de cada alumno y calcular sumaCalificacionesGrupo
print(f"El promedio de {nombres1} {apellidoPaterno1} {apellidoMaterno1} es: {promedio1}")
sumaCalificacionesGrupo += promedio1

print(f"El promedio de {nombres2} {apellidoPaterno2} {apellidoMaterno2} es: {promedio2}")
sumaCalificacionesGrupo += promedio2

print(f"El promedio de {nombres3} {apellidoPaterno3} {apellidoMaterno3} es: {promedio3}")
sumaCalificacionesGrupo += promedio3

# Calcular el promedio del grupo
promedioGrupo = round(sumaCalificacionesGrupo / 3, 2)

# Mostrar el promedio del grupo
print("El promedio del grupo es:", promedioGrupo)
