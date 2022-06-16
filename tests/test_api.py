import json
import requests

def load_db():
    #Path to dbmock have to be called from root directory, otherwise have to be changed
    with open("JsonData/dbmock.json") as f:
        return json.load(f)

baseurl = 'http://localhost:5000/api/card/'

db_lenght = len(load_db())
db_range = range(db_lenght)

def test_api():
    for db_object in db_range:
        response = requests.get(baseurl + str(db_object))
        #get the keys of the dbmock.jsonfile
        dictkey = response.json().keys()
        #convert to list and later to str and get the first object
        key = str(list(dictkey)[0])
        asserttionMessage = "expected  key = answer , got: "
        #Check if all cards from dbmock.json have answer=question schema
        assert key == "answer", asserttionMessage + key
