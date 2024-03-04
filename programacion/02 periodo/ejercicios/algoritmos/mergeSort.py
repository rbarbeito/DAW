import random


def mezlaNatural(lista, inicio, medio, final):
    if len(lista1) == 0 or len(lista2) == 0:
        return lista + lista1 + lista2

    if lista1[0] < lista2[0]:
        lista.append(lista1[0])
        return mezclaNatural(lista1[1:medio], lista2[medio+1:final], lista)

    else:
        lista.append(lista2[0])
        return mezclaNatural(lista1[:medio], lista2[1:], lista)

    return


def mergeSort(lista, inicio, final):
    if inicio < final:
        m = (inicio+final)//2
        mergeSort(lista, inicio, m)
        mergeSort(lista, m+1, final)

        mezlaNatural(lista, inicio, m, final)


lista = [random.randint(1, 100) for i in range(10)]

print(lista)

print(mergeSort(lista, 0, len(lista)-1))
