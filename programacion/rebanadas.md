# Rebanadas

`my_list[start:end]`

1. `start` es el índice del primer elemento incluido en la rebanada.
2. `end` es el índice del primer elemento no incluido en la rebanada.


Así es como los índices negativos funcionan en las rebanadas:
```Python
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1]
print(new_list)
```

el resultado es `[8, 6, 4]`

3. Si omites el start en tu rebanada, se supone que deseas obtener un segmento que comienza en el elemento con índice 0

> `my_list[:end]` es un equivalente más compacto de `my_list[0:end]`

4. Del mismo modo, si omites el end en tu rebanada, se supone que deseas que el segmento termine en el elemento con el índice `len(my_list)`.

>`my_list[start:]` es equivalente a `my_list[start:len(my_list)]`

## borrar elementos

La instrucción `del` descrita anteriormente puede eliminar más de un elemento de la lista a la vez, también puede eliminar rebanadas
```Python
my_list = [10, 8, 6, 4, 2]
del my_list[1:3]
print(my_list)
```
`Nota:` En este caso, la rebanada **¡no produce ninguna lista nueva!**  modifica la lista original. La salida del fragmento es: `[10, 4, 2]`.

`del my_list[:]` borra el contenido de la lista
`del my_list` borra la lista