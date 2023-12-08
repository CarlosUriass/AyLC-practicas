import random

contador_computadora = 0
contador_usuario = 0
contador_empate = 0
jugar = True

while jugar:
    # Pedir opción del usuario
    opcion_usuario = input("¿Piedra, papel o tijera.. ?").lower()

    # Generar opción de la computadora
    opcion_computadora = random.randint(1, 3)

    # Imprimir la opción de la computadora
    if opcion_computadora == 1:
        print("La computadora escogió piedra")
    elif opcion_computadora == 2:
        print("La computadora escogió papel")
    elif opcion_computadora == 3:
        print("La computadora escogió tijera")

    # Validar empate
    if (
        (opcion_usuario == 'piedra' and opcion_computadora == 1) or
        (opcion_usuario == 'papel' and opcion_computadora == 2) or
        (opcion_usuario == 'tijera' and opcion_computadora == 3)
    ):
        print("Empate!")
        contador_empate += 1
    else:
        # Combinaciones de juego
        if (
            (opcion_usuario == 'piedra' and opcion_computadora == 2) or
            (opcion_usuario == 'papel' and opcion_computadora == 3) or
            (opcion_usuario == 'tijera' and opcion_computadora == 1)
        ):
            print(f"¡{opcion_usuario.capitalize()} pierde, has perdido!")
            contador_computadora += 1
        else:
            print(f"¡{opcion_usuario.capitalize()} gana, has ganado!")
            contador_usuario += 1

    # Evaluar si sigue jugando
    continuar = input("Seguir jugando? 1) Si 2) No ")
    
    if continuar == "1":
        jugar = True
    else:
        jugar = False

# Mostrar cuántas veces ha ganado cada quien
print("La computadora ha ganado:", contador_computadora)
print("El usuario ha ganado:", contador_usuario)
print("Han empatado:", contador_empate)

# Validar ganador del juego
if contador_computadora > contador_usuario:
    print("El ganador es la computadora")
elif contador_computadora < contador_usuario:
    print("El ganador es el usuario")
else:
    print("Han empatado")
