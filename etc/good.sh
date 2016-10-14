#!/bin/bash

# good.sh

good=$CONFIGDIR/good.txt
name=$CONFIGDIR/name.txt

shuf -n1 > $good <<EOFgood
awesome
cool
excellent 
fantastic 
good 
great 
lovely
nice
wonderful
EOFgood

shuf -n1 > $name <<EOFname
$USERNAME... 
 
EOFname

response=$(echo "$(cat $good) $(cat $name)")

echo $response | $VOICE

# rm $good $name
