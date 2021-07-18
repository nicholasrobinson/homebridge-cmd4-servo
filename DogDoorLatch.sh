#!/bin/bash

# Script for controlling a servo using pigpio.
# Usage: bash DogDoorLatch.sh Set <LATCH/UNLATCH> On 1

if [ "$1" = "Get" ]; then
    if [ "$3" = "Name" ]; then
        echo "$2"
        exit 0
    else
        # Stateless switch is always off
        echo "0"
        exit 0
    fi
fi

if [ "$1" = "Set" ]; then
   if [ "$3" = "On" ]; then
      if [ "$4" = "1" ]; then
         # Execute dog_door_latch.py
         ./dog_door_latch.py "$2"
         exit $?
      else
         # There is no turning off a command
         exit 0
      fi
   fi
fi

exit -1
