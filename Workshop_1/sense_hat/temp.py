# Language: Python
# File name: temp.py
# Description: This will display the current temperature in celcius and
# make an increasing/decreasing bar on the LED matrix

from sense_hat import SenseHat

# Initialize the senseHAT and clear all data
sense = SenseHat()
sense.clear()

# This calibrates the LED matrix, by making the current temperature 33%
# of the way between the maximum and minimum temperature values
tmax = int(sense.get_temperature()) + 2
tmin = tmax - 3

# Main program loop
while True:
    # Gets current temperature and prints it
    temp = sense.get_temperature()
    print(temp)

    # This will fill the amount of rows according the the temperature
    temp = int(temp) - tmin
    for x in range(0, 8):

	# This part fills the bars under the current temperature all red
        for y in range(0, temp):
            sense.set_pixel(x, y, 255, 0, 0)

	# This part will leave all the bars above the temp full 
        for y in range(temp, 8):
            sense.set_pixel(x, y, 0, 0, 0)
