#!/bin/bash


read -p "Teclea tu edad" age


if [ $age -ge 18 ] 
then
 echo 'Eres un adulto cagon para que los niños pinchen los mojones'
elif [ $age -lt 18 -a $age -ge 13 ]
then
  echo 'ahora te comes los mojones que pinchaste de niño'
else
  echo "eres un pincha mojon"
fi


while [ $age -lt 18 ]
do
  echo "edad: $age"
  let age=$age+1
done






