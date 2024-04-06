#!/bin/bash

for (( i=0 ; i<16; i++))
do
if [ $((i%2)) = 0 ]; then
echo "El numero $i es multiplo por 2" 
else
echo "El número $i no es multiplo de 2"
fi
done
