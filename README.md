#README for Workshop 1 


##Directories

__LED__ and __sense_hat__ represent the different "halfs" of the workshop. 

__LED__ is the first half that has to do with building a circuit and
how the Raspberry Pi can be used as a platform for building 
circuits and making them do something. 

__sense_hat__ is the second half, where students learn how to use sensors to
create functional programs. 


###LED

Here is what each file does 
+ LED.py
  + This will turn the LED on and off with time input and voltage output
+ Photoresistor.py
  + This will print the amount of time it takes for a capacitor to charge.
   The capacitor is in series with the capacitor, so it will take a different
   amount of time to charge according to the resistance of the photoresistor. 
+ LED_Photoresistor.py
  + This will turn the LED on and off using the Photoresistor 


###sense_hat

Here is what each file does:
+ gyro_data.py
  + This will print out the gyroscopic raw data (voltage between -1,1) and print 
   it in X,Y,Z components. 
+ gyro_move.py
  + This will make a "point" or "cursor" on the LED matrix which will have motion 
   logic that uses the gyro_data function to operate. 
+ gyro_maze.py
  + This will combine the last two and make a maze game. 
  + Students can change the LED matrix in the code to design their own maze layout.
  + There is also a bug where if there are two walls that look like this:
   
             ***
             ***
                ***
                ***
   Where each group stars are a wall; pointers can slip between them. The solution 
   to the bug it commented out. It is to the disgression of the instructor to 
   use that bug as they wish. 
+ temp.py
  + This will print the temperature in the room (in Celcius) as well as move a 
   "bar" that will show up on the LED matrix. 
  + The program takes the initial temperature and uses it to initialize the "bar" 
   on the LED matrx, so that it starts at 3 bars and can always be able to move
   up or down, depending on the relative temperature (relative to the initial
   temperature). 
+ text.py
  + This one is the simplist. 
  + This is one line that has a function that writes a message onto the screen 
   by scrolling it from left to right. There are several values students can 
   change. 
