#!/bin/bash

# OpenAssistant 0.03
# 2016 General Public License V3
# By Andrew Vavrek, Clayton G. Hobbs, Jezra, Jonathan Kulp

# diagnostics.sh

echo "ok... running diagnostics..." | $VOICE &

# Processor Temperature
cputemp=$(sensors | grep "id 0" | awk -F "id 0: " '{print $2}' | awk -F "°C " '{print $1}' | sed 's/ +//') && echo "proccessor temperature is currently $cputemp degrees centegrade" | $VOICE

# Memory Free
freemem=$(free -h | grep "Mem:" | awk -F "Mem: " '{print $2}' | awk '{print $3}' | sed 's/G//') && echo "system memory has $freemem giga bytes free" | $VOICE

# Drive Space Free
space=$(df -h /dev/sda1 | awk '{print $4}' | grep G | cut -d "G" -f1 -) && echo "internal drive has $space giga bytes free" | $VOICE

# Network Status
./bin/nettest.py | $VOICE

echo "none" > $CONFIGDIR/topic
