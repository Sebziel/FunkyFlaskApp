# from pickle import NONE
import json

def get_counter_data():
    with open("counter.json", "r") as counterJson:
        data = json.load(counterJson)
    return data

def get_counter_value():
    counterValue = get_counter_data()
    return counterValue["counter"]

def update_counter():
    value = get_counter_data()
    value["counter"] += 1
    with open("counter.json", "w") as jsonfile:
        json.dump(value, jsonfile)

update_counter()

#update_counter()


"""
def find_counter():
    for item in db:
        key_list = list(item.keys())[0]
        if "counter" in key_list:
            result = item.get("counter")
            print("im here")
        else:
            result = "counter not present"
            print("im in else")
    return result

print(find_counter())"""

"""

for object in db:
    print(object.get("counter"))

def find_counter():
    for item in db:
        print(list(item.keys())[0])
        return "null"

print(find_counter())



cardnr = 0
print(str(db))

def card_view():
    global cardnr
    card = db[cardnr]
    return card

print(cardnr)

while cardnr < len(db):
    print(card_view())
    cardnr += 1
    print(str(cardnr) + "Numer z while'a")"""