#!/bin/bash

# OpenAssistant 0.03
# 2016 General Public License V3
# By Andrew Vavrek, Clayton G. Hobbs, Jezra, Jonathan Kulp

# yes.sh

TOPIC=$(echo $(cat $CONFIGDIR/topic))

case $TOPIC in
"none")
  echo "ok... yes..." | $VOICE
  ;;
"diagnostics")
  $BINDIR/diagnostics.sh
  ;;
"jokes")
 echo "ok... here is a joke... why did the chicken cross the road..." | $VOICE
 echo "roll around in the dirt..."  | $VOICE
 echo "and then cross back over again..." | $VOICE
 sleep 1
 echo "because this chicken was a dirty double crosser..." | $VOICE
 echo "none" > $CONFIGDIR/topic
  ;;
esac
