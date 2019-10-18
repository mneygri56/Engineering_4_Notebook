from picamera import PiCamera
from gpiozero import Button

camera = PiCamera()
button = Button(17)
camera.rotation = 0
camera.start_preview(alpha = 200)
frame = 1
while True:
    try:
        button.wait_for_press()
        camera.capture('/home/pi/Documents/Engineering_4_Notebook/Animation/frame%03d.jpg' % frame)
        print("picture taken")
        frame += 1
    except KeyboardInterrupt:
        camera.stop_preview()
        break

