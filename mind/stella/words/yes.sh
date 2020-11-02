#!/bin/bash

# OpenAssistant 0.04
# 2016 General Public License V3
# By Andrew Vavrek, Clayton G. Hobbs, Jezra, Jonathan Kulp

# yes.sh

TOPIC=$(echo $(cat $MINDDIR/words/topic))

case $TOPIC in
"none")
  echo "ok..." | $VOICE
  ;;
"diagnostics")
  $MINDDIR/words/diagnostics.sh
  ;;
"jokes")
 shuf -n 1 $MINDDIR/words/jokes | tee /dev/tty | $VOICE
  ;;
esac
