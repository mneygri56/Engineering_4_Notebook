from gpiozero import MotionSensor
from picamera import PiCamera
from time import sleep
from datetime import datetime
camera = PiCamera()
pir = MotionSensor(17)


while True:
    filename = "intruder {0:%Y}-{0:%m}-{0:%d} {0:%H}-{0:%M}-{0:%S}.h264".format(datetime.now())
    pir.wait_for_motion()
    camera.start_recording(filename)
    print("started video")
    pir.wait_for_no_motion()
    camera.stop_recording()
    print("video traken")

