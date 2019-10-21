#Detect people in your room
#Written by David and Miles
from gpiozero import MotionSensor
from picamera import PiCamera
from time import sleep
from datetime import datetime

#Define camera and pir sensor
camera = PiCamera()
pir = MotionSensor(17)


while True:
	#Filename is the date and time
    filename = "intruder {0:%Y}-{0:%m}-{0:%d} {0:%H}-{0:%M}-{0:%S}.h264".format(datetime.now())
    #When there is motion, start recording until there is no movement
    pir.wait_for_motion()
    camera.start_recording(filename)
    print("started video")
    pir.wait_for_no_motion()
    camera.stop_recording()
    print("video traken")

