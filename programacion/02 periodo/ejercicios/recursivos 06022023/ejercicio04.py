#  Suma de elementos pares de una lista de manera ascendente


def suma_pares_descendente(lista, fin):
    if fin <= 0:
        if lista[0] % 2 == 0:
            return lista[0]
        return 0

    if lista[fin] % 2 == 0:
        return suma_pares_descendente(lista, fin-1)+lista[fin]

    return suma_pares_descendente(lista, fin-1)


lista = [2, 4, 1, 3, 6, 5, 4]

print(suma_pares_descendente(lista, len(lista)-1))
