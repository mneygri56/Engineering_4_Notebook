#Second Camera Program
#Written by David and Miles

from picamera import PiCamera
from  time import sleep
#import functions
effects = ['none', 'negative', 'solarize', 'sketch', 'denoise', 'emboss', 'oilpaint',
           'hatch', 'gpen', 'pastel', 'watercolor', 'film', 'blur', 'saturation',
           'colorswap', 'washedout', 'posterise', 'colorpoint', 'colorbalance', 'cartoon', 'deinterlace1', 'deinterlace2'] #array of all effects
myCamera = PiCamera() #declares camera
myCamera.start_preview() #broadcasts camera view to screen
for effect in effects: #for-each loop, shows each effect for 3 seconds, then goes to next one
    myCamera.image_effect = effect
    myCamera.annotate_text = "This effect is: "+effect
    sleep(3)
    if effect == 'gpen' or effect == 'solarize' or effect == 'negative' or effect == 'posterise' or effect == 'emboss' or effect == 'cartoon': #takes pictures when a specific effect is active
        myCamera.annotate_text = "Taking picture with: "+effect
        sleep(3)
        myCamera.annotate_text = "3"
        sleep(1)
        myCamera.annotate_text = "2"
        sleep(1)
        myCamera.annotate_text = "1"
        sleep(1)
        myCamera.annotate_text = "This effect is: "+effect
        myCamera.capture(effect+'.jpg')

myCamera.stop_preview()

