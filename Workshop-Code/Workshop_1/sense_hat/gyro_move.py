# Language: Python
# File name: gyro_move.py
# Description: This will output the position of the pointer on the maze

#Import the libraries needed
from sense_hat import SenseHat
import os
from time import sleep


# Initialize the SenseHat
sense = SenseHat()
# This clears the LED matrix
sense.clear()


# This is the starting position of the point on the LED matrix
x = 1
y = 1


# This function will move the ball, it takes in the pitch and roll,
# as well as the point position
def move_pointer(pitch, roll, x, y):
    # new_x, new_y are local variables
    new_x = x
    new_y = y

    # This changes the ball's x value
    if -1 < pitch < -.2 and x != 0:
        new_x -= 1
    elif 1 > pitch > .2 and x != 7:
        new_x += 1

    # This changes the ball's y value
    if -1 < roll < -.2 and y != 0:
        new_y -= 1
    elif 1 > roll > .2 and y != 7:
        new_y += 1

    # This sets the x and y values to be equal to the local variables
    x,y = new_x, new_y

    # This returns the new position
    return x,y



# Main program loop
while True:
    # This imports the gyroscope values in a list acceleration[]
    acceleration = sense.get_accelerometer_raw()

    # X direction
    pitch = acceleration['x']
    # Y direction
    roll = acceleration['y']
    # Z direction
    yaw = acceleration['z']


    # This rounds the variables to the first decimal point place
    pitch = round(pitch, 1)
    roll = round(roll, 1)
    yaw = round(yaw, 1)

    # This will make the function wait a short amount of time before going
    # to make sure it doesnt consume too much CPU power
    sleep(0.05)

    # This will take the last x,y point and make it white
    sense.set_pixel(x , y , 0 , 0 , 0)
    # This will set the new x,y values based on the gyroscope data
    x,y = move_pointer(pitch, roll, x, y)
    # This will place the pointer in the next position
    sense.set_pixel(x , y , 255 , 0 , 0)


    # This will print the pitch and roll values
    print("pitch = {}, roll = {}".format(pitch, roll))
    # This will print the x and y position
    print("x = {}, y = {}".format(x,y))
