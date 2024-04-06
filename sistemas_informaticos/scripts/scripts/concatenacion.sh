#!/bin/bash

echo "enter name"
read name

echo "write an adjective"
read adjective


result="$name is $adjective" 
echo $result

result="${name}___ is ${adjective}"
echo $result

result="${name}ito is ${adjective}"
echo $result

#pasar a minusculas
echo ${name,,}

#pasa a mayusculas
echo ${name^^}


echo ${name,,[AEIOU]} # Pasa a minuculas todas las letras que estan en los corchetes y  que esten mayusculas

