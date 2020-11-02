#!/bin/bash

# oa.sh - Open Assistant Launch Script

# Command Variables

export AUDIOPLAYER="aplay"
export BROWSER="screen -d -m firefox"
export CLICK="xdotool click"
export EMAIL="screen -d -m thunderbird"
export KEYPRESS="xdotool key"
export LAUNCH="python3 ./oa.py -c -m 0"
export MASTERPASS="masterpassword"
export MINDDIR="$PWD/mind/stella"
export MESSENGER="screen -d -m caprine"
export PASSWORD="password"
export SEARCHFILES="catfish"
export SEARCHWEB="https://duckduckgo.com"
export TYPE="xdotool type"
export USERNAME=$(whoami)
export VOICE="flite -voice slt --setf int_f0_target_mean=263 --setf duration_stretch=1.11 --setf int_f0_target_stddev=27"
export TERMINAL="screen -d -m xfce4-terminal"
export TEXTEDIT="screen -d -m subl"
export WINCLOSE="wmctrl -c"
export WINGO="wmctrl -a"

# Launch Open Assistant

python3 ./oa.py -c -m 0
