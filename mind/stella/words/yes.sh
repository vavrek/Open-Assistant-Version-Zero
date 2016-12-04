#!/bin/bash

# yes.sh

TOPIC=$(echo $(cat ./mind/stella/words/topic))

case $TOPIC in
"none")
  echo "ok..." | $VOICE
  ;;
"diagnostics")
  ./mind/stella/words/diagnostics.sh
  ;;
"jokes")
 shuf -n 1 ./mind/stella/words/jokes | tee /dev/tty | $VOICE
  ;;
esac
