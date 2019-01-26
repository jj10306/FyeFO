from flask import render_template, redirect, url_for, request, flash
from queueapp import app
from queueapp.forms import Form
from queueapp.Queue import Queue
from queueapp.table import StudentTable
from queueapp.Student import Student

daQueue = Queue() #this is the queue whose contents are being displayed

@app.route("/", methods = ['GET', 'POST'])
def index():
    form = Form()
    table = StudentTable(daQueue.__repr__())
    if request.method == "GET":
        return render_template('index.html', form=form, table=table)

    if request.method == "POST":
        if request.form["button"] == "Submit":
            name = request.form["student_name"]
            choice = request.form["reason"]
            if name != "" and choice != "Select":
                daQueue.enqueue(Student(name,choice))
        return redirect(url_for("queueIndex"))

@app.route("/ta", methods = ['GET', 'POST'])
def taIndex():
    form = Form()
    table = StudentTable(daQueue.__repr__())
    if request.method == "GET":
        return render_template('taIndex.html', form=form, table=table)
    if request.method == "POST":
        if request.form["removeButton"] == "Remove":
            daQueue.dequeue()
        return redirect(url_for("queueIndex"))

@app.route("/queue", methods = ['GET'])
def queueIndex():
    form = Form()
    if request.method == "GET":
        table = StudentTable(daQueue.__repr__())
        return render_template('queue.html', form=form, table=table)
