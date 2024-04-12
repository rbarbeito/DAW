#!/bin/bash
 
clear

echo "Dime el nombre del directorio a crear: "
read folder

if [ -d "$folder" ]
then
	echo "El directorio $folder existe"
else
	echo "El directorio $folder no existe"
	read -p "¿Le gustaria crearlo? (s/N) " op

	if [ "$op" = "s" ]; then
		mkdir $folder
		echo "$folder creado correctamente"
		ls -d */
	fi
fi 
 

echo "Dime el nombre del directorio a borrar: "
read folder

if [ ! -d "$folder" ]
then
        echo "El directorio $folder no existe"
else
        echo "El directorio $folder existe"
        read -p "¿Le gustaria borrarlo? (s/N) " op

        if [ "$op" = "s" ]; then
                rm -rf $folder
                echo "$folder borrado correctamente"
                ls -d */
        fi
fi

