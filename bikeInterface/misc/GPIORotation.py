# Monitors a GPIO pin for changes in voltage and increments a counter
# A change in state correspinds to one rotation of the bike wheel

from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

# Declare pin 12 as the input to watch and place a pull up resistor on it
inputPin=12
GPIO.setup(inputPin,GPIO.IN,pull_up_down=GPIO.PUD_UP)

counter = 0

# For each rotation increment the counter
while(1): 
        if  GPIO.input(inputPin)==0:
                sleep(.3)
                counter+=1
                print(counter) 
