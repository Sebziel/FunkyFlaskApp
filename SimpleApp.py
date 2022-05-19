from datetime import datetime
from flask import Flask, render_template, abort
from model import db , get_counter_value , update_counter
import FlowersUtilities

app = Flask(__name__)

## Todo: welcome_counter = 0

@app.route("/")
def welcome():
    update_counter()
    current_time = str(datetime.now())
    counter = get_counter_value()
    allFlowersDict = FlowersUtilities.get_flowers_data()
    allFlowers = allFlowersDict[0]
    return render_template("welcome.html", cards=db, current_time = current_time, counter = counter , allFlowers = allFlowers)

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

@app.route("/add_card")
def add_card():
    update_counter()
    return render_template("add_card.html")


@app.route("/FirstPage")
def FirstPage():
    update_counter()
    return "There's First page it was served at " +str(datetime.now())


@app.route("/ViewCounter")
def ViewCounter():
    update_counter()
    return str(get_counter_value())

@app.route("/flowerList")
def flower_list_view():
    update_counter()
    try:
        flowerlist = FlowersUtilities.get_flowers_list()
        return render_template("flowers.html", flowerlist=flowerlist)
    except IndexError:
        abort(404)



@app.route("/flower/<string:dindex>")
def flower_view(dindex):
    update_counter()
    try:
        specificFlower = FlowersUtilities.get_flowers_data()
        flowerlist = specificFlower[0] #Wyciaga zerowy obiekt ze wzgledu na strukture danych w Jsonie
        flower = flowerlist[dindex]
        return render_template("flower.html", flower=flower)
    except IndexError:
        abort(404)