# Language: Python
# File name: photoresistor.py
# Description: This will print out the amount of time (in ms) that it takes for the capacitor to fully charge at 3.3V

import RPi.GPIO as GPIO, time

# Tell the GPIO library to use Broadcom GPIO references
GPIO.setmode(GPIO.BCM)

# Define function to measure charge time
def RCtime (PiPin):
  measurement = 0
  # Discharge capacitor
  GPIO.setup(PiPin, GPIO.OUT)
  GPIO.output(PiPin, GPIO.LOW)
  time.sleep(0.1)

  GPIO.setup(PiPin, GPIO.IN)
  # Count loops until voltage across
  # capacitor reads high on GPIO
  while (GPIO.input(PiPin) == GPIO.LOW):
    measurement += 1

  return measurement

# Main program loop
while True:
  print RCtime(4) # Measure timing using GPIO4
