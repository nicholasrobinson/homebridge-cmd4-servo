# Motivation

I wanted to control a servo to latch and unlatch my dog door using Homebridge. This simple script allows a switch to be used for this purpose.

# Example config.json

```
...
    {
        "platform": "Cmd4",
        "name": "Cmd4",
        "accessories": [
            {
                "type": "Switch",
                "displayName": "LATCH",
                "on": "FALSE",
                "name": "Dog Door Servo - Latch",
                "state_cmd": "/var/lib/homebridge/Cmd4Scripts/DogDoorLatch.sh"
            },
            {
                "type": "Switch",
                "displayName": "UNLATCH",
                "on": "FALSE",
                "name": "Dog Door Servo - Unlatch",
                "state_cmd": "/var/lib/homebridge/Cmd4Scripts/DogDoorLatch.sh"
            }
        ]
   }
...
```

# Example dog_door_latch.py

You will need to specify the GPIO pins for power/pwm and the pulse width for the off/on positions:
```
GPIO_POWER_PIN = 4
GPIO_PWM_PIN = 12
UNLOCK_PULSE_WIDTH = 500
LOCK_PULSE_WIDTH = 1400
```
