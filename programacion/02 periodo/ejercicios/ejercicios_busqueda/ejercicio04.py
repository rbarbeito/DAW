# buscar la ultima posicion de un numero diferente de cero que esta después de cero de manera descendente

def buscar(lista, inicio, position):

    if inicio <= 0:
        return position

    if lista[inicio-1] == 0 and lista[inicio] != 0:
        position = inicio
        return buscar(lista, inicio-1, position)

    return buscar(lista, inicio-1, position)


lista = [0, 0, 8, 5, 0, 2]
print(buscar(lista, len(lista)-1, -1))
