#!/bin/bash

# thanks.sh

thanks=$CONFIGDIR/thanks
name=$CONFIGDIR/name

shuf -n1 > $thanks <<EOFthanks
thanks
thank you
much appreciated
you bet
sure
a pleasure
cheers
EOFthanks

shuf -n1 > $name <<EOFname
$USERNAME... 
 
EOFname

response=$(echo "$(cat $thanks) $(cat $name)")

echo $response | $VOICE

# rm $thanks $name
