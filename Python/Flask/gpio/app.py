from flask import Flask, render_template, request
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)

blueState = False
redState = False

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
	global blueState
	global redState
	global blueMsg
	global redMsg
	global msg
	if request.method == "POST":
		if 'blue' in request.form:
			if blueState == False:
				blueState = True
				GPIO.output(17, GPIO.HIGH)
				blueMsg = "Blue is On"
			else:
				blueState = False
				GPIO.output(17, GPIO.LOW)
				blueMsg = "Blue is Off"
		elif 'red' in request.form:
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
		GPIO.output(18,GPIO.LOW)
	return render_template("index.html", msg=blueMsg + "and" + redMsg, blueLed=blueState, redLed=redState)
if __name__ == "__main__":
	app.run(host="0.0.0.0", port=80)

GPIO.cleanup()
