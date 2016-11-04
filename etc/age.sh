#!/bin/bash

# OpenAssistant 0.03
# 2016 General Public License V3
# By Andrew Vavrek, Clayton G. Hobbs, Jezra, Jonathan Kulp

# Stella's Age Script

# birthday.sh

BIRTHDAY=10/01/2016

days_old=$(( ( $(date +%s) - $(date -d "$BIRTHDAY" +%s) ) /(24 * 60 * 60 ) ))

echo "I am" $days_old "days old." | tee /dev/tty | $VOICE


