let menos = document.getElementById('minus')
let plus = document.getElementById('plus')
let button = document.getElementsByTagName('button')[0]

let cantidad = document.getElementById('cant')
let cant_valor = Number(cantidad.textContent)

let total = document.getElementById('final')
let precio_final = Number(total.textContent)

menos.addEventListener('click', () => {
  cant_valor -= 1
  if (cant_valor < 0) {
    cant_valor = 0
  }

  cantidad.innerHTML = cant_valor
})

plus.addEventListener('click', () => {
  cant_valor += 1
  cantidad.innerHTML = cant_valor
})

button.addEventListener('click', () => {
  let precio = Number(document.getElementsByTagName('h4')[0].textContent)

  total.innerHTML = precio * cant_valor
})
