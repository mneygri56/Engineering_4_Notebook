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
