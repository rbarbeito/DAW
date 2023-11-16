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

list_total=[]


for i in range(5):
    lista=[]
    for x in range(5):
        enunciado = "Teclee el valor " + \
            str(x+1) + " de la fila " + str(i+1) + ": "
        nuevo_numero = int(input(enunciado))

        lista.append(nuevo_numero)

    list_total.append(lista)
    
print()
print(list_total)


lista_suma_filas=[]
lista_suma_columnas=[]

for i in range(5):
    suma_filas=0
    suma_columnas=0
    for x in range(5):
        suma_filas+=list_total[i][x]
        suma_columnas+=list_total[x][i]
    lista_suma_filas.append(suma_filas)
    lista_suma_columnas.append(suma_columnas)
        
print(lista_suma_columnas)        
print(lista_suma_filas)        