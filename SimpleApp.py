from datetime import datetime
from flask import Flask, render_template, abort
from model import db , get_counter_value , update_counter

app = Flask(__name__)

## Todo: welcome_counter = 0

@app.route("/")
def welcome():
    update_counter()
    current_time = str(datetime.now())
    counter = get_counter_value()
    return render_template("welcome.html", cards=db, current_time = current_time, counter = counter)

@app.route("/card/<int:index>")
def card_view(index):
    update_counter()
    try:
        card = db[index]
        return render_template("card.html", card=card, index=index, max_index=len(db)-1)
    except IndexError:
        abort(404)

@app.route("/api/card/<int:index>")
def api_card_view(index):
    try:
        return db[index]
    except IndexError:
        abort(404)

@app.route("/FirstPage")
def FirstPage():
    update_counter()
    return "There's First page it was served at " +str(datetime.now())

#counter = 0

def funkcja():
    return "Wywolalem funkcje"

@app.route("/ViewCounter")
def ViewCounter():
    update_counter()
    return str(get_counter_value())
    # global counter
    # counter += 1
    # return "The page was viewed " + str(counter) + " times"