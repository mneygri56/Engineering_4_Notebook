import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageOps
# Import the LSM303 module.
import Adafruit_LSM303
import math


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
leftText = Image.new('1', (height, width))
drawLeft = ImageDraw.Draw(leftText)
pi = 3.14159265358979323846264338327950
yPos = 48
currX = 1
values = [48]
startX = 0
#start of real code
def realMap(number, lowFirst, highFirst,lowSecond, highSecond):
    newNumber =(number-lowFirst)/(highFirst-lowFirst)*(highSecond-lowSecond)+lowSecond
    return newNumber

while True:
    
    accel, mag = lsm303.read()
    accel_x, accel_y, accel_z = accel
    draw.rectangle((0,0,width,height),0,0)
    drawLeft.text((17,5), "a(m/s^2)", fill = 125)
    w = leftText.rotate(90, expand=1)
    image.paste(w)
    draw.line((16,0,16,48), fill = 255)
    draw.line((16,48,128,48), 255)
    draw.text((32,50), "Time (seconds)", font=font,fill=125)
        
    
    #map the acceleration to a better outline
    #x = realMap(accel_x, -1000, 1000, 0, 100)
    y = realMap(accel_y, -1000, 1000, 0, 32)
    #z = realMap(accel_z, -1000, 1000, 0, 100)
    yPos = 48-y
    values.append(yPos)
    currX+=1
    startX = currX-112
    if startX<0:
        startX = 0
    for xPos in range(112):
        if(xPos>currX-1):
            break
        draw.line((16+xPos, values[startX+xPos-1], xPos+17, values[startX+xPos]), fill = 255)
    #screenText = "X:"+str(round(x,2))+"\nY:"+str(round(y, 2))+"\nZ:"+str(round(z, 2))
    #draw.text((10,10),  "Accel Data:\n"+screenText, font=font, fill=125)
    disp.image(image)
    disp.display()
    
