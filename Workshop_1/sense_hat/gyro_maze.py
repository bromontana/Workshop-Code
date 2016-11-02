# Language: Python
# File name: gyro_maze.py
# Description: This will build the maze and allow users to play
#              the maze game on the senseHAT

# Import the libraries needed
from sense_hat import SenseHat
import os
from time import sleep


# Initialize the SenseHat
sense = SenseHat()
# Ihis clears the LED matrix
sense.clear()



# Win condition
game_over = False


# Define some variables to represent colors
# red is the wall
r = (255,0,0)
# b is blank
b = (0,0,0)
# w is the pointer
w = (255,255,255)
# g is the goal
g = (0,255,0)


# This is the starting position of the point on the LED matrix
x = 1
y = 1



# Matrix for the maze
# This is a list of lists
# Each item in the list is a row
maze = [[r,r,r,r,r,r,r,r],
        [r,b,b,b,b,b,b,r],
        [r,b,b,b,b,b,b,r],
        [r,b,b,b,b,b,b,r],
        [r,b,b,b,b,b,b,r],
        [r,b,b,b,b,b,b,r],
        [r,b,b,b,b,b,b,r],
        [r,r,r,r,r,r,r,r]]





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
    x,y = check_wall(x, y, new_x, new_y)

    # This returns the new position
    return x,y


# This will check the placement for a new ball and look for collisions
def check_wall(x,y,new_x,new_y):

    if maze[new_y][new_x] != r:
        # This code will not allow the pointer to go through corners
        #if maze[new_y][x] and maze[y][new_x] == r:
        #    return x,y
        return new_x, new_y
    elif maze[new_y][x] != r:
        return x, new_y
    elif maze[y][new_x] != r:
        return new_x, y
    return x,y


# This checks the win condition, if the position of the ball is on the green
# Spot then the game is over
def check_win(x,y):
    global game_over
    if maze[y][x] == g:
        game_over = True
        sense.show_message('You Win')

# Body of the code, contition is that the game is not over
while not game_over:
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

    # This will set the new x,y values based on the gyroscope data
    x,y = move_pointer(pitch, roll, x, y)

    # This checks the win condition
    check_win(x,y)



    # This will place the pointer in the next position
    maze[y][x] = w


    # Builds the maze
    sense.set_pixels(sum(maze,[]))


    # This will make the function wait a short amount of time before going
    # to make sure it doesnt consume too much CPU power
    sleep(0.05)

    # This will take the last x,y point and make it white
    maze[y][x] = b





    # This will print the pitch and roll values
    print("pitch = {}, roll = {}".format(pitch, roll))
    # This will print the x and y position
    print("x = {}, y = {}".format(x,y))


