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
