#Activate LEDs via GPIO
#Written by David and Miles

import RPi.GPIO as GPIO
from time import sleep
#libraries
GPIO.setmode(GPIO.BOARD) #sets up pins
GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)

for i in range(0,10): #runs loop 10 times
    GPIO.output(12,1) #turns leds on
    GPIO.output(11,1)
    sleep(0.5) #half second wait
    GPIO.output(11,0) #turns leds off
    GPIO.output(12,0)
    sleep(0.5) #half second wait
GPIO.cleanup() #resets gpio
