#!/bin/bash

# OpenAssistant 0.03
# 2016 General Public License V3
# By Andrew Vavrek, Clayton G. Hobbs, Jezra, Jonathan Kulp

# assist.sh - Assistant Launch Script

# Global Variables

export ASSISTNAME="stella"
export USERNAME="andrew"
export VOICE="/usr/bin/festival --tts"
export BROWSER="firefox"
export CONFIGDIR="./etc"
export KEYPRESS="xvkbd -xsendevent -secure -text"
export TERMINAL="xfce4-terminal -x"

# Gstreamer Library Path

export GSTREAMER_LIB_PATH=/usr/lib/gstreamer-1.0

# Make Binary Files Executable

chmod -R +x ./bin/*

# Make Configuration Files Writable & Executable

chmod -R +wx ./etc/*

# Replace All Instances of 'ASSISTNAME' In Command File

sed -i -e 's/$ASSISTNAME/stella/g' $CONFIGDIR/commands.json

# Launch OpenAssistant In Continuous Mode
# With History Of 20 Recent Commands

python3.5 assistant.py -c -H 20

# Launch Gui (Buggy): use "./assistant.py -i G"
# Launch In 'Continuous' Listen Mode: add "-C"
# Use Mic Other Than System Default: add "-m <device Number>"
# Find Mic Device Number: "cat /proc/asound/cards" Or "arecord -l"
# Pass Each Word As A Separate Argument: add "-p"
# Run Command Each Valid Sentence: "--valid-sentence-command=/path/to/command"
# Run Command Each Invalid Sentence: "--invalid-sentence-command=/path/to/command"

# Default Arguments Configured In "./etc/commands.json"
