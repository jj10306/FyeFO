from flask import render_template, request, jsonify, url_for, flash
from piQ import app
from piQ.models import Queue
from piQ.forms import Form
from piQ.table import UserTable
from piQ.logic import get_user_info
from datetime import datetime

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
    return jsonify({"queue": source.__repr__(), "tas": source.tas})

#takes in a request and does the required logic
def process_request(request):

    global source
    global name
    global active_ta
    print("ACTIVE TA IS",active_ta)
    avg_wait=0
    try:
        avg_wait = round(source.totalWait/source.totalHelped,2)
    except:
        avg_wait = 0

    if request.method == "POST":
        #different possible TA button presses
        if request.form.get("remove"):
            source.dequeue()
            return render_template("ta.html", name=name)
        elif request.form.get("clear"):
            temptas = source.tas
            source = Queue()
            source.tas = temptas
            return render_template("index.html",wait=avg_wait)
        elif request.form.get("exit"):
            return render_template("index.html",wait=avg_wait)
        elif request.form.get("signout"):
            source.removeTa(active_ta)
            return render_template("index.html",wait=avg_wait)

        else:
            gtid = request.form["gtid"]
            user_data = get_user_info(gtid)
            if user_data != None:
                name = user_data["name"]

                if user_data["role"] == "Ta":
                    active_ta = name
                    if name not in source.tas:
                        tas.append(name)
                        source.tas.append(name)

                    return render_template("ta.html", name=name)
                else:
                    if not source.isElement(name):
                        source.enqueue((name,datetime.now()))
            else:
                flash("GTID not found")
    return render_template("index.html",wait=avg_wait)
