## Suma de elementos pares de una lista de manera descendentes

def suma_pares_descendentes(lista,fin):

    if fin <= 0:
        if lista[0] % 2 ==0:
            return lista[0]
        return 0

    if lista[fin] %2==0:

        return lista[fin] +  suma_pares_descendentes(lista,fin-1)
    return suma_pares_descendentes(lista,fin-1)


lista=[1,5,8,4,9,3,15,46,30,78]


print(suma_pares_descendentes(lista,len(lista)-1))
