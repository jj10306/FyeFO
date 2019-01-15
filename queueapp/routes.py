from flask import render_template, request
from queueapp import app
from queueapp.forms import Form
from queapp.Queue import Queue
from queueapp.table import StudentTable
from queueapp.Student import Student

daQueue = Queue() #this is the queue whose contents are being displayed

@app.route("/", methods = ['GET', 'POST'])
def index():
    form = Form()


    if request.method == 'POST':
        name = request.form["student_name"]
        choice = request.form["reason"]


    return render_template('index.html', form=form)


