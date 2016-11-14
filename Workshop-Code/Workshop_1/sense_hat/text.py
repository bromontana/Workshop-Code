# Language: Python
# File name: text.py
# Description: This will display text on the LED matrix with the given conditions

from sense_hat import SenseHat

# SenseHAT initialization
sense = SenseHat()

# Main program loop
while True:
  #                  display text   scroll speed       color       RGB code     background  RGB code
  sense.show_message("Hello World", scroll_speed=0.05, text_colour=[255,255,0], back_colour=[0,0,255])

