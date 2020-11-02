#!/bin/bash

kill -9 `ps -A | awk ' ($4=="oa.py") {print $1}'`

# pkill -o -f oa.py

./oa.sh
