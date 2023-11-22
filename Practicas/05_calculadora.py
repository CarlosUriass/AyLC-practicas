"""
5. Elabore una calculadora que permita realizar las funciones aritméticas
básicas (suma, resta, multiplicación y división) a dos números. Se deberán
pedir dos números y qué operación se desea realizar con ellos, dependiendo de
lo que el usuario ingrese, se deberá realizar la operación correspondiente y
mostrar una salida similar a la siguiente:

Ejemplo:
Ingrese el primer número: 8
Ingrese el segundo número: 5
¿Qué operación desea realizar? 1)Suma 2)Resta 3)Multiplicación 4)División
3 La multiplicación de 8*5 es: 40
Validaciones:
En el caso de la división, no es posible dividir entre 0 (cero), si el usuario
ingresa 0 en el segundo número (divisor), se mostrará el mensaje “No es
posible dividir entre 0”.
"""

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

operacion = int(input("Que operacion desea realizar? 1)Suma 2)Resta 3)Multiplicación 4)División "))

if operacion == 1:
    print(f'La suma de {num1} + {num2} = {num1 + num2}')
elif operacion == 2:
    print(f'La resta de {num1} - {num2} = {num1 - num2}')
elif operacion == 3:
    print(f'La multiplicacion de {num1} * {num2} = {num1 * num2}')
elif operacion == 4:
    if num2 != 0:
        print(f'La division de {num1} / {num2} = {num1 / num2}')
    else:
        print("No es posible dividir entre 0")