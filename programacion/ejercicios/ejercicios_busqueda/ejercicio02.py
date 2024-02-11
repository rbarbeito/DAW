
def busq_desc(lista, fin, posicion):

    if fin < 0:
        return posicion

    if lista[fin] != 0:
        posicion = fin
        return busq_desc(lista, fin-1, posicion)

    return busq_desc(lista, fin-1, posicion)


lista = [0, 1, 0, 5]
print(busq_desc(lista, len(lista)-1, -1))
