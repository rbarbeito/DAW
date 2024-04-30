const palabras = ['cerveza', 'messi', 'whisky']

const palabraVacia = document.getElementById('palabraVacia')
const mensaje = document.getElementById('mensaje')
const letra = document.getElementById('letra')

let newPalabra = palabras[Math.floor(Math.random() * palabras.length)]

// let newPalabra = palabra.split('')
// let concat = []
// for (let i = 0; i < newPalabra.length; i++) {
//   concat.push('_')
// }
let concat = new Array(newPalabra.length).fill('_')

palabraVacia.innerText = concat.join(' ')

letra.addEventListener('keypress', (event) => {
  if (event.key == 'Enter') {
    newPalabra.includes(letra.value.toLowerCase()) ? esta() : noEsta()

  
  }
})

function esta() {
  mensaje.innerText = 'La letra esta en la palabra'

  for (let i = 0; i < newPalabra.length; i++) {
    if (newPalabra[i] == letra.value) {
        concat[i] = letra.value
    }
  }

  palabraVacia.innerText = concat.join(' ')
  letra.value=''

  if (!concat.includes('_')){
    // mensaje.innerText='Adivinaste la palabra'
    // mensaje.setAttribute("class","ganador")

    toastr.options = {
      closeButton: false,
      debug: false,
      newestOnTop: false,
      progressBar: true,
      positionClass: 'toast-top-full-width',
      preventDuplicates: false,
      onclick: null,
      showDuration: '300',
      hideDuration: '1000',
      timeOut: '5000',
      extendedTimeOut: '1000',
      showEasing: 'swing',
      hideEasing: 'linear',
      showMethod: 'fadeIn',
      hideMethod: 'fadeOut',
    }
    toastr.info('Adivinaste la palabra')
  }
}

function noEsta() {
  mensaje.innerText = 'La letra no esta en la palabra'
  letra.value = ''
}
