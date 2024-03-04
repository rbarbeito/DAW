# Arreglos tridimensionales

> Imagina un hotel. Es un hotel enorme que consta de tres edificios, de 15 pisos cada uno. Hay 20 habitaciones en cada piso. Para esto, necesitas un arreglo que pueda recopilar y procesar información sobre las habitaciones ocupadas/libres.

```Python
rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]

# False for r in range(20) --- numero de habitaciones

# [[False for r in range(20)] for f in range(15) --- Cada uno de los pisos

# [[False for r in range(20)] for f in range(15)] for t in range(3) -- Cada uno de los edificios del Hotel
```


El primer índice (0 a 2) selecciona uno de los edificios; el segundo (0 a 14) selecciona el piso, el tercero (0 a 19) selecciona el número de habitación. Todas las habitaciones están inicialmente desocupadas. 

> Ahora ya puedes reservar una habitación para dos recién casados: en el segundo edificio, en el décimo piso, habitación 14:

```Python
rooms[1][9][13] = True
```