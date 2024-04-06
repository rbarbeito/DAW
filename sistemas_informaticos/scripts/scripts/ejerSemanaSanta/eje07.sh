#!/bin/bash

read -p "entre el numero: " numero

counter=0

until [ $counter -gt $numero ]
do
	echo Counter: $counter
	((counter++))
done 
