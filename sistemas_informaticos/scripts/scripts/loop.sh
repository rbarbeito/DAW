\#!/bin/bash

number=0

while [ $number -lt 10 ]
do
  echo $number
  number=$((number + 1))
done

until [ $number -gt 100 ]
do
  echo $number
  number=$((number**2))
done


