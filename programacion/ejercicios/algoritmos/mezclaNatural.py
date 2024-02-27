def mezclaNatural(lista1, lista2, lista):
        
    if len(lista1)==0 or len(lista2)==0:
        return lista + lista1 + lista2

    if lista1[0]<lista2[0]:
        lista.append(lista1[0])
        return mezclaNatural(lista1[1:],lista2[:],lista)

    else:
        lista.append(lista2[0])
        return mezclaNatural(lista1[:],lista2[1:],lista)


print(mezclaNatural([1,5,7,9],[2,6,8,10],[]))


