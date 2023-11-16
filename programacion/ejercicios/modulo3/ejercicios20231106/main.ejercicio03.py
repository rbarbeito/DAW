# Diseñar el algoritmo correspondiente a un programa, que:

# Crea una tabla (lista con dos dimensiones) de 5x5 enteros.
# Carga la tabla con valores numéricos enteros.
# Suma todos los elementos de cada fila y todos los elementos de cada columna visualizando
# los resultados en pantalla.

margen_izquierdo = 4
titulo = "TABLA DE 5X5 Y RESULTADOS"
long = len(titulo)+margen_izquierdo*2
print()
print("*"*long)
print(" "*margen_izquierdo + titulo)
print("*"*long)

fila1 = []
fila2 = []
fila3 = []
fila4 = []
fila5 = []

for i in range(5):
    x = 0
    while x < 5:
        enunciado = "Teclee el valor " + \
            str(x+1) + " de la fila " + str(i+1) + ": "
        nuevo_numero = int(input(enunciado))

        if i == 0:
            fila1.append(nuevo_numero)
        elif i == 1:
            fila2.append(nuevo_numero)
        elif i == 2:
            fila3.append(nuevo_numero)
        elif i == 3:
            fila4.append(nuevo_numero)
        elif i == 4:
            fila5.append(nuevo_numero)

        x += 1

print()
print(fila1)
print(fila2)
print(fila3)
print(fila4)
print(fila5)


suma_fila1 = suma_fila2 = suma_fila3 = suma_fila4 = suma_fila5 = 0
lista_suma_columna = []
for i in range(5):
    suma_fila1 += fila1[i]
    suma_fila2 += fila2[i]
    suma_fila3 += fila3[i]
    suma_fila4 += fila4[i]
    suma_fila5 += fila5[i]

    lista_suma_columna.append(fila1[i]+fila2[i]+fila3[i]+fila4[i]+fila5[i])

print()
print("SUMA POR COLUMNAS")
for n in range(5):
    print("Suma de la columna" + str(n+1) + ": " + str(lista_suma_columna[n]))


print()
print("SUMA POR FILAS")
print("Suma fila1:", suma_fila1)
print("Suma fila2:", suma_fila2)
print("Suma fila3:", suma_fila3)
print("Suma fila4:", suma_fila4)
print("Suma fila5:", suma_fila5)
