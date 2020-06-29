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
                "name": "Dog Door Latch",
                "state_cmd": "/var/lib/homebridge/Cmd4Scripts/DogDoorLatch.sh",
                "polling": true,
                "interval": 5,
                "timeout": 60000
            },
            {
                "type": "Switch",
                "displayName": "UNLATCH",
                "on": "FALSE",
                "name": "Dog Door Unlatch",
                "state_cmd": "/var/lib/homebridge/Cmd4Scripts/DogDoorLatch.sh",
                "polling": true,
                "interval": 5,
                "timeout": 60000
            }
        ]
   }
...
```

# Example dog_door_latch.py

You will need to specify the GPIO pin and the pulse width for the off/on positions:
```
GPIO_PIN = 12
UNLOCK_PULSE_WIDTH = 500
LOCK_PULSE_WIDTH = 1400
```
