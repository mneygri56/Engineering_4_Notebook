#First Camera program
#Written by David and Miles

from picamera import PiCamera #importing libraries and functions
from  time import sleep



myCamera = PiCamera() #declares camera
#SPOOKTOBER (transparency joke)
myCamera.start_preview(alpha = 245) #broadcasts the camera's output to screen, slightly transparent
sleep(5) #pause for 5 seconds

myCamera.stop_preview() #stop broadcasting camera output

