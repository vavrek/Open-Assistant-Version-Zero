#!/bin/bash

# OpenAssistant 0.04
# 2016 General Public License V3
# By Andrew Vavrek, Clayton G. Hobbs, Jezra, Jonathan Kulp

# Stella's Age Script

# birthday.sh
# import dateutil *

# from dateutil.relativedelta import relativedelta

BIRTHDAY=10/01/2016

days_old=$(( ( $(date +%s) - $(date -d "$BIRTHDAY" +%s) ) /(24 * 60 * 60 ) ))

years_old=days_old / 365

echo "My birthday is October first, twenty sixteen. I am" $years_old "years old." | tee /dev/tty | $VOICE


#rdelta = relativedelta(now, birthdate)
#print 'Age in years - ', rdelta.years
#print 'Age in months - ', rdelta.months
#print 'Age in days - ', rdelta.days