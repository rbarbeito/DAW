#!/bin/bash


echo "Introduce el pass:"
read input1

echo "Introduce el pass2:"
read input2

echo "$input1 $input2"


if [ $input1 = $input2 ]
then
  echo "Passwprd Correcto"
else
  echo "wrong password"
fi
