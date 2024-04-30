const contador = document.getElementById('contador')
const clicks = document.getElementById('clicks')
const caja = document.getElementById('caja')

let count = 0

let finishTime = false
let startGame = false

let colorsList = ['uno', 'dos', 'tres', 'cuatro']

function startCount(segundos) {
  contador.innerHTML = segundos
  if (segundos == 0) {
    contador.innerHTML = 'Tiempo Terminado'
    finishTime = true
    return
  }
  setTimeout(() => {
    startCount(segundos - 1)
  }, 1000)
}

caja.addEventListener('click', () => {
  if (startGame == false) {
    startCount(10)
    startGame = true
  }
  console.log(finishTime)
  if (!finishTime) {
    let numberRandom = Math.floor(Math.random() * colorsList.length)

    count++
    clicks.textContent = count
    caja.setAttribute('class', colorsList[numberRandom])
  }
})
