#!/bin/bash

read -p "Defina un numero: " numero  


case $numero in
	0|10) echo "numero incorrecto";;
	[1-9]) echo "Dijiste $numero";;
	*) echo "Numero no reconocido";;
esac
