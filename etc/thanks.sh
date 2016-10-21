#!/bin/bash

# OpenAssistant 0.03
# 2016 General Public License V3
# By Andrew Vavrek, Clayton G. Hobbs, Jezra, Jonathan Kulp

# Shuffle Script By Jonathan Kulp . http://jonathankulp.org

# thanks.sh

thanks=$CONFIGDIR/thanks
name=$CONFIGDIR/name

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
