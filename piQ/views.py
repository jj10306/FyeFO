from flask import render_template, request, jsonify, url_for
from piQ import app
from piQ.models import Queue
from piQ.forms import Form
from piQ.table import UserTable
from piQ.logic import get_user_info

source = Queue()
tas = list()
active_ta = ""

@app.route("/", methods = ["GET", "POST"])
def index():
    return process_request(request)

    #always display table, regardlesss of if change was made or not
    # table=UserTable(source.__repr__())

#serves the current queue and ta list to the front-end for manipulation/display
@app.route("/queue")
def serve():
    return jsonify({"queue": source.__repr__(), "tas": tas})

#takes in a request and does the required logic
def process_request(request):
    global source
    global name

    if request.method == "POST":
        #different possible TA button presses
        if request.form.get("remove"):
            source.dequeue()
            return render_template("ta.html", name=name)
        elif request.form.get("clear"):
            source = Queue()
            return render_template("index.html")
        elif request.form.get("exit"):
            return render_template("index.html")

        else:
            gtid = request.form["gtid"]
            user_data = get_user_info(gtid)
            name = user_data["name"]

            if user_data["role"] == "Ta":
                if name not in tas:
                    tas.append(name)
                return render_template("ta.html", name=name)
            else:
                if not source.isElement(name):
                    source.enqueue(name)
    return render_template("index.html")
