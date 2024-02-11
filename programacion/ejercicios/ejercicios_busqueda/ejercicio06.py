# obtener una lista con todas las posiciones disitintas de cero descendente

def posiciones(lista, inicio, listado):

    if inicio <= 0:
        return listado

    if lista[inicio] != 0:
        listado.append(inicio)
        return posiciones(lista, inicio-1, listado)

    return posiciones(lista, inicio-1, listado)


lista = [0, 0, 1, 0, 50, 0, 0, 0, 1, 0, 0]
print(posiciones(lista, len(lista)-1, []))
