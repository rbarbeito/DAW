const popup = document.getElementById('popup')
const closeButton = document.getElementById('buttonClose')

setTimeout(() => {
  popup.setAttribute('class', 'abrir')
}, 3000)


closeButton.addEventListener("click",()=>{
    popup.removeAttribute('class', 'abrir')
})
