from picamera import PiCamera
from  time import sleep

myCamera = PiCamera()
myCamera.start_preview(alpha = 200)
myCamera.image_effect = 'cartoon'
myCamera.start_recording('myVid.h264')
sleep(10)
myCamera.stop_recording()
myCamera.stop_preview()
