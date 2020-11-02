#!/bin/bash

# Shuffle Script By Jonathan Kulp . http://jonathankulp.org

# thanks.sh

thanks=$MINDDIR/words/thanks
name=$MINDDIR/words/name

shuf -n1 > $thanks <<EOFthanks
thanks
thanks so much
thank you
much appreciated
you bet
sure
a pleasure
you are very kind
EOFthanks

shuf -n1 > $name <<EOFname
$USERNAME...

EOFname

response=$(echo "$(cat $thanks) $(cat $name)")

echo $response | $VOICE

# rm $thanks $name
