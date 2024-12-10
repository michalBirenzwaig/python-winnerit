from enum import verify

import pytest
import requests
from assertpy import assert_that

from pythonProject.tests.req_res.requests_basic import response


@pytest.fixture()
def base_url():
    return "https://jsonplaceholder.typicode.com/users"

def test_get_users(base_url):
    response=requests.get(base_url, verify=False)
    assert response.status_code==200
    assert len(response.json())==10

def test_get_user_by_id(base_url):
    response=requests.get(f"{base_url}/1",verify=False)
    assert response.status_code==200
    assert (response.json()["name"]=="Leanne Graham")
    assert (response.json()["email"]=="Sincere@april.biz")

def test_user_not_found(base_url):
    response=requests.get(f"{base_url}/999",verify=False)
    assert response.status_code==404

def test_get_user_by_id_2(base_url):
    response=requests.get(f"{base_url}/2",verify=False)
    assert response.status_code==200
    assert_that(response.json()).contains_key('id')
    assert_that(response.json()).contains_key('username')
    assert_that(response.json()['address']).contains_key('suite')
    assert_that(response.json()['company']).contains_key('name')


params = [(3, "Clementine Bauch"), (4, "Patricia Lebsack"), (5, "Chelsey Dietrich")]
@pytest.mark.parametrize("user_id, user_name", params)
def test_get_users(user_id, user_name,base_url):
    response = requests.get(f"{base_url}/{user_id}",verify=False)
    assert response.status_code == 200
    assert response.json()["id"] == user_id
    assert response.json()["name"] == user_name

