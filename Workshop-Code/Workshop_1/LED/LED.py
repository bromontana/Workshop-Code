# Language: Python
# File name: LED.py
# Description: This will toggle an LED for 1 second then turn it off

import RPi.GPIO as GPIO
import time

# Tells the GPIO library to use Broadcom references
GPIO.setmode(GPIO.BCM)

# Disables warnings
GPIO.setwarnings(False)

# Tells the pi which pin will be in use
GPIO.setup(18,GPIO.OUT)

# Prints "LED on" before the LED turns on
print "LED on"

# Turns on the LED
GPIO.output(18,GPIO.HIGH)

# Waits one second
time.sleep(1)

# Prints "LED off" before turning the LED off
print "LED off"

# Turns off the LED
GPIO.output(18,GPIO.LOW)
