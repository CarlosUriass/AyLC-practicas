num = 0

while num < 2 or num > 9:
    num = int(input("¿Qué tabla de multiplicar desea? "))  # Se redefine el valor de la variable para saber si sale del ciclo o no

# Generar ciclo
for i in range(1, 11):  # for del 1 al 10
    print(f"{num} x {i} = {i * num}")
