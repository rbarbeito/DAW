#!/bin/bash
 
clear

echo "Comparando cadenas de texto"
read -p "introduzca su primera cadena de texto: " cadena1
read -p "Teclee su segunda cadena de texto: " cadena2

if [ $cadena1 = $cadena2 ]; then echo "las cadenas son iguales"; else echo "Las cadenas son diferentes"; fi

