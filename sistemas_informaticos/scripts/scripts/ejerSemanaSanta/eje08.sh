#!/bin/bash
 

read -p "Teclee su numero: " numero

if [ $numero -ge 0  ] && [ $numero -le 10 ]; then
echo "El numero $numero este entre cero y diez"
else
echo "El numero $numero  no est en el rango de ceo a 10"
fi
