#!/bin/bash

# OpenAssistant 0.03
# 2016 General Public License V3
# By Andrew Vavrek, Clayton G. Hobbs, Jezra, Jonathan Kulp

# yes.sh 

TOPIC=$(echo $(cat $CONFIGDIR/topic))

if [[ $TOPIC == "diagnostics" ]]; 
	then
	echo "ok... running diagnostics" | $VOICE
elif [[ $TOPIC == "jokes" ]]
	then
	echo "ok... here is a joke... why did the chicken cross the road... roll around in the dirt... then cross back over again..." | $VOICE 
	echo "because he was a dirty... double... crosser..." | $VOICE
else 
	echo ok... yes... | $VOICE
fi

echo "none" > $CONFIGDIR/topic
