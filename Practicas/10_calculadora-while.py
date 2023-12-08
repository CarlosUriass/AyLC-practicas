encendido = True

while encendido:
    # Solicitar el primer número
    num1 = float(input("Ingrese el primer número: "))

    # Solicitar el segundo número
    num2 = float(input("Ingrese el segundo número: "))

    # Solicitar la operación deseada
    print("¿Qué operación desea realizar?")
    print("1) Suma")
    print("2) Resta")
    print("3) Multiplicación")
    print("4) División")
    operacion = int(input())

    # Realizar la operación seleccionada (Switch)
    if operacion == 1:
        resultado = num1 + num2
        print(f"La suma de {num1} + {num2} es: {resultado}")
    elif operacion == 2:
        resultado = num1 - num2
        print(f"La resta de {num1} - {num2} es: {resultado}")
    elif operacion == 3:
        resultado = num1 * num2
        print(f"La multiplicación de {num1} * {num2} es: {resultado}")
    elif operacion == 4:
        # Repetir hasta que sea diferente a 0
        while num2 == 0:
            print("No es posible dividir entre 0. Por favor, ingrese un número diferente de 0:")
            num2 = float(input())

        # Una vez sea diferente de 0 se realiza este bloque de código
        if num2 != 0:
            resultado = num1 / num2
            print(f"La división de {num1} / {num2} es: {resultado}")
    else:
        print("Operación no válida")

    seguir = input("¿Desea realizar otra operación? (Escriba 'si') ").lower()

    if seguir == "si":
        encendido = True
    else:
        encendido = False  # En caso de que el usuario ingrese algo diferente a "si", encendido se vuelve falso; por lo tanto, no repite el ciclo
