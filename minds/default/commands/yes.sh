#!/bin/bash

# OpenAssistant 0.04
# 2016 General Public License V3
# By Andrew Vavrek, Clayton G. Hobbs, Jezra, Jonathan Kulp

# yes.sh

TOPIC=$(echo $(cat $OA_PERSONALITY_DIR/etc/topic))

case $TOPIC in
"none")
  echo "ok..." | $VOICE
  ;;
"diagnostics")
  $OA_PERSONALITY_DIR/commands/diagnostics.sh
  ;;
"jokes")
 shuf -n 1 $OA_PERSONALITY_DIR/docs/jokes.txt | tee /dev/tty | $VOICE
 echo "none" > $OA_PERSONALITY_DIR/etc/topic
  ;;
esac
