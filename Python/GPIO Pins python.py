import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)

for i in range(1,10):
    GPIO.output(12,1)
    GPIO.output(11,1)
    sleep(0.5)
    GPIO.output(11,0)
    GPIO.output(12,0)
    sleep(0.5)
GPIO.cleanup()
