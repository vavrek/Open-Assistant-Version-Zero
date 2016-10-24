#!/bin/bash

# OpenAssistant 0.03
# 2016 General Public License V3
# By Andrew Vavrek, Clayton G. Hobbs, Jezra, Jonathan Kulp

# Shuffle Script By Jonathan Kulp . http://jonathankulp.org

# good.sh

good=$CONFIGDIR/good

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
