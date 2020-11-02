#!/bin/bash

# Stella's Age Script

# Stella's Birthday == 10/01/2016

birth_year=2016
birth_month=10
birth_day=01

year_now=$(date '+%Y')
month_now=$(date '+%m')
day_now=$(date '+%d')

age_year=$(($year_now-$birth_year))
age_month=$(($month_now-$birth_month))
age_day=$(($day_now-$birth_day))

if [ $age_month -lt 0 ] ; then
   age_month=$(($month_now-$birth_month+12))
else
   age_month=$(($month_now-$birth_month))
fi

if [ $age_day == 1 ] ; then
   day="day"
else
   day="days"
fi

if [ $age_month == 1 ] ; then
   month="month"
else
   month="months"
fi

if [ $birth_month == $month_now ] && [ $birth_day == $day_now ] ; then
	echo "Today is my birthday! I am $age_year years old." | tee /dev/tty | $VOICE
elif [ $age_day == 0 ] ; then
    echo "My birthday is October First, Twenty-Sixteen. I am $age_year years and $age_month $month old."  | tee /dev/tty | $VOICE
elif [ $age_month = 0 ] ; then
	echo "My birthday is October First, Twenty-Sixteen. I am $age_year years and $age_day $day old."  | tee /dev/tty | $VOICE
else 
	echo "My birthday is October First, Twenty-Sixteen. I am $age_year years, $age_month $month, and $age_day $day old."  | tee /dev/tty | $VOICE
fi


