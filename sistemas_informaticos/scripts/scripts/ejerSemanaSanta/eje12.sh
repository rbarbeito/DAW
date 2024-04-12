#!/bin/bash

read -p "Teclee su primero número: " numero1
read -p "Teclee su segundo número: " numero2

if [[ $numero1 -gt $numero2 ]]; then
echo "La resta de ambos numero es $((numero1 - numero2))"
else
echo "Los números no se pueden restar"
fi 
