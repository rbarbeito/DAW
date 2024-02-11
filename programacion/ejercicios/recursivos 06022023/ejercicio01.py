# Suma de elementos de una lista de manera Asc

def ascendente(lista, inicio):

    if inicio == len(lista)-1:
        return lista[inicio]

    return ascendente(lista, inicio+1) + lista[inicio]


lista = [2, 4, 1, 3, 6, 5, 4]

print(ascendente(lista, 0))
