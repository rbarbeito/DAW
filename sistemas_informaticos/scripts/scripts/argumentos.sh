#! /bin/bash

echo "todo en una"
echo $@
echo $*

echo "De string a lista"
args=("$@")
echo "Result: ${args[0]}, ${args[1]}, ${args[1]}"
