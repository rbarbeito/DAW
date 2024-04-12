#!/bin/bash

cd ~/SSII/scripts
touch $1
chmod +x $1
echo "#!/bin/bash" > $1
echo " ">>$1
echo "clear">>$1
nano $1
