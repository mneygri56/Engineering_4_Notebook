#Third Camera Program
#Written by David and Miles

from picamera import PiCamera
from  time import sleep
#libraries

myCamera = PiCamera()
myCamera.start_preview(alpha = 200) #starts a preview with transparency
myCamera.image_effect = 'cartoon' #applies effect to camera
myCamera.start_recording('myVid.h264') #starts to record video
sleep(10) #wait 10 seconds
myCamera.stop_recording() #stop recording video
myCamera.stop_preview() #stop broadcasting to screen
