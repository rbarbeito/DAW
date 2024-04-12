#!/bin/bash
 
clear

read -p "Teclee su nombre: " nombre

if [ $nombre = $USER ]; then echo "Bienvenido $USER"; else echo "Eres un impostor"; fi


