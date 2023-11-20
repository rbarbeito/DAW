`absolute:` Hace que el resto de los elementos pierdan la referencia hacia el, puede posicionarse en cualquier parte de la pagina web.

`relative:` Hace que los elementos que contiene tengan referencia solo hacia el, solo se utiliza en contenedores

`fixed:` Fija un elemento en una posición especifica y ese elemento no se mueve aunque hagas scroll, se aplica al menu o al footer, se fijan arriba o abajo con `Top` y con `Left`

`z-index:` position en el eje Z `no` funciona si no tienes implementada la propiedad position

```css
* {
    padding: 0;
    margin: 0;
}

#principal {
    border: 1px solid;
    height: 50vh;
    display: flex;
    flex-direction: column;
    position: relative;
}

.caja {
    width: 100px;
    height: 100px;
    border-radius: 15px;
    margin-top: 10pt;
}

#c1 {
    background-color: red;
}

#c2 {
    background-color: blue;
    position: absolute; /* Este position absolute hace que el elmento c3 pierda la referencia hacia c2 y se referencie con c1*/
    top: 0%;
    left: 10%;
    z-index:-1;

}

#c3 {
    background-color: green;
}

```