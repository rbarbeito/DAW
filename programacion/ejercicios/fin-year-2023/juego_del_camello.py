import random as rand

print("\n¡Bienvenido al Camello!")
print("Has robado un camello para atravesar el gran desierto del Mobi.")
print("¡Los nativos quieren que les devuelvas su camello y salen en persecución tuya! Tendrás que sobrevivir al desierto y correr más que los nativos.")

opciones = ["\n",
            "A. Beber de la cantimplora.",
            "B. Velocidad moderada hacia adelante.",
            "C. A toda velocidad hacia adelante.",
            "D. Parar y descansar.",
            "E. Comprueba tu estado.",
            "F. Detenerte en la noche",
            "Q. Salir. "
            ]

hecho = False

millas_recorridas = 0
sed = 0
cansancio_camello = 0

avances = 0


millas_nativos = -20
sorbos_agua = 6


def sand_storm():
    return rand.choices([0, 1], weights=[1, 1], k=1)


def oasis():
    return rand.choices([0, 1], weights=[20, 1], k=1)


def go_forward_max_speed():
    global cansancio_camello, millas_nativos, millas_recorridas, sed, avances
    sed += 1
    cansancio_camello += rand.randint(1, 3)
    millas_recorridas += rand.randint(10, 20)
    millas_nativos += forward_natives()
    avances += 1


def go_forward_mod_speed():
    global cansancio_camello, millas_nativos, millas_recorridas, sed, avances
    sed += 1
    cansancio_camello += 1
    millas_recorridas += rand.randint(5, 12)
    millas_nativos += forward_natives()
    avances += 1


def stop_at_night():
    global cansancio_camello
    cansancio_camello = 0
    print("\nEl camello se congratula de ello")


def forward_natives():
    return rand.randint(7, 14)


while not hecho:

    for m in range(len(opciones)):
        print("" * 2, opciones[m])

    option = input("\n¿Qué eliges?: ")
    option = option.upper()

    if sed > 4 and sed <= 6:
        print("\nEstas sediento, bebe agua")
    elif sed > 6:
        print("\nHaz muerto de sed")
        hecho = True
        continue

    if cansancio_camello > 5 and cansancio_camello <= 8:
        print("\nTú camello se esta cansando")
    elif cansancio_camello > 8:
        print("\nTú camello ha muerto")
        hecho = True
        continue

    if millas_nativos >= 0:
        print("\nLos nativos te han capturado")
        hecho = True
        continue
    elif millas_nativos <= 15 and millas_nativos > 0:
        print("\nLos nativos se están acercando")

    if millas_recorridas >= 200 and sed <= 6 and cansancio_camello <= 8 and millas_nativos > 0:
        print("\nCruzaste el desierto, te haz escapado")
        hecho = True
        continue

    if option == "Q":
        break

    elif option == "A":

        if sorbos_agua >= 1:
            sed = 0
        elif sorbos_agua == 0:
            print("\nTe quedaste sin agua")
            sorbos_agua -= 1
            if oasis() == 1:
                print("\nA lo lejos se ve un oasis, te has salvado")
                sorbos_agua = 6
            else:
                print(
                    "\nNo ves un oasis hasta donde alcanzan tus ojos, estas muriendo de sed")
                sorbos_agua -= 1
        elif sorbos_agua < 0:
            print("\nHaz muerto de sed")
            hecho = True
            continue

    elif option == "B":

        go_forward_mod_speed()

        if millas_recorridas >= 200:
            print("\nCruzaste el desierto, te haz escapado")
            hecho = True
            continue
        else:
            print("\nHaz recorrido", millas_recorridas, "millas")

    elif option == "C":

        if avances % 3 == 0:
            if sand_storm() == 1:
                print("\nSe acerca una tormenta de nieve, avanzaras a menos velocidad")
                go_forward_mod_speed()
            else:
                go_forward_max_speed()
        elif avances % 5 == 0:
            if oasis() == 1:
                print(
                    "\nPasaste por un Oasis, restableciste tus fuerzas y la del camello")
                cansancio_camello = 0
                sed = 0
                sorbos_agua = 6

    elif option == "D":
        print("D")

    elif option == "E":

        print("\nMillas recorridas:", millas_recorridas)
        print("Veces que has bebido de la cantimplora:", sorbos_agua)
        print("Los nativos están a", millas_nativos*-1, "millas detrás de ti.")

    elif option == "F":
        stop_at_night()
        millas_nativos += forward_natives()
