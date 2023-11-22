"""
Práctica 8. Algoritmo que imprima las tablas de multiplicar del 5 al 9.
Desde el
5 * 1 = 5
Hasta
9 * 10 = 90

"""

for i in range (5, 9+1):
    for j in range(1, 10+1):
        print(f'{i} * {j} = {i*j}')