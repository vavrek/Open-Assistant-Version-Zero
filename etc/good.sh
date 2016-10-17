#!/bin/bash

# OpenAssistant 0.03
# 2016 General Public License V3
# By Andrew Vavrek, Clayton G. Hobbs, Jezra, Jonathan Kulp

# Shuffle Script By Jonathan Kulp . http://jonathankulp.org

# good.sh

VOICE="/usr/bin/festival --tts"

good=$CONFIGDIR/good
name=$CONFIGDIR/name

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
