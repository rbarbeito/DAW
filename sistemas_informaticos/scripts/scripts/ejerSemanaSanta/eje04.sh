#!/bin/bash

for (( i=0; i < 16; i++  ))
do
if [ $((i%3)) = 0 ]; then
echo "El número $i es multiplo de 3"
else
echo "El número $i no es multiplo de 3"
fi
done

