## Ocurrencias en una lista de  manera Ascendente

def ocurrencias_ascendentes(lista, inicio, buscado, count):
    
    if inicio == len(lista)-1:
        if buscado  == lista[inicio]:
           return count+1

        return count

    if buscado == lista[inicio]:
        return ocurrencias_ascendentes(lista, inicio+1, buscado, count+1)

    return ocurrencias_ascendentes(lista, inicio+1, buscado, count)


lista=[1,5,8,4,9,5,15,46,5,78]
buscado=5
count=0

print(ocurrencias_ascendentes(lista, 0, buscado, count))
