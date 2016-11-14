#!/bin/sh

# OpenAssistant 0.04
# 2016 General Public License V3
# By Andrew Vavrek, Clayton G. Hobbs, Jezra, Jonathan Kulp

# assist.sh - Assistant Launch Script

# Environment Configuration
ROOT=$( cd $(dirname $0) ; pwd -P )
MINDDIR="$ROOT/mind/empty"


# Use system speech synthesizer on macOS
if [[ "`uname`" == "Darwin" ]]
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