import requests

def test_mainSite():
    response = requests.get('http://localhost:5000')
    asserttionMessage = "expected  response = 200 , got: "
    assert response.status_code == 200, asserttionMessage + str(response.status_code)