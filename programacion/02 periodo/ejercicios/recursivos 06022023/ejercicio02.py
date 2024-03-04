# suma de elementos de una lista de manera descendente


def descendente(lista, fin):
    if fin <= 0:
        return lista[0]

    return descendente(lista, fin-1) + lista[fin]


lista = [2, 4, 1, 3, 6, 5, 4]

print(descendente(lista, len(lista)-1))
