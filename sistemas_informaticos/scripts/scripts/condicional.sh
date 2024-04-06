#!/bin/bash

age=20

if [ $age -eq 20 ]
then
  echo "los números son iguales"
fi


if (( age == 20 ))
then
  echo "el numero es igual"
else
  echo "el numero es distinto"
fi



