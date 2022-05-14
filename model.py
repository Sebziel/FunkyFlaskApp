import json

def load_db():
    with open("dbmock.json") as f:
        return json.load(f)

db = load_db()


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
    return