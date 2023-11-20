lista = [1, 3, 4, 5, 6, 7, 82]
contador=len(lista)

while contador >0:
    contador+=-1
    del lista[contador]
    print(lista)
    
print()
print("La lista esta vacia")
