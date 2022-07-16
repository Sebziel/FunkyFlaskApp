import requests

baseurl = 'http://localhost:5000/'

def test_techDetails():
    response = requests.get(baseurl + 'techDetails')
    asserttionMessage = "expected  response = 200 , got: "
    assert response.status_code == 200, asserttionMessage + str(response.status_code)

def test_card_list():
    response = requests.get(baseurl + 'card_list')
    asserttionMessage = "expected  response = 200 , got: "
    assert response.status_code == 200, asserttionMessage + str(response.status_code)

def test_FirstPage():
    response = requests.get(baseurl + 'FirstPage')
    asserttionMessage = "expected  response = 200 , got: "
    assert response.status_code == 200, asserttionMessage + str(response.status_code)

def test_card_list():
    response = requests.get(baseurl + 'card_list')
    asserttionMessage = "expected  response = 200 , got: "
    assert response.status_code == 200, asserttionMessage + str(response.status_code)