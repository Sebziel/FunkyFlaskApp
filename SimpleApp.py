from datetime import datetime
from flask import Flask, render_template, abort
from model import db

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("welcome.html", cards=db)

@app.route("/card/<int:index>")
def card_view(index):
    try:
        card = db[index]
        return render_template("card.html", card=card, index=index, max_index=len(db)-1)
    except IndexError:
        abort(404)

@app.route("/FirstPage")
def FirstPage():
    return "There's First page it was server at " +str(datetime.now())

counter = 0

@app.route("/ViewCounter")
def ViewCounter():
    global counter
    counter += 1
    return "The page was viewed " + str(counter) + " times"