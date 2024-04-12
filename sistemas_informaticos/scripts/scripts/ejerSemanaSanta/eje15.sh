#!/bin/bash

num1=$1
num2=$2

echo "La suma de $num1 + $num2 es igual a: $((num1 + num2 ))"
echo "La resta de $num1 - $ num2 es igual a: $((num1 - num2))"
if [ $num2 -ne 0 ]; then echo "La division de $num1 / $num2 es igual a: $((num1/num2))"; else echo "La división por cero no es valida"; fi
echo "La multiplicación de $num1 * $num2 es igual a: $((num1*num2))"
if [ $num2 -ne 0 ]; then echo "El resto de la division de $num1 / $num2 es igual a: $((num1%num2))"; else echo "La diviión por cero no es valida"; fi

