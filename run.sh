#!/bin/sh

# OpenAssistant 0.10
# 2016 General Public License V3
# By Andrew Vavrek, Clayton G. Hobbs, Jezra, Jonathan Kulp

# run.sh - Open Assistant Launch Script

# Environment Configuration
export USERNAME=$(whoami)
export ROOT=$( cd $(dirname $0) ; pwd -P )
export MINDDIR="$ROOT/mind/boot"
export BROWSER="firefox"
export KEYPRESS="xvkbd -xsendevent -secure -text"
export TERMINAL="tmux new-window "

# Use system speech synthesizer on macOS
if [[ "uname" == "Darwin" ]]
then
	export VOICE="say"
else
	export VOICE="/usr/bin/festival --tts"
fi

# Launch OpenAssistant
# 	-c	In ContinuousMode
# 	-H 20	With HistoryLength 20
# 	-m 0	With InputDevice 0
#	--mind "$MINDDIR"
python3.5 "$ROOT/run.py" $@
