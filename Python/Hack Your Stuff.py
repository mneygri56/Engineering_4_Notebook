#Switch-activated alarm
#Written by David and Miles

import RPi.GPIO as G
import time
from gpiozero import MotionSensor
#libraries
switchIn = True
G.setwarnings(False) #gpio setup
G.setmode(G.BCM)
G.setup(18, G.OUT)
G.setup(17,G.IN)
while True: #infinite loop, when the switch is thrown, give the alarm power
    switchIn = G.input(17)
    
    if(not switchIn):
        G.output(18, G.LOW)
        print("Low")
    else:
        G.output(18, G.HIGH)
        print("High")
