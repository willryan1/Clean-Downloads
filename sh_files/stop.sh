#!/usr/bin/env bash

if [ "$1" != "" ]; then
  pkill -f "$1"
  # shellcheck disable=SC2188
  >pid.txt
else
  echo "Positional parameter for the path to the clean.py was not included"
fi