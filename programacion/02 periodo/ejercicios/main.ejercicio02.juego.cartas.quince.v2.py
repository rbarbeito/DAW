import random


def rules():

    if sum_players[0] > 15 and sum_players[1] > 15:
        print("Ambos tienen mas de 15 puntos")
        return "No ha ganado nadie"
    elif sum_players[0] > 15:
        print(jugadores[0], "tiene mas de 15 puntos")
        return "Ganó " + jugadores[1]
    elif sum_players[1] > 15:
        print(jugadores[1], "tiene mas de 15 puntos")
        return "Ganó " + jugadores[0]
    elif sum_players[0] > sum_players[1]:
        print(jugadores[0], "tiene mas puntos que", jugadores[1])
        return "Ganó " + jugadores[0]
    elif sum_players[1] > sum_players[0]:
        print(jugadores[1], "tiene mas puntos que", jugadores[0])
        return "Ganó " + jugadores[1]

    return "Han empatado"


print("JUEGO DE CARTAS (QUINCE)")
jugadores = []
cartas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
players_data = [random.choices(cartas, k=3) for n in range(2)]
sum_players = [0, 0]

for i in range(2):
    jugadores.append(input("Entre el nombre del jugador " + str(i+1) + ": "))

for i in range(len(jugadores)):
    print(jugadores[i], "ha sacado:", players_data[i])

for i in range(3):
    sum_players[0] += players_data[0][i]
    sum_players[1] += players_data[1][i]


print("\n", rules(), sep="")
