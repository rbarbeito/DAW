## Ocurrencias en una lista de  manera Ascendente

def ocurrencias(lista, fin, buscado, count):
    
    if fin == 0:
        if buscado  == lista[fin]:
           return count+1

        return count

    if buscado == lista[fin]:
        return ocurrencias(lista, fin-1, buscado, count+1)

    return ocurrencias(lista, fin-1, buscado, count)


lista=[1,5,8,4,9,5,15,46,5,78]
buscado=5
count=0

print(ocurrencias(lista, len(lista)-1, buscado, count))
