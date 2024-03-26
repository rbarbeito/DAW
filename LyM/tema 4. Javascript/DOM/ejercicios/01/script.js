// console.log(document)

// Obtener un elemento
let seccion = document.getElementById('principal')
// console.log(seccion)

let tituloH1 = document.getElementsByTagName('h1')
tituloH1[0].style.color = '#fff'
console.log('tituloH1 :', tituloH1)

// Obtener varios elementos

let parrafos = document.getElementsByClassName('parrafo')
// console.log(parrafos)
// console.log(parrafos[0].innerHTML)

// Cambiar las propiedades de las secciones
seccion.style.background = '#561C24'
seccion.style.width = '100vw'
seccion.style.height = '100vh'
seccion.style.display = 'flex'
seccion.style.alignItems = 'center'
seccion.style.justifyContent = 'center'
seccion.style.flexDirection = 'column'
seccion.style.gap = '2px'
seccion.style.textAlign = 'center'

// parrafos[0].style.padding='1rem'
// parrafos[0].style.width='60%'
// parrafos[0].style.fontSize='20px'
// parrafos[0].style.background='#654412'

// parrafos[1].style.padding='1rem'
// parrafos[1].style.width='60%'
// parrafos[1].style.fontSize='20px'
// parrafos[1].style.background='green'

for (let i = 0; i < parrafos.length; i++) {
  if (parrafos[i].id == 'mierda') {
    parrafos[i].style.padding = '1rem'
    parrafos[i].style.width = '60%'
    parrafos[i].style.fontSize = '20px'
    parrafos[i].style.background = '#6D2932'
  } else {
    parrafos[i].style.padding = '1rem'
    parrafos[i].style.width = '60%'
    parrafos[i].style.fontSize = '20px'
    parrafos[i].style.background = '#C7B7A3'
  }
}

let button = document.getElementsByTagName('button')[0]

button.addEventListener('click', () => {
  console.log('A la mierda con estos 2')

  let colores = ['red', 'yellow', 'blue', 'magenta']
  let color = colores[Math.floor(Math.random() * colores.length)]

  seccion.style.background = colores[Math.floor(Math.random() * colores.length)]
  parrafos[0].style.color = colores[Math.floor(Math.random() * colores.length)]
  parrafos[1].style.color = colores[Math.floor(Math.random() * colores.length)]
})
