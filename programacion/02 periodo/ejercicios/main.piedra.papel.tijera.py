import random

print("PIEDRA, PAPEL, TIJERA\n")

cantidad = 15
contador_jugador = 0
contador_computadora = 0
ultimo_compu = 0
opcion_computadora = random.randint(1, 3)

while True:
    print("*"*cantidad)
    print(" "*3 + "Opciones")
    print("*"*cantidad)
    print(" 1. Piedra")
    print(" 2. Papel")
    print(" 3. Tijera")
    print(" 0. Salir")
    print("*"*cantidad)

    while ultimo_compu == opcion_computadora:
        opcion_computadora = random.randint(1, 3)

    ultimo_compu = opcion_computadora
    opcion_jugador = int(input("Seleccione su opción: "))

    if opcion_jugador == 0:
        break

    if opcion_jugador == 1 and opcion_computadora == 2:
        contador_computadora = contador_computadora+1
        print("Perdiste computadora escogio 'PAPEL'")
    elif opcion_jugador == 2 and opcion_computadora == 3:
        contador_computadora = contador_computadora + 1
        print("Perdiste computadora escogio 'TIJERA'")
    elif opcion_jugador == 3 and opcion_computadora == 1:
        contador_computadora = contador_computadora+1
        print("Perdiste computadora escogio 'PIEDRA'")
    elif opcion_jugador == 2 and opcion_computadora == 1:
        contador_jugador = contador_jugador+1
        print("Ganaste computadora escogio 'PIEDRA'")
    elif opcion_jugador == 3 and opcion_computadora == 2:
        contador_jugador = contador_jugador+1
        print("Ganaste computadora escogio 'PAPEL'")
    elif opcion_jugador == 1 and opcion_computadora == 3:
        contador_jugador = contador_jugador+1
        print("Ganaste computadora escogio 'TIJERA'")
    else:
        print("Nadie suma nada ambos escogieron lo mismo")


if contador_jugador > contador_computadora:
    a_favor = "a favor del jugador"
elif contador_jugador == contador_computadora:
    a_favor = "¡Empate técnico!"
else:
    a_favor = "a favor de la computadora"

print("El marcador quedo:", contador_jugador,
      "a", contador_computadora, a_favor)
