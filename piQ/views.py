from flask import render_template, request, jsonify, url_for, flash
from piQ import app
from piQ.models import Queue
from piQ.logic import get_user_info, getAvergeWait
from datetime import datetime

source = Queue()
active_ta = ""

@app.route("/", methods = ["GET", "POST"])
def index():
    return process_request(request)

@app.route("/forgot")
def forgot():
    avg_wait = getAvergeWait(source)
    return render_template("forgot.html", wait=avg_wait)


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
    avg_wait = getAvergeWait(source)

    if request.method == "POST":
        #different possible TA button presses
        if request.form.get("remove"):
            source.dequeue()
            avg_wait = getAvergeWait(source)
            return render_template("ta.html", name=name, wait=avg_wait)
        elif request.form.get("clear"):
            temptas = source.tas
            source.clear()
            avg_wait = getAvergeWait(source)
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
            if user_data:
                name = user_data["name"]
                print(user_data)
                if user_data["role"] == "Ta":
                    active_ta = name
                    if name not in source.tas:
                        source.tas.append(name)

                    return render_template("ta.html", name=name, wait=avg_wait)
                else:
                    if not source.contains(name):
                        source.enqueue((name,datetime.now()))
            else:
                if len(gtid) == 9:
                    return render_template("index.html",wait=avg_wait, not_on_roster=True)
                else:
                    return render_template("index.html",wait=avg_wait, invalid=True)
    return render_template("index.html",wait=avg_wait)
