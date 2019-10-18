import RPi.GPIO as G
import time
from gpiozero import MotionSensor

switchIn = True
G.setwarnings(False)
G.setmode(G.BCM)
G.setup(18, G.OUT)
G.setup(17,G.IN)
while True:
    switchIn = G.input(17)
    
    if(not switchIn):
        G.output(18, G.LOW)
        print("Low")
    else:
        G.output(18, G.HIGH)
        print("High")
