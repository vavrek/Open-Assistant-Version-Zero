#!/bin/bash

# OpenAssistant 0.03
# 2016 General Public License V3
# By Andrew Vavrek, Clayton G. Hobbs, Jezra, Jonathan Kulp

# yes.sh

TOPIC=$(echo $(cat $CONFIGDIR/topic))

case $TOPIC in
"none")
  echo "ok..." | $VOICE
  ;;
"diagnostics")
  $CONFIGDIR/diagnostics.sh
  ;;
"jokes")
 shuf -n 1 ./docs/jokes.txt | tee /dev/tty | $VOICE
 echo "none" > $CONFIGDIR/topic
  ;;
esac
