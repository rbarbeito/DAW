#!/bin/bash

read -p "introduzca su número: " numero 

if [[ $numero -eq 0 || $numero -eq 1 ]]; then
echo "$numero no es primo"
else
	primo=true
	for ((i=2; i<=$((numero/2)); i++)); do
		if [ $((numero%i)) -eq 0 ]; then
			primo=false
			break
		fi
		done
	if [[ $primo = true ]]; then
		echo "$numero es primo"
	else
		echo "$numero no es primo"
	fi	

fi

