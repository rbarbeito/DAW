## Métodos de la clase Array

```js
arr.push() //Adiciona un elemento al final del array

arr.pop()  // Elimina el ultimo elemento del array

arr.unshift() //Adiciona un elemento al Inicio

arr.shift() // Elimina el primer elemento del array

arr.sort() // Ordena los elementos del array
```

## Clase `Math` y algunos de sus métodos

```js
Math.random() // Devuelve un numero random entre 0 y 1 (El uno no esta incluido)

Math.floor() //Redondea el numero de forma decreciente, hacia el piso

Math.ceil() //Redondea el numero de forma ascendente, es decir hacia el cielo
```

## Función para generar un número aleatorio

```js

let numero = 10 // Este numero define el rango desde cero hasta donde queremos el aleatorio, en este caso entre (0 - 10)
const aleatorio= Math.floor(Math.random() * numero)
```

> Ver archivos de ejemplos en las carpetas