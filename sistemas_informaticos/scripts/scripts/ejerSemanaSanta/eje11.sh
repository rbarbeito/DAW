#!/bin/bash

read -p "Diganos su edad: " edad

if [[ $edad -lt 10 ]]; then
echo "Eres muy joven"

elif [[ $edad -ge 10 && $edad -le 25 ]]; then
echo "Que mala edad tienes"
else
echo "Que bien te veo"
fi
 
