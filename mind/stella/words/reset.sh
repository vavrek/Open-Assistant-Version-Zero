#!/bin/bash

kill -9 `ps -A | awk ' ($4=="oa.py") {print $1}'`

# pkill -o -f oa.py

python3 /home/vav/stella/oa.py -c -m 0