#!/bin/bash

#echo "defina su numero"
#read numero

read -p "Defina el numero" numero

if [ $numero -le 200 ]
then 
echo "Es menor o igual que 200"
else
echo "Es mayor que 200" 
fi


