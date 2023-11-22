"""
Diseñe un algoritmo que permita decir si una persona es menor o mayor de edad. Considerando que 
la mayoria de edad es de 18 años, solicite el nombre e la persona y su fecha de nacimiento
y en base a esta deberá calcular su edad exacta (años cumplidos) y mostrar en pantalla un mensaje
como el siguiente

José tiene 19 años y es mayor de edad
paco tiene 17 años y es menor de edad

"""

nombre = str(input("¿Cual es tu nombre? "))
año_nacimiento = int(input("Ingrese su año de nacimiento: "))
mes_nacimiento = int(input("Ingrese su mes de nacimiento (numero): "))
dia_nacimiento = int(input("Ingrese su dia de nacimiento: "))

año_actual = int(input("¿Que año es? "))
mes_actual = int(input("De que mes? (Numero) "))
dia_actual = int(input("¿Que dia es hoy? "))


edad = año_actual - año_nacimiento

if edad < 18:
    print(f'{nombre} tiene {edad} y es menor de edad')
elif edad > 18:
   print(f'{nombre} tiene {edad} y es mayor de edad')
elif edad == 18: 
    if mes_actual > mes_nacimiento:
        if dia_actual > dia_nacimiento:
            print(f'{nombre} tiene {edad} y es mayor de edad')
        else:
            print(f'{nombre} tiene {edad} y es menor de edad')
    else:
        print(f'{nombre} tiene {edad} y es menor de edad')