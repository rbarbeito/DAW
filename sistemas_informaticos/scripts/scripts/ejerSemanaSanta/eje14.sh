#!/bin/bash

clear
read -p "Defina el primer número: " num1
read -p "Defina el segundo número: " num2

menu=10
length=0
list_menu=("Menú" "1.-Suma" "2.-Resta" "3.-Multiplicacion" "4.-Division" "5.-¿Es el primer numero par?" "6.-¿Es el segundo número par?" " " "0.-Salir")

for ((i=0; i<${#list_menu[@]}; i++)); do

	#item="${list_menu[$i]}"

	if [[ "${#list_menu[i]}" -gt  "$length" ]]; then
		length=${#list_menu[i]}
	fi
done

star='**'
for ((i=0; i<$length;i++)); do
	star="${star}*"
done
star="${star}**"

#echo ""
#echo "${star}"



while [[ $menu -ne 0 ]]; do
	
	echo ""
	echo "${star}"

	for ((i=0;i<${#list_menu[@]};i++)); do
		echo "  ${list_menu[i]}"
	done
	echo "${star}"
	echo " "
	read -p "Que acción desea realizar: " menu

	clear

	case $menu in
		1)
			echo "La suma de $num1 + $num2 es: $((num1 + num2))"
		;;
		2)
			echo "La resta de $num1 - $num2 es: $(($num1 - $num2))"
		;;
		3)
			echo "La Multiplicación de $num1 * $num2 es: $(($num1 * $num2))"
		;;
		4)
			if [ $num2 -ne 0 ] ; then
				echo "La division de $num1 / $num2 es: $(($num1/$num2))"; else
				echo "Division por cero no permitida"; fi
		;;
		5)
			if [ $((num1%2)) -eq 0 ] ; then
				echo "$num1 es par"; else
				echo "$num1 es impar"; fi
		;;
		6)
			if [ $((num2%2)) -eq 0 ]; then
				echo "$num2 es par"; else
				echo "$num2 es impar"; fi
		;;
		0)
		 	echo "Hasta la vista Baby!!!"
		;;
		*)
			echo "Opción no disponible"
		;;
	esac

done	
