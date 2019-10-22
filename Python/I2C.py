#Accelerometer numerical out
#Written by David and Miles

import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
#libraries
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
# Import the LSM303 module.
import Adafruit_LSM303


# Create a LSM303 instance.
lsm303 = Adafruit_LSM303.LSM303()
# Raspberry Pi pin configuration:
RST = 24
# Note the following are only used with SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

# Note you can change the I2C address by passing an i2c_address parameter like:
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3D)

# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))
font = ImageFont.load_default()
# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

#start of real code
#map number to bounds
def realMap(number, lowFirst, highFirst,lowSecond, highSecond):
    newNumber =(number-lowFirst)/(highFirst-lowFirst)*(highSecond-lowSecond)+lowSecond
    return newNumber

while True: #gets the accelerometer data, outputs it to the OLED in text form
	#reset the screen by drawing a rectangle
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    accel, mag = lsm303.read()
    #get the accelerations and map them to the gravity thing
    accel_x, accel_y, accel_z = accel
    x = realMap(accel_x, -1000, 1000, -9.81, 9.81)
    y = realMap(accel_y, -1000, 1000, -9.81, 9.81)
    z = realMap(accel_z, -1000, 1000, -9.81, 9.81)
    #print out the values to the screen
    screenText = "X:"+str(round(x,2))+"\nY:"+str(round(y, 2))+"\nZ:"+str(round(z, 2))
    draw.text((10,10),  "Accel Data:\n"+screenText, font=font, fill=125)
    disp.image(image)
    disp.display()
    
