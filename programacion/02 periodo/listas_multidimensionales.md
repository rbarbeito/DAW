# Aplicaciones avanzadas

Imagina que desarrollas una pieza de software para una estación meteorológica automática. El dispositivo registra la temperatura del aire cada hora y lo hace durante todo el mes. Esto te da un total de 24 × 31 = 744 valores. Intentemos diseñar una lista capaz de almacenar todos estos resultados.

```Python
temps = [[0.0 for h in range(24)] for d in range(31)]
```

 Determinar la temperatura promedio mensual del mediodía.

 ```Python
 temps = [[0.0 for h in range(24)] for d in range(31)]
#
# La matriz se actualiza aquí.
#

total = 0.0

# days es cada una de las listas dentro de lista madre
for day in temps:
    total += day[11]

average = total / 31

print("Temperatura promedio al mediodía:", average)
```