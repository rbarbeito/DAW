#!/bin/bash
 
clear


read -p "Dame una url para visitar o descargar: " url

#curl $url > users.json

#cat users.json


curl url > imagen.jpg
