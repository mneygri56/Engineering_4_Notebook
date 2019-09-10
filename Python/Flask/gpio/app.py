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
	msg = "asfjojsghiojhiodfg"
	if request.method == "POST":
		if 'blue' in request.form:
			GPIO.output(17,GPIO.HIGH)
		elif 'red' in request.form:
			GPIO.output(18,GPIO.HIGH)
	else:
		GPIO.output(17,GPIO.LOW)
		msg = "No click yet."
	return render_template("index.html", msg=msg)

def blueOn():
	GPIO.output(17,GPIO.HIGH)

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=80)

GPIO.cleanup()
