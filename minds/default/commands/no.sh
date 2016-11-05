#!/bin/bash

# OpenAssistant 0.04
# 2016 General Public License V3
# By Andrew Vavrek, Clayton G. Hobbs, Jezra, Jonathan Kulp

# no.sh

TOPIC=$(echo $(cat $CONFIGDIR/topic))

if [ $TOPIC = "diagnostics" ]; then
	echo "ok... fine..." | $VOICE
else
	echo "ok..." | $VOICE
fi

echo "none" > $OA_MIND_DIR/etc/topic
