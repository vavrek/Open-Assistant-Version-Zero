#!/bin/bash

# Shuffle Script By Jonathan Kulp . http://jonathankulp.org

# good.sh

good=./good

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

echo "$(cat $good)" | $VOICE

# rm $good $name
