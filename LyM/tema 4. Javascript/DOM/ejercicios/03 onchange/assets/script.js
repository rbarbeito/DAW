let menos = document.getElementById('minus')
let plus = document.getElementById('plus')
let selectBandera = document.getElementById('banderas')
let imagenProducto = document.getElementById('imagenProducto')
let description = document.getElementById('description')
let equipo = document.getElementById('equipo')
let precio = document.getElementsByTagName('h4')[0]

let cantidad = document.getElementById('cant')
let cant_valor = Number(cantidad.textContent)

let total = document.getElementById('final')
let precio_final = Number(total.textContent)

const pulovers = [
  {
    pais: 'Cuba',
    imagen:
      'https://imgs.search.brave.com/VmjfTACFsYc0MKPZSjwnUT8Mb_kF-w8bE0pxYfilsVQ/rs:fit:500:0:0/g:ce/aHR0cHM6Ly9pbWFn/ZXMudmV4ZWxzLmNv/bS9tZWRpYS91c2Vy/cy8zLzMxODY5Ni9p/c29sYXRlZC9wcmV2/aWV3LzU4ZWY1ZjRj/OWE5NGUwZWZjNDk5/MjI4NzRiOWJiMWEy/LWNhbWlzZXRhLWRl/LWZ1dGJvbC1kZS1j/dWJhLnBuZw',
    precio: '500',
    description: 'lorem lorem lorem cuba cuba',
  },
  {
    pais: 'Colombia',
    imagen:
      'https://imgs.search.brave.com/QvfU1osciJvuJnCKnPUNGJpaEhkTiqzt5hoaqLVP7AM/rs:fit:500:0:0/g:ce/aHR0cHM6Ly9pbWFn/ZXMudmV4ZWxzLmNv/bS9tZWRpYS91c2Vy/cy8zLzMxODY5OC9p/c29sYXRlZC9wcmV2/aWV3L2JlZmJjMDRm/ODg2ZTNiMzI1YWYw/OTMzNzk5ZTM2MzNh/LWNhbWlzZXRhLWRl/LWZ1dGJvbC1kZS1j/b2xvbWJpYS5wbmc',
    precio: '300',
    description: 'lorem lorem lorem',
  },
  {
    pais: 'España',
    imagen:
      'https://imgs.search.brave.com/qVxfSZPG5i1I1ZYhzIuVtG7ujwXWssMaJfAzyKIHfug/rs:fit:500:0:0/g:ce/aHR0cHM6Ly9pbWFn/ZXMudmV4ZWxzLmNv/bS9tZWRpYS91c2Vy/cy8zLzMyMTk0NS9p/c29sYXRlZC9wcmV2/aWV3LzFlODc3Yjlh/NmM3NjUyMDNmZjgw/ZDM5ODRlOWY1MDhk/LWNhbWlzZXRhLWlu/c3BpcmFkYS1lbi1s/YS1iYW5kZXJhLWRl/LWVzcGFhLWEucG5n',
    precio: '100',
    description: 'lorem lorem lorem',
  },
]

imagenProducto.src = pulovers[0].imagen
description.innerHTML = pulovers[0].description
equipo.innerHTML = `Camiseta de equipo ${pulovers[0].pais}`
precio.innerHTML = pulovers[0].precio
total.innerHTML = calcularPrecio()

menos.addEventListener('click', () => {
  cant_valor -= 1
  if (cant_valor < 0) {
    cant_valor = 0
  }

  cantidad.innerHTML = cant_valor
  total.innerHTML = calcularPrecio()
})

plus.addEventListener('click', () => {
  cant_valor += 1
  cantidad.innerHTML = cant_valor
  total.innerHTML = calcularPrecio()
})

// button.addEventListener('click', () => {
//   total.innerHTML = calcularPrecio()
// })

selectBandera.addEventListener('change', () => {
  imagenProducto.src = pulovers[selectBandera.value].imagen
  description.innerHTML = pulovers[selectBandera.value].description
  equipo.innerHTML = `Camiseta de equipo ${pulovers[selectBandera.value].pais}`
  precio.innerHTML = pulovers[selectBandera.value].precio

  cant_valor = 0
  cantidad.innerHTML = cant_valor
  total.innerHTML = calcularPrecio()
})

function calcularPrecio() {
  return Number(precio.textContent) * cant_valor
}
