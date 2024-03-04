# Listas dentro de listas

Rellenado de una lista
```Python
row = []

for i in range(8):
    row.append("WHITE_PAWN")
    
print(row)
```

## Compresión de listas

Una comprensión de lista es en realidad una lista, pero se creó sobre la marcha durante la ejecución del programa, y no se describe de forma estática.

```Python
row = [WHITE_PAWN for i in range(8)]
```

### Ejemplos

El fragmento de código genera una lista de diez elementos y la rellena con cuadrados de diez números enteros que comienzan desde cero `(0, 1, 4, 9, 16, 25, 36, 49, 64, 81)`

```Python
squares = [x ** 2 for x in range(10)]
```

El fragmento crea un arreglo de ocho elementos que contiene las primeras ocho potencias del numero dos `(1, 2, 4, 8, 16, 32, 64, 128)`

```Python
twos = [2 ** i for i in range(8)]
```

> A las lineas comprimidas se le puede poner condicionales

El fragmento crea una lista con solo los elementos impares de la lista squares. `[1, 3, 1, 5, 3, 7, 9]`

```Python
squares=[1,2,3,1,2,4,5,6,2,3,4,7,8,9,10]

odds = [x for x in squares if x % 2 != 0 ]
    
print(odds)
```


### Cosas interesantes

Hacer una listas con elementos aleatorios

```Python
import random

a=[random.randint(1,50) for _ in range(6)]

print(a)
```

> Ejemplo salida: [11, 44, 14, 3, 27, 34]


## Listas dentro de listas: arreglos bidimensionales

Arreglo bidemensional de 8x8

```Python
board = []

for i in range(8):
    row = ["EMPTY" for i in range(8)]
    board.append(row)
    
print(board)
```

>De manera reducida

```Python
board=[["EMPTY" for i in range(8)] for j in range(8)]
```

