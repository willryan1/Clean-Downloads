#!/usr/bin/env bash

if [ "$1" != "" ]; then
  chmod +x "$1"
  nohup "$1" > output.log &
  pgrep -f "$1" > pid.txt
else
  echo "Positional parameter for the path to the clean.py does not exist"
fi