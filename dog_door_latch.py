#!/usr/bin/env python
import sys
import pigpio

# Note: Pinout
# https://i.stack.imgur.com/yHddo.png
# Note: Hardware PWM available on GPIO12, GPIO13, GPIO18, GPIO19 
# https://www.raspberrypi.org/documentation/usage/gpio/
GPIO_PIN = 12
UNLOCK_PULSE_WIDTH = 500
LOCK_PULSE_WIDTH = 1400

pi = pigpio.pi()

pi.set_mode(GPIO_PIN, pigpio.OUTPUT)

if sys.argv[-1] == 'LATCH':
    # Latch
    pi.set_servo_pulsewidth(GPIO_PIN, LOCK_PULSE_WIDTH)
else:
    # Unlatch
    pi.set_servo_pulsewidth(GPIO_PIN, UNLOCK_PULSE_WIDTH)

pi.stop()