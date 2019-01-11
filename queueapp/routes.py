from flask import render_template
from queueapp import app

@app.route("/", methods = ['GET', 'POST'])
def index():
	return "Hello World"

