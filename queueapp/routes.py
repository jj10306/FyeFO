from flask import render_template, request
from queueapp import app
from queueapp.forms import Form

@app.route("/", methods = ['GET', 'POST'])
def index():
    form = Form()

    if request.method == 'POST':
        name = request.form["student_name"]
        choice = request.form["choice"]
        print(name)

    return render_template('index.html', form=form)


