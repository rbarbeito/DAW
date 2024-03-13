//  comentario de una sola linea

/**
 * Comentario multilinea, para la documentacion
 * Dada la lista busca el numero 30 e imprimelo en pantalla y el numero de veces que aparece
 */

// let lista = [10, 20, 30, 40, 50]
// let lista2 = [10, 20, 30, 40, 50]

// function buscador(numero, lista){
//     let pos
//     let cont=0

//     for (let i = 0; i < lista.length; i++) {
//         if (lista[i] == numero) {
//             pos = i
//             cont++
//         }
//     }

//     if (cont == 0) {
//         console.log(`El numero ${numero} no esta en la lista`);
//     } else {
//         console.log(`El numero es: ${numero} esta en la posición ${pos} y aparece ${cont} veces`);

//     }

// }

// buscador(10, lista2)

// let pos
// let contador = 0
// for (let i = 0; i < lista.length; i++) {
//     if (lista[i] == 30) {
//         numero = lista[i]
//         pos = i
//         contador++
//     }

// }

// if (contador == 0) {
//     console.log(`El numero 30 no esta en la lista`);
// } else {
//     console.log(`El numero es: ${numero} esta en la posición ${pos}`);

// }

/**
 * Crea una funcion que dad un alista pasada como parametro, imprima por consola todos los elementos de la lista, indique cuales son pares y cual impares
 * y si la suma final es par o impar
 */


list = [15, 5, 78, 3, 49, 45, 7, 89, 45]

function kk(lista) {
    let suma = 0
    for (let i = 0; i < lista.length; i++) {

        if (lista[i] % 2 == 0) {
            console.log(`El numero ${lista[i]} es par`);
        } else {
            console.log(`El numero ${lista[i]} es impar`);
        }

        suma += lista[i]
    }

    return suma
}


let suma = kk(list)

if (suma % 2 == 0) {
    console.log(`El valor de la suma es ${suma} y es un numero par`);
} else {
    console.log(`El valor de la suma es ${suma} y es un numero impar`);
}


