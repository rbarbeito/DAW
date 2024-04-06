#!/bin/bash

read -p "Diga su numero: " numero 

if [ $(( numero%2 )) = 0 ]; then
echo "El numero $(($numero)) es par"
else
echo "El numero es impar"
fi


