#!/bin/bash

echo "escoge el valor 1, 2, 3: "
read valor

case $valor in
  1)
    echo "Imprimiste el 1"
    ;;
  2)
    echo "Imprimiste el 2"
    ;;
  *)
    echo "Error"
    ;;
esac


