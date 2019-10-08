from picamera import PiCamera
from  time import sleep



myCamera = PiCamera()
#SPOOKTOBER
myCamera.start_preview(alpha = 245, PiCamera.IMAGE_EFFECTS(1))
sleep(5)

myCamera.stop_preview()

