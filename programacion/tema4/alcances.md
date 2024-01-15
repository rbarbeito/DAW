# Los Alcances en Python

> :policeman: El alcance de un nombre (por ejemplo, el nombre de una variable) es la parte del código donde el nombre es reconocido correctamente

Python deja usar las variables fuera del scope, si son usadas para leer.

- La variable var creada dentro de la función no es la misma que la que se definió fuera de ella, parece ser que hay dos variables diferentes con el mismo nombre.
- La variable de la función es una sombra de la variable fuera de la función.

> 🚨 Una variable que existe fuera de una función tiene un alcance dentro del cuerpo de la función, excluyendo a aquellas que tienen el mismo nombre.

```Python
def my_function():
    var = 2
    print("¿Conozco a la variable?", var)

var = 1
my_function()
print(var)
```
```
¿Conozco a la variable? 2
1
```


Existe un método especial en Python el cual puede **extender el alcance de una variable incluyendo el cuerpo de las funciones** para poder no solo leer los valores de las variables sino también modificarlos.

Este efecto es causado por la palabra clave reservada llamada `global`

```Python
global name
global name1, name2, ...
```

Usar `global` no es una buena practica