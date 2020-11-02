#!/bin/bash

# OpenAssistant 0.04
# 2016 General Public License V3
# By Andrew Vavrek, Clayton G. Hobbs, Jezra, Jonathan Kulp

# no.sh

TOPIC=$(echo $(cat $MINDDIR/words/topic))

if [ $TOPIC = "diagnostics" ]; then
	echo "ok... no diagnostics..." | $VOICE
else
	echo "ok..." | $VOICE
fi
