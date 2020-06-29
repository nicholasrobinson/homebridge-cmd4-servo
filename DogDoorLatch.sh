#!/bin/bash

# Script for controlling a servo using pigpio.
# Usage: bash DogDoorLatch.sh Set <LATCH/UNLATCH> On true

if [ "$1" = "Get" ]; then
   # Stateless switch is always off
   echo "0"
   exit 0
fi

if [ "$1" = "Set" ]; then
   if [ "$3" = "On" ]; then
      if [ "$4" = "true" ]; then
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
