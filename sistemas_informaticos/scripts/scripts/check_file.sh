#!/bin/bash
 
clear

read -p "Teclee el nombre del archivo: " archivo

if [ ! -f "$archivo" ]; then 
	read -p "No existe el archivo, desea crearlo (s/n) :" op
	if [ "$op" = 's' ]; then
		read -p "Desea incluirle algun texto: (s/N) " text
		if [ "$text" = 's' ]; then
			read -p "Teclea el contenido inicial: " contenido
			touch $archivo && echo $contenido >> $archivo
			clear
	                echo "Contenido del archivo" && echo ""
        	        cat $archivo
		else
			touch $archivo
		fi
	else
		echo "Nada más que hacer"
	fi
else
	read -p "El archivo existe, desea agregar algun texto: (s/n)" text
	if [ "$text" = "s" ]; then
		read -p "Teclea el contenido inicial: " contenido
		echo $contenido >> $archivo
		clear
		echo "Contenido del archivo" && echo ""
		cat $archivo
	fi
fi





