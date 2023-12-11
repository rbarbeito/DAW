# Ejemplos Random

```Python
input random

#lanzamientos en la ruleta,
print(random.choices(['red','black','green', [18,18,2], k=6]))


#Cartas repartidas
deal = random.sample(['tens', 'low cards'], counts=[16,36], k=20)
print(deal)
```