# This is our Engineering 4 Notebook
Table of Contents:
 - [Introduction Assignments](#Introduction%20assignments)
 - [Python Stuff](#awesome%20python%20code%20part%20thats%20really%20fun%20stuff)
 - [GPIO Assignments](#gpio%20stuff!!)
 - [Hard Flask Stuff Angry Face](#start%20of%20flask%20stuff)
 - [Big Hard Assignments That take a While](#putting%20it%20all%20together)
## Introduction Assignments
<!-- toc -->
### Hello Raspberry Pi Zero
This assigment was an introduction to bash scripts and pi stuff in general
#### Code
Our code here wasn't too complicated, so we spiced it up a bit, see for yourself;
<details>
  <summary>Code</summary>
	
```
#!/bin/bash
str="Hello World!" #declares the string
for i in {1..10} #run the loop 10 times
do
str="$str $str" #concatenates the string with itself, doubles length
echo $str #prints the final (massive) string to the terminal
done

```

</details>

### Hello Mathematica
Here we had to figure out how to write a line of Mathematica to make a plot with sliders

We couldn't retrieve the actual line of code that we used, but we had to use the Manipulate() function with the graph that we wanted to create two sliders that controlled constants in the equation

### Hello Python
This boi is a die roller written in Python, we wrote a program to roll a die and print out a random number between 1 and 6

#### Code

<details>
  <summary>How to Roll a Die in Python (Ten Steps) (With Pictures!)</summary>
  
```python
  
#Automatic Dice Roller
#Written by David and Miles

import random

print("Automatic Dice Roller")
print("Enter to Roll, x to exit")
while(True): #loop that runs forever
    x = input("Roll the Dice")
    if(x == ""):
        print(random.randint(1,6)) #generates random int 1-6
    elif(x == "x"): #conditional to kill program
        print("Done already?")
        raise SystemExit
```

</details>

### Calculator
The goal of this assignment was to create a program with a function that could calculate the sum, difference, quotient, and product of two inputs

#### Code

<details>
  <summary> This man can calculate large sums in his head, #3 will suprise you (Not Clickbait)</summary>
  
```python
#Calculator
#Written By David and Miles

print("x to exit")

def doMath(first, second, operation): #function to do math
    num = 0 #variable to be output
    if(operation == 1): #addition
        num = first+second 
    if(operation == 2): #subtraction
        num = first-second
    if(operation == 3): #multiplication
        num = first*second
    if(operation == 4): #division, rounded to two decimals
        num = round(first/second, 2)
    if(operation == 5): #modulus
        num = int(first)%int(second)
    return num
while(True):
    numOne = input("First Number") 
    numTwo = input("Second Number")
    if(numOne == 'x' or numTwo == 'x'):#exit condition
        raise SystemExit
    #calls to doMath to get outputs
    print("Sum:\t\t" + str(doMath(float(numOne), float(numTwo), 1)))
    print("Difference:\t" + str(doMath(float(numOne), float(numTwo), 2)))
    print("Product:\t" + str(doMath(float(numOne), float(numTwo), 3))) 
    print("Quotient:\t" + str(doMath(float(numOne), float(numTwo), 4)))
    print("Modulo:\t\t" + str(doMath(float(numOne), float(numTwo), 5)))
    
```
  
</details>

### Quadratic Solver

Ever been in math class and wanted an easy way to calculate those weird quadratics, well you've got it.

#### Code
This program prints out the roots of a quadratic given the coefficients, call now and we'll double your order, just call 1-800-not-scam

<details>
  <summary>Act fast, our first 30 customers get a free code with their order</summary>
  
```python
#Quadratic Solver
#Written by David and Miles
import math
print("x to exit")
print("Quadratic Solver,  \nEnter coefficients for ax^2 + bx + c = 0")

#Calculate the roots of the function given coefficients

def rootCalc(fna, fnb, fnc):
    #Calculate the Discriminant
    fnD = fnb**2 - 4*fna*fnc
    #if its more than 0, calculate two roots
    if(fnD>0):
        fnD = math.sqrt(fnD)
        roots = [round(-(b+fnD)/(2*a), 3), round((-b+fnD)/(2*a), 3)]
    #if the Discriminant is zero, calculate one root
    elif(fnD == 0):
        fnD = math.sqrt(fnD)
        roots = [round(-b/(2*a), 3)]
    #otherwise, it has no real roots
    else:
        roots = ["No Real Roots"]
    return roots
while(True):
    #ask for a, b, and c inputs
    a = input("Input a for ax^2 ")
    b = input("Input b for bx ")
    c = input("Input c for c ")
    #if a coefficient is entered as x,
    #end the program, otherwise calculate the roots
    if(a!="x" and b!="x" and c!="x"):
        a = float(a)
        b = float(b)
        c = float(c)
        newRoots = rootCalc(float(a), float(b), float(c))
        #print out all elements in the newRoots array
        print("Roots: "+str(newRoots[0:]))
    else:
        raise SystemExit
        
```
 
 </details>
 
 ### Hello Git
This project was setting up github on the pi. Github has sinced ceased to function for no reason, so we decided to make our own github:

1st, put the changed files onto a flash drive (The "hub")

2nd, download them onto another computer (The "Git")

3rd, Commit and Push

Yay hubGit™!!!

### Git Forks and Clones
We forked a repository called class accounts, and cloned it to the pi, added our names to it, then committed it.

We want to make sure we pull recent changes from github before pushing

## Awesome Python Code Part thats really fun stuff

### Strings and Loops
This program was a little tricky, we had to learn how to split strings, so that's my lessons learned, the split() function is really useful.

<details>
  <summary>Code</summary>
	
```python   
#Strings and Loops
#Written By David and Miles
while(True):
	#Get a User Input
    sentence = input("Enter a Sentence: ")
    #Split the Input by Spaces
    splitsentence = sentence.split()

    for n in range(len(splitsentence)):
	#if the sentence is over, end the system
	if (splitsentence[n] == "-1"):
		raise SystemExit
	#Otherwise, print out each character in the string
	for x in range(len(splitsentence[n])):
	    print(splitsentence[n][x])
	#print a - between words
	print("-")
 ```
  
</details>
  
### Man Shaped Pinata (Pronounced Pin-ate-ae, no accent whatsoever)
This program was to make a "Man Shaped Pinata" game, which is basically (whispers) Hangman (/whispers) This was a bit frustrating, the first program with a "Problems" Section!

#### Code
<details>
  <summary>Code</summary>
	
```python
#Man Shaped Pinata word guessing game
#Written by David and Miles
import getpass
#Define how one makes the man shaped pinata
MSP = "---" + u'\u2510' + "\n   O\n   |\n  /|\\\n   |\n  / \\"
def main():
    #x is the number of characters in the man shaped pinata to print
    x = 4

    #get the word
    word = getpass.getpass("Player 1, what is the word? ")
    wordArr = word.split()
    guessList = []
    #Clear the terminal
    print("\n"*50)
    guessNum = 0
    workingWord = ""
    spacesAfter = 0
    #get the "working word" which is how much player two has guessed
    for n in wordArr:
	workingWord += "-"*len(n)+" "
    #put the word into lowercase
    word = word.lower()
    #while guesses is less than 8 and the words havent been guessed
    while (workingWord.split() != word.split() and guessNum < 8):
	#clear screen, print out the Man shaped pinata, print the amount that
	#has been guessed followed by the letters that have been guessed
	print("\n"*50)
	print(MSP[:x]+"\n"*(5-spacesAfter))
	guessCorrect = False
	print((workingWord))
	print("Previously guessed: " + ", ".join(guessList))
	guess = raw_input("Player 2, guess a letter ").lower()
	isUsed = True
	while(isUsed):
	    isUsed = False
	    #if n has already been guessed, give them another shot
	    for n in guessList:
		if(n == guess):
		    isUsed = True
	    if(not isUsed):
		guessList.append(guess)
	    else:
		print("Already Guessed FOOL")
		guess = raw_input("Player 2, guess a letter AGAIN ").lower()
	#if the letter is in the word, change working word to have that letter
	#in the right place, otherwise ...
	for n in range(len(workingWord)-1):
	    if (guess == word[n]):
		workingList = list(workingWord)
		workingList[n] = guess
		workingWord = "".join(workingList)
		guessCorrect = True
	if(guess.split() == word.split()):
	    workingWord = word
	    guessCorrect = True
	#... Otherwise add to x so that the next piece is revealed
	if (guessCorrect == False):
	    guessNum+=1
	    if(guessNum == 7 or guessNum == 3):
		x+=4
		spacesAfter +=1
	    elif(guessNum == 4 or guessNum == 5):
		x+=1
	    elif(guessNum == 8):
		x+=2
	    else:
		spacesAfter +=1
		x += 5
    #Win conditions, the word has been guessed, player two wins
    #too many guesses, player one wins
    if(workingWord.split() == word.split()):
	print("Player Two wins, the word was: "+word)
    else:
	print(MSP)
	print("Player One wins, the word was: "+word)
    #see if they want to play again
    playAgain = raw_input("Play Again y/n ")
    if(playAgain == "y"):
	main()
    else:
	raise SystemExit
main()
```
  
</details>

#### Problems
We took a bit of time on figuring out how to clear the terminal. We eventually decided on printing 50 new lines, but then we saw that it was collapsing the 50 into one, so we had to go into settings and make it not collapse it into the one line. Also we wanted to spice our program up a bit and made the user input private, but that line didn't work in shell, so we had to run it in terminal. That was a weird error, but we got it cleared up by using it in terminal.

## GPIO stuff!!
This is the start of gpio funTimes.
### GPIO Pins - Bash

This was an introduction to GPIO using a bash script to blink an LED, it wasn't too hard and it is useful for learning how to use the pins. 

#### Code
<details>
	<summary> Code to Blinkenlichten </summary>

```python

#!bin/bash

# this script makes 2 leds blink 10 times each

gpio mode 0 out #sets up gpio pin
gpio mode 1 out #sets up gpio pin


for i in {1..10} #runs the loop 10 times
do
gpio write 0 1 #turns led on
gpio write 1 1 #turns other led on
sleep 0.5 #wait for half a second
gpio write 0 0 #turns led off
gpio write 1 0 #turns other led off
sleep 0.5 #wait for half a second
done

```
	
</details>

### GPIO pins - Python

This assignment taught us how to use python with GPIO, we want to remember how to use the GPIO libraries because that is something that is probably going to be a big thing in the future

#### Code
<details>
	<summary> Blinkenlichten but python this time </summary>

```python

#Activate LEDs via GPIO
#Written by David and Miles

import RPi.GPIO as GPIO
from time import sleep
#libraries
GPIO.setmode(GPIO.BOARD) #sets up pins
GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)

for i in range(0,10): #runs loop 10 times
    GPIO.output(12,1) #turns leds on
    GPIO.output(11,1)
    sleep(0.5) #half second wait
    GPIO.output(11,0) #turns leds off
    GPIO.output(12,0)
    sleep(0.5) #half second wait
GPIO.cleanup() #resets gpio

```

</details>

### GPIO pins - SSH
This assignment was pretty cool, we used our phone to make an LED turn on and off, it was pretty cool to be able to control the pi without actually touching it.

We used an app on our phone to communicate with the pi, there wasn't a code file, it was just turning the leds on and off in the console.

## Start of Flask Stuff

### Hello Flask
This assignment was to create a website that showed "hello world" when you connected to it.

#### Code
<details>
	<summary>Code</summary>
	
```python
	  
#Hello world via Flask
#Written by David and Miles

from flask import Flask
#import the flask library
app = Flask(__name__)
#turns on flask
@app.route("/")
def hello_world(): #creates function to return hello world
	return "hello world!"

if __name__ == "__main__": #ports
	app.run(host="0.0.0.0", port=80)
```
</details>

### GPIO pins - Flask

This Was Hard. We would have had less trouble if we had realized that we could make global variables, but we didn't, it took us like a week to figure out the global variables thing, but the rest was pretty easy. We got to make it look good and function with CSS tags.

#### Code

There are two parts to this code, html and Flask

<details>
	<summary> html stuff code bois </summary>

```xml

<!doctype html>
<html>
<head>
	<style> <!-- designs the buttons and sets up location stuff for them -->
		.redButton{
		background-color: #808080;
		color: #F00;
		font-size: 40px;
		padding: 200px 300px;
		border-radius: 10px;
		border: none;
		float: right;
		}
		.blueButton{
		background-color: #808080;
		color: #00F;
		font-size: 40px;
		padding: 200px 300px;
		border-radius: 10px;
		border: none;
		float: left;
		}
		div{
		margin-left: 100px;
		margin-right: 100px;
		}
	</style>
	<title>GPIO with Flask!</title> <!-- what shows up on the tab of the browser -->
</head>
	<body> <!-- creates the buttons and sets up what happens when they are pushed -->
		<div>
		<center><h1>{{msg}}</h1>
		<img src="https://i.redd.it/ku1neu504sh01.jpg" alt="backend-frontend ayy lmao" style="width:322px;height:445px"> <!-- self-roast in the form of an image comparing the front-end(pretty good) and the back-end(this file) -->
		</center>
		<form method="POST">
			<button align="left" type="submit" class="blueButton"  name="blue" value="blueLed">Blue</button>
			<button align="right" type="submit" class="redButton" name="red" value="redLed">Red</button>
		</form>
		</div>
<body>
</html>
		
```
</details>

<details>
	<summary> Python Code bois </summary>
	
```python
#Flask/HTML combo program
#Written by David and Miles

from flask import Flask, render_template, request
import RPi.GPIO as GPIO
#imports libraries
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
#set up gpio
blueState = False
redState = False
blueMsg = "Blue is Off"
redMsg = "Red is Off" #messages displayed on
app = Flask(__name__) #activate flask

@app.route("/", methods=["GET","POST"])
def index(): 
	global blueState
	global redState
	global blueMsg
	global redMsg
	global msg
	if request.method == "POST":
		if 'blue' in request.form: #activates/deactivates blue led and changes message to reflect current state
			if blueState == False:
				blueState = True
				GPIO.output(17, GPIO.HIGH)
				blueMsg = "Blue is On"
			else:
				blueState = False
				GPIO.output(17, GPIO.LOW)
				blueMsg = "Blue is Off"
		elif 'red' in request.form: #activates/deactivates red led and changes message to reflect current state
			if redState == False:
                                redState = True
                                GPIO.output(18, GPIO.HIGH)
				redMsg = "Red is On"
                        else:
                                redState = False
                                GPIO.output(18, GPIO.LOW)
				redMsg = "Red is Off"
	else:
		GPIO.output(17,GPIO.LOW)
		GPIO.output(18,GPIO.LOW) #auto deactivates leds
	return render_template("index.html", msg=blueMsg + " and " + redMsg, blueLed=blueState, redLed=redState) #sends messages to html file for outputting to website
if __name__ == "__main__":
	app.run(host="0.0.0.0", port=80)

GPIO.cleanup()
```

</details>

## Putting it all together

### GPIO Pins - I2C

This one wasn't too hard, we had a bit of trouble importing random files because the internet sucks here, so we had to wait a long time for the files to download.

#### Code
This assignment was to make an OLED screen print out the acceleration of the pi along x, y, and z axies(axisis? axes? axs?)
<details>
	<summary> Control the slaves from a master ... </summary>
	
```python
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
 ```
 
 </details>
 
 ### Headless
Step 1: Get a guillotine

Step 2: use it...

This program was kind of bad, by bad I mean it wasn't fun, not that our program was bad, it was actually quite good thank you very much. We had to make a code that made a line plot that scrolled. We were able to make a line plot pretty easily, but our problem came with scrolling. We had to re draw the luine plot each time with a new start value. Eventually, we figured this out, but not before trying every otehr workaround.

<details> 
	<summary> chop the head off the pi </summary>

```python
#Accelerometer graph
#Written by David and Miles

import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
#libraries
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

while True: #gets the data from the accelerometer, then outputs it to the OLED screen
    
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
    y = realMap(accel_y, -1000, 1000, 0, 32)
    #put the values on the graph
    yPos = 48-y
    values.append(yPos)
    currX+=1
    startX = currX-112
    #draw all the lines to make a line plot
    if startX<0:
        startX = 0
    for xPos in range(112):
        if(xPos>currX-1):
            break
        draw.line((16+xPos, values[startX+xPos-1], xPos+17, values[startX+xPos]), fill = 255)
    disp.image(image)
    disp.display()
    
```

</details>

### Pi Camera
We did three assignments so we could take selfies with the pi... guys, if you want to take a selfie, just use your phone, this is a little too much. Also, we had some cool recursive pics. We learned to make the preview window slightly less opaque so that we could kill the program if it messed up.

#### Code
Three part assignment, not too bad. 

<details>
	<summary> Part One </summary>

```python

#First Camera program
#Written by David and Miles

from picamera import PiCamera #importing libraries and functions
from  time import sleep



myCamera = PiCamera() #declares camera
#SPOOKTOBER (transparency joke)
myCamera.start_preview(alpha = 245) #broadcasts the camera's output to screen, slightly transparent
sleep(5) #pause for 5 seconds

myCamera.stop_preview() #stop broadcasting camera output
```

</details>

<details>
	<summary> Part Two </summary>

```python
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
```

</details>

<details>
	<summary> Part Three </summary>

```python
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
```

</details>

#### Images

![Image of Crazy](/Pictures/cartoon.jpg)

![Trippy](/Pictures/emboss.jpg)

![Recursion](/Pictures/gpen.jpg)

![Posterise](/Pictures/posterise.jpg)

![Negative](/Pictures/negative.jpg)

![Solarize](/Pictures/solarize.jpg)

Cool!
### Hack Your Stuff

We had to connect an alarm to the and a switch to make it go off when the switch is flicked. We had a bit of trouble, and if we were to tell ourselves one thing, it would be that the plate thing is a speaker, not a magnetic sensor or w/e we thought it was.

#### Code:::

<details>
	<summary> Killing everyone's ears one siren at a time</summary>

```python
#Switch-activated alarm
#Written by David and Miles

import RPi.GPIO as G
import time
from gpiozero import MotionSensor
#libraries
switchIn = True
G.setwarnings(False) #gpio setup
G.setmode(G.BCM)
G.setup(18, G.OUT)
G.setup(17,G.IN)
while True: #infinite loop, when the switch is thrown, give the alarm power
    switchIn = G.input(17)
    
    if(not switchIn):
        G.output(18, G.LOW)
        print("Low")
    else:
        G.output(18, G.HIGH)
        print("High")
```

</details>

### Copypasta
Basically, we got a couple of tutorials and followed them, we know how to use google to tell us what to do now.
#### Parent Detector
We used a PIR sensor to control a camera so that we could tell if someone went and messed with the pi
##### Code
<details>
	<summary> Find your parents messing with your stuff</summary>
	
```python
#Detect people in your room
#Written by David and Miles
from gpiozero import MotionSensor
from picamera import PiCamera
from time import sleep
from datetime import datetime

#Define camera and pir sensor
camera = PiCamera()
pir = MotionSensor(17)


while True:
	#Filename is the date and time
    filename = "intruder {0:%Y}-{0:%m}-{0:%d} {0:%H}-{0:%M}-{0:%S}.h264".format(datetime.now())
    #When there is motion, start recording until there is no movement
    pir.wait_for_motion()
    camera.start_recording(filename)
    print("started video")
    pir.wait_for_no_motion()
    camera.stop_recording()
    print("video traken")
```

</details>

#### Stop Motion

The goal of this project was to make a stop motion animation of something creative. Most of the time spent on this project was getting the updates needed for libav. We made "A Flash Drive's Journey"

##### Code

<details>
	<summary> Making Of</summary>
Press Button, Take Picture.
	
```python
  
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
```

</details>

##### Video
[Animation](https://youtu.be/NJuUF_IHOos)
