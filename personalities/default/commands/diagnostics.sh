#!/bin/bash

# OpenAssistant 0.04
# 2016 General Public License V3
# By Andrew Vavrek, Clayton G. Hobbs, Jezra, Jonathan Kulp

# diagnostics.sh

echo "Running Diagnostics:" &

echo "ok... running diagnostics..." | $VOICE &

# Processor Temperature
cputemp=$(sensors | grep "id 0" | awk -F "id 0: " '{print $2}' | awk -F "°C " '{print $1}' | sed 's/ +//') && echo "Proccessor temperature is currently $cputemp degrees Centegrade..." | tee /dev/tty | $VOICE

# Memory Free
freemem=$(free -h | grep "Mem:" | awk -F "Mem: " '{print $2}' | awk '{print $3}' | sed 's/G//') && echo "System memory has $freemem Gigabytes free..." | tee /dev/tty | $VOICE

# Drive Space Free
space=$(df -h /dev/sda1 | awk '{print $4}' | grep G | cut -d "G" -f1 -) && echo "Internal hard drive has $space Gigabytes free..." | tee /dev/tty | $VOICE

# Network Status
$OA_PERSONALITY_DIR/commands/nettest.py | tee /dev/tty | $VOICE

echo "none" > $OA_PERSONALITY_DIR/etc/topic
