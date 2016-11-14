# Language: Python
# File name: Photoresistor_LED.py
# Description: This will toggle the LED if the photoresistor is contact with enough light
import RPi.GPIO as GPIO
import time

# Tells the GPIO library to use Broadcom references
GPIO.setmode(GPIO.BCM)
# Disables warnings
GPIO.setwarnings(False)
# Tells the pi which pin will be in use
GPIO.setup(18,GPIO.OUT)

# Define function to measure charge time
def RCtime (PiPin):
  measurement = 0
  # Discharge capacitor
  GPIO.setup(PiPin, GPIO.OUT)
  GPIO.output(PiPin, GPIO.LOW)
  time.sleep(0.1)

  GPIO.setup(PiPin, GPIO.IN)
  # Count loops until voltage across
  # Capacitor reads high on GPIO
  while (GPIO.input(PiPin) == GPIO.LOW):
    measurement += 1

  return measurement



# Main program loop
while (True):
  photo_time = RCtime(4)
  LED_state = False
  if (photo_time >= 600 and state == False):
    # Prints "LED on" before the LED turns on
    print "LED on"

    # Turns on the LED
    GPIO.output(18,GPIO.HIGH)

  elif (photo_time < 600):
    # Prints "LED off" before turning the LED off
    print "LED off"

    # Turns off the LED
    GPIO.output(18,GPIO.LOW)

  else:
    # This continues the loop after a short delay
    time.sleep(.2)
    continue
