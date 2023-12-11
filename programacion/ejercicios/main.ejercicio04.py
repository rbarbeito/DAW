# Diseñar el algoritmo correspondiente a un programa, que:

# Crea una tabla bidimensional de longitud 5x15 y nombre ‘marco’.
# Carga la tabla con dos únicos valores 0 y 1, donde el valor uno ocupará las posiciones o
# elementos que delimitan la tabla, es decir, las más externas, mientras que el resto de los
# elementos contendrán el valor 0.

marco = []

columnas = int(input("¿Cuantas filas tendra su tabla?: "))
filas = int(input("¿Cuantas columnas tendra su tabla?: "))

for i in range(columnas):
    list = []
    for x in range(filas):
        if x == 0 or i == 0:
            list.append(1)
        elif x == filas - 1 or i == columnas - 1:
            list.append(1)
        else:
            list.append(0)

    for z in range(len(list)):
        print(list[z], end=" ")
    print()
    marco.append(list)

# print(marco)
