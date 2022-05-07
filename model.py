import json

def load_db():
    with open("dbmock.json") as f:
        return json.load(f)

db = load_db()