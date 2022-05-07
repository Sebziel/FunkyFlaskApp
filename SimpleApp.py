from datetime import datetime
from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("welcome.html", message='Message from view!')

@app.route("/FirstPage")
def FirstPage():
    return "There's First page it was server at " +str(datetime.now())

counter = 0

@app.route("/ViewCounter")
def ViewCounter():
    global counter
    counter += 1
    return "The page was viewed " + str(counter) + " times"