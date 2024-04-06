#!/bin/bash

echo 10+20 
echo $((10+20))


x=10
y=20

echo $((x + y))
echo $((x - y))
echo $((x * y))
echo $((x / y))
echo $((x % y))


echo $(expr $x + $y)
echo $(expr $x - $y)
echo $(expr $x / $y)
echo $(expr $x \* $y)
echo $(expr $x % $y)
