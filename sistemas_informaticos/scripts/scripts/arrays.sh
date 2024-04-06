#!/bin/bash


names=( "juan" "pepe" "maria" )
echo $names

echo "Todos los items: ${names[*]}"

echo "Todos los items: ${names[@]}"

echo "Item 0: ${names[0]}"  
echo "${names[1]}"  
echo "${names[2]}"  


echo "Idices negativos: ${names[-1]}"  
echo "${names[-2]}"  
echo "${names[-3]}"  


echo "Los indices son: ${!names[@]}"


echo "Total de elementos: ${#names[*]}"
echo "Total de elementos: ${#names[@]}"


echo "Ultimo indice, sin indices negativos: ${names[${#names[@]}-1]}"
echo "Ultimo indice, sin indices negativos: ${names[${#names[*]}-1]}"

echo "barriendo con un for los elementos"
for i in ${names[@]}
do
echo $i
done


#delete items
unset names[1]
echo ${names[@]}


# insertar elementos
names[${#names[@]}]="la mierda"
echo ${names[@]}

