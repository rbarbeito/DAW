# Buscar el primer registro que nos piden Asc y desc, distinto de cero


def busq_asc(lista, inicio):

    if inicio >= len(lista):
        return -1

    if lista[inicio] != 0:
        return inicio

    return busq_asc(lista, inicio+1)


lista = [0, 1, 0, 5]


print(busq_asc(lista, 0))
