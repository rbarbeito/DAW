# Javascript

## Variable y tipos de datos

Variable almacena informacion de diferentes tipos

tipos de datos:
-  string
- boolean
- number
- array
- objetos
- char

> toda variable debe tener un entorno de trabajo `scope`

`var`, `let`, `const`

> **No usar var** ya que hace vulneraba la aplicación, ya que una variable global es accesible desde cualquier parte de mi aplicación

## Estructuras de control
 
 ```Javascript
 if (condition){

 }

// Otro tipo de if
 if(condition){

 }else if(condicion){

 } else {

 }
 ```


## Bucles

Todo bucle necesita un iterador

```javascript
// Bucle for
for (let i=0; i < lista.length; i++){

}

// while
let i=0
while(i< l.length){
    console.log(i)
    console.log(l[i])
    i++
}
```
## Funciones

Bloque de código que puede ser invocado desde cualquier parte de mi aplicación donde sea importada

```javascript
// A los parametros se le dan valores cuando se llama la función o pueden ser definidos con valores por defectos
function nombre(parametro1, parametro2){

}

// función sin parametros
function nombre(){
    
}

```

las funciones pueden retornar algo o no, `return` corta el funcionamiento de la función

