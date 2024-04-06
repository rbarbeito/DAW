#!/bin/bash
 

read -p "Diga su numero: " numero

for (( i=0; i<($numero+1); i++))
do
echo $i
done
