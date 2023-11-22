"""
Práctica 7. Algoritmo que pida un número e imprima la tabla de multiplicar de ese número.
Ejemplo:
¿Qué tabla de multiplicar desea?
6
6 *1 = 6
6 * 2 = 12
…
6 * 10 = 60
"""
tabla = int(input("¿Que tabla de multiplicar desea? "))


for i in range(1, 10 + 1):
    print(f' {i} * {tabla} = {i*tabla}')