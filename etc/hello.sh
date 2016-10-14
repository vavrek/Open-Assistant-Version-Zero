#!/bin/bash

# hello.sh

greeting=$CONFIGDIR/greeting.txt
name=$CONFIGDIR/name.txt
question=$CONFIGDIR/question.txt

shuf -n1 > $greeting <<EOFgreeting
cheers 
greetings 
hello 
hello again 
hello there 
hey 
hey there 
hi 
hi again 
hi there 
yes
EOFgreeting

shuf -n1 > $name <<EOFname
$USERNAME... 
...
EOFname

shuf -n1 > $question <<EOFquestion
how are you?
how can i help you?
how's it going?
how are things?
how are you feeling?
how can i help you?
what would you like to do?
what's going on?
 
EOFquestion

response=$(echo "$(cat $greeting) $(cat $name) $(cat $question)")

echo $response | $VOICE

# rm $greeting $name $question
