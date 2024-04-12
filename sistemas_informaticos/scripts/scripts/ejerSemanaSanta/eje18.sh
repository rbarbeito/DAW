#!/bin/bash

clear
echo "Calculo de la potencia"
read -p "Diga la base: " base
read -p "Diga la potencia: " potencia

echo "la potencia de $base elevado a la $potencia es igual a: $((base**potencia))" 
