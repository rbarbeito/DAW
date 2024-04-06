#!/bin/bash

cd ~/SSII/scripts/ejerSemanaSanta
touch $1
chmod +x $1
echo "#!/bin/bash" > $1
echo " ">>$1
nano $1
