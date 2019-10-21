#Stop Motion Code
#Written by David and Miles

from picamera import PiCamera
from gpiozero import Button

camera = PiCamera()
button = Button(17)
#set the camera rotation to 0
camera.rotation = 0
#start the camera preview with an opacity of 200/255
camera.start_preview(alpha = 200)
#loop control variable
frame = 1
while True:
    try:
    	#wait for a button press and then take a pictue
        button.wait_for_press()
        camera.capture('/home/pi/Documents/Engineering_4_Notebook/Animation/frame%03d.jpg' % frame)
        #let the user know a picture has been taken
        print("picture taken")
        #make sure the filename is right
        frame += 1
    except KeyboardInterrupt:
    	#when ^C is pressed, end the preview and program
        camera.stop_preview()
        break

