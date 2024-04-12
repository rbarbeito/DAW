#!/bin/bash

for ((i=1;i<11;i++)); do
	echo "Tabla del $i"
	echo "************"
	for((j=0;j<11;j++ )); do
		echo "$i x $j = $((i*j))"
	done
	echo ""
done 
