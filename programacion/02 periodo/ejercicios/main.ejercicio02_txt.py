# Escriba un programa que permita crear dos listas de palabras y que, a continuación,
# escriba las siguientes listas (en las que no debe haber repeticiones):

# -Lista de palabras que aparecen en las dos listas.
# -Lista de palabras que aparecen en la primera lista, pero no en la segunda.
# -Lista de palabras que aparecen en la segunda lista, pero no en la primera.
# -Lista de palabras que aparecen en ambas listas.


# Nota: Para evitar las repeticiones, el programa deberá empezar eliminando los elementos
#       repetidos en cada lista.


margen_izquierdo = 4
titulo = "COMPARACIÓN DE CONTENIDO DE LISTAS"
long = len(titulo)+margen_izquierdo*2
print()
print("*"*long)
print(" "*margen_izquierdo + titulo)
print("*"*long)


lista1 = []
lista2 = []
palabras_en_las_dos_listas = []


while True:
    palabra = input("Palabra de la lista1, -1 para finalizar esta lista: ")

    if palabra == "-1":
        break
    lista1.append(palabra)

print()
while True:
    palabra = input("Palabra de la lista2, -1 para finalizar esta lista: ")

    if palabra == "-1":
        break
    lista2.append(palabra)


for i in range(len(lista1)):
    for x in range(len(lista2)):

        if lista1[i] == lista2[x]:
            palabras_en_las_dos_listas.append(lista1[i])


for i in range(len(palabras_en_las_dos_listas)):
    cant_comp = len(lista1)
    while cant_comp >= 0:
        if palabras_en_las_dos_listas[i] == lista1[cant_comp-1]:
            del lista1[cant_comp-1]
        cant_comp -= 1

    cant_comp = len(lista2)
    while cant_comp >= 0:
        if palabras_en_las_dos_listas[i] == lista2[cant_comp-1]:
            del lista2[cant_comp-1]
        cant_comp -= 1

print()
print("Palabras presentes en ambas listas: ", palabras_en_las_dos_listas)
print("Palabras exclusivas de la lista 1: ", lista1)
print("Palabras exclusivas de la lista 2: ", lista2)

if len(palabras_en_las_dos_listas) == 0:
    print()
    print("No se repiten las palabras en las 2 filas")
elif len(palabras_en_las_dos_listas) == 1:
    print()
    print("Se repite una sola palabra:", palabras_en_las_dos_listas[0])
else:
    print()
    listado = ""
    for i in range(len(palabras_en_las_dos_listas)-1):
        listado += palabras_en_las_dos_listas[i] + ", "

    listado += palabras_en_las_dos_listas[len(palabras_en_las_dos_listas)-1]
    print("Se repiten un total de " + str(i) +
          " palabras en ambas listas, ellas son: " + listado)

if len(lista1) == 0:
    print("La lista 1 no tiene palabras exclusivas")
elif len(lista1) == 1:
    print("La lista 1 tiene una sola palabra exclusiva:", lista1[0])
else:
    listado = ""
    for i in range(len(lista1)-1):
        listado += lista1[i] + ", "

    listado += lista1[len(lista1)-1]
    print("La lista 1 tiene un total de " + str(i) +
          " palabras exclusivas, ellas son: " + listado)

if len(lista2) == 0:
    print("La lista 2 no tiene palabras exclusivas")
elif len(lista2) == 1:
    print("La lista 2 tiene una sola palabra exclusiva:", lista1[0])
else:
    listado = ""
    for i in range(len(lista2)-1):
        listado += lista2[i] + ", "

    listado += lista2[len(lista2)-1]
    print("La lista 2 tiene un total de " + str(i) +
          " palabras exclusivas, ellas son: " + listado)
