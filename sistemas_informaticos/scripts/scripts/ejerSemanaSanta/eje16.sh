#!/bin/bash

read -p "De que número desea la tabla de multiplicar: " numero

for ((i=0; i<11; i++)); do
echo "$numero x $i = $((numero*i))"
done 
