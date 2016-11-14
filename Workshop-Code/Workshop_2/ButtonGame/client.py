# Language: Python
# File name: client.py
# Description: use this to join the web client
import RPi.GPIO as GPIO
import time
import datetime
from socketIO_client import SocketIO, LoggingNamespace
from uuid import getnode as get_mac
mac = get_mac()
print("Your mac address is "+str(mac))
IP = raw_input('Enter game server IP: ')
print("Connecting to "+IP+"...")
socketIO = SocketIO(IP, 3000, LoggingNamespace)
print("Connected!")
GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(17,GPIO.OUT)
state = False

socketIO.emit("join", str(mac))

while True:
    input_state = GPIO.input(4)
    if (input_state != state)and(input_state==True):
        print('Button Pressed')
        GPIO.output(17, GPIO.HIGH)
        state = input_state
        date = (time.time())
        socketIO.emit('push', date)
    elif(input_state!=state)and(input_state==False):
        GPIO.output(17, GPIO.LOW)
        state = input_state
    time.sleep(0.2)
