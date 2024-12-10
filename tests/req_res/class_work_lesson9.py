import requests
import pprint
from assertpy import assert_that

BASE_URL = "https://reqres.in/api"

def test_Single_user_not_found():
    response=requests.get(f"{BASE_URL}/users/{999}", verify=False)
    assert response.status_code==404
    assert response.reason=="Not Found"
    #pprint.pprint(response.reason)

def test_login_successful():
    user={"email": "eve.holt@reqres.in", "password": "cityslicka"}
    response=requests.post(f"{BASE_URL}/login",json=user, verify=False)
    assert response.status_code == 200
    assert "token" in response.json()

def test_register_unsuccessful():
    data = {"email": "sydney@fife"}
    response=requests.post(f"{BASE_URL}/register",json=data, verify=False)
    assert response.status_code==400
    assert "error" in response.json()
    assert response.json()['error']=="Missing password"

