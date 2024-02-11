# suma de elementos pares de una lista de manera Ascendentes


def suma_pares_ascendente(lista, inicio):

    if inicio == len(lista)-1:
        if lista[inicio] % 2 == 0:
            return lista[inicio]
        return 0

    if lista[inicio] % 2 == 0:
        return lista[inicio] + suma_pares_ascendente(lista, inicio+1)

    return suma_pares_ascendente(lista, inicio+1)


lista = [2, 4, 1, 3, 6, 5, 4]

print(suma_pares_ascendente(lista, 0))
