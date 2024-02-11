## Suma de elementos impares de una lista de manera ascendente

def suma_impares_ascendente(lista,inicio):

    if inicio == len(lista)-1:
        if lista[inicio] %2 != 0:
            return lista[inicio]

        return 0
        

    if lista[inicio] %2 != 0:
        return lista[inicio] + suma_impares_ascendente(lista, inicio+1)

    return suma_impares_ascendente(lista, inicio+1)


lista=[1,5,8,4,9,3,15,46,30,78]


print(suma_impares_ascendente(lista,0))
