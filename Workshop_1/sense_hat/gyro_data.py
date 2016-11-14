# Language: Python
# File name: gyro_data.py
# Description: This will print the gyroscope data for x, y, and z

# Import the libraries needed
from sense_hat import SenseHat
import os


# Initialize the SenseHat
sense = SenseHat()


# Body of the code
while True:
    acceleration = sense.get_accelerometer_raw()

    # Pitch
    x = acceleration['x']
    # Roll
    y = acceleration['y']
    # Yaw
    z = acceleration['z']

    # This rounds the values to the first decimal point
    x=round(x, 1)
    y=round(y, 1)
    z=round(z, 1)


    # This prints each position value
    print("x={0}, y={1}, z={2}".format(x, y, z))
