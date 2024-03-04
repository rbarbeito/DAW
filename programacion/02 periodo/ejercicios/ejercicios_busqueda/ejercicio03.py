# buscar la ultima posicion de un numero diferente de cero que esta después de cero de manera ascendente

def buscar(lista, inicio, position):

    if inicio >= len(lista)-1:
        return position

    if lista[inicio+1] != 0 and lista[inicio] == 0:
        position = inicio+1
        return buscar(lista, inicio+1, position)

    return buscar(lista, inicio+1, position)


lista = [1, 0, 10, 5, 1, 1]
print(buscar(lista, 0, -1))
