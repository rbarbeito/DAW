#!/bin/bash

echo "" > primos.txt
count=1
number=2
while [[ $count -le 10 ]]; do
	primo=True
	for ((i=2; i<=$((number/2)); i++)); do
		if [[ $((number%i)) -eq 0 ]]; then
			primo=False
			break
		fi
	done

	if [[ $primo = True ]]; then
		echo $number >> primos.txt
		((count+=1))
	fi
	((number+=1))

done

cat primos.txt
