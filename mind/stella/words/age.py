#!/bin/bash

# Stella's Age Script

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
