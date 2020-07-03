#!/usr/bin/env python
import sys
import time
import pigpio

# Note: Pinout
# https://i.stack.imgur.com/yHddo.png
# Note: Hardware PWM available on GPIO12, GPIO13, GPIO18, GPIO19 
# https://www.raspberrypi.org/documentation/usage/gpio/
GPIO_POWER_PIN = 4
GPIO_PWM_PIN = 12
UNLOCK_PULSE_WIDTH = 500
LOCK_PULSE_WIDTH = 1400

GPIO_HIGH = 1
GPIO_LOW = 0

pi = pigpio.pi()

pi.set_mode(GPIO_POWER_PIN, pigpio.OUTPUT)
pi.set_mode(GPIO_PWM_PIN, pigpio.OUTPUT)

pi.write(GPIO_POWER_PIN, GPIO_HIGH)
if sys.argv[-1] == 'LATCH':
    # Latch
    pi.set_servo_pulsewidth(GPIO_PWM_PIN, LOCK_PULSE_WIDTH)
else:
    # Unlatch
    pi.set_servo_pulsewidth(GPIO_PWM_PIN, UNLOCK_PULSE_WIDTH)
time.sleep(1)
pi.write(GPIO_POWER_PIN, GPIO_LOW)

pi.stop()