// console.log("hola mundo kk!");

let nameList = ['Rodolfo']

console.log('Before Push: ', nameList)

/**
 * add nuevo elemento en el array con Push,
 * Este los adiciona al final del array
 */

nameList.push('Pepe')
console.log('After puh :', nameList)

/**
 * Adición de elementos al principio del array
 * Para esto se usa unshift
 */

nameList.unshift('Maria')
console.log('After unshift :', nameList)

/**
 * Eliminar el ultimo elemento del array
 * Se usa el POP
 */

nameList.pop()
console.log('After POP :', nameList)

/**
 * Eliminar e primer elemento del array
 */

nameList.unshift()
console.log('After unshift :', nameList)

/**
 * Agregar varios elementos a la vez
 */

nameList.push('Juan', 'Jose', 'Fernando')
console.log('After push multiple :', nameList)

/**
 * Ordenar asc los elementos de un array
 */

nameList.sort()
console.log('After sort :', nameList)

console.log('<---- Objetos ---->')

let persona = {
  nombre: 'Rodolfo',
  edad: 52,
  preferencias: 'MotoGp',
  casado: true,
  peso: 50,
  amigos: ['yo', 'mismo'],
}

/**
 * Accediendo a la propiedad nombre del objeto persona
 */
console.log('nombre: ', persona.nombre)

/**
 * Array de objetos
 */

let personas = require('./data.json')

console.log(personas)

/**
 * Ejercicio 01.
 * Dado el array de objetos recien creado, crea una funcion que devuelva un nuevo array con los alumnos casados
 */
console.log('Ejercicio 1')

function listaCasados(lista) {
  let casados = []
  for (let i = 0; i < lista.length; i++) {
    if (lista[i].casado == true) {
      casados.push(lista[i].nombre)
    }
  }

  return casados
}

console.log('lista casados: ', listaCasados(personas))

/**
 * Ejercicio 2. media de edades
 */
console.log('<--- Ejercicio 1 --->')

function mediaEdad(lista) {
  let suma = 0

  for (let i = 0; i < lista.length; i++) {
    suma += lista[i].edad
  }

  return suma / lista.length
}

console.log('Media de las edades: ', mediaEdad(personas))

function listaGraficos(lista) {
  let listaParaGraficos = []
  for (let i = 0; i < lista.length; i++) {
    listaParaGraficos.push([i + 1, lista[i]])
  }

  return listaParaGraficos
}

listainicial = [3, 5, 6, 7, 8, 9, 4, 9, 8, 4, 6, 5]
console.log('lista para graficos', listaGraficos(listainicial))

/**
 * Obtener numeros aleatorios
 */

let aleatorio = Math.floor(Math.random() * personas.length)
console.log('aleatorio :', aleatorio)

console.log('alumno :', personas[aleatorio].nombre)

/**
 * Ejercicio 2. media de edades
 * dado el array de objetos antes creado, crea una función que imprima por consola, algún amigo de los alumnos mayores de 18
 */
console.log('<--- Ejercicio 3 --->')

function amigos(lista) {
  let mayoresDO = []

  for (let i = 0; i < lista.length; i++) {
    if (lista[i].edad >= 18) {
      mayoresDO.push({
        nombre: lista[i].nombre,
        amigos: lista[i].amigos,
      })
    }
  }


  for (let i = 0; i < mayoresDO.length; i++) {

    let aleatorio = Math.floor(Math.random() * mayoresDO[i].amigos.length)

    console.log(
      `Un amigo de  ${mayoresDO[i].nombre} es ${mayoresDO[i].amigos[aleatorio]}`
    )
  }
}

amigos(personas)



console.log(personas[0].amigos[3])
