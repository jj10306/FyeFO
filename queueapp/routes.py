from flask import render_template, request, flash
from queueapp import app
from queueapp.forms import Form
from queueapp.Queue import Queue
from queueapp.table import StudentTable
from queueapp.Student import Student

daQueue = Queue() #this is the queue whose contents are being displayed

@app.route("/", methods = ['GET', 'POST'])
def index():
    form = Form()

    if request.method == "POST":
        if request.form["button"] == "Submit":
            name = request.form["student_name"]
            choice = request.form["reason"]
            if name != "" and choice != "Select":
                daQueue.enqueue(Student(name,choice))
    table = StudentTable(daQueue.__repr__())

    return render_template('index.html', form=form, table=table)


@app.route("/ta", methods = ['GET', 'POST'])
def taIndex():
    form = Form()
    if request.method == "POST":
        if request.form["removeButton"] == "Remove":
            daQueue.dequeue()
    table = StudentTable(daQueue.__repr__())
    return render_template('taIndex.html', form=form, table=table)
