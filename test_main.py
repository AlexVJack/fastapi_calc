from fastapi.testclient import TestClient
import pymongo

from main import app

client = TestClient(app)

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["calcdb"]


def test_addition():
    "testing response of addition page and correct result"
    response = client.get("/add/2/2")
    assert response.status_code == 200
    assert response.json() == {"result of addition": 4}


def test_subtraction():
    "testing response of subtraction page and correct result"
    response = client.get("/sub/6/3")
    assert response.status_code == 200
    assert response.json() == {"result of subtraction": 3}


def test_division():
    "testing response of division page and correct result"
    response = client.get("/div/6/3")
    assert response.status_code == 200
    assert response.json() == {"result of division": 2}


def test_multiplication():
    "testing response of multiplication page and correct result"
    response = client.get("/mult/6/8")
    assert response.status_code == 200
    assert response.json() == {"result of multiplication": 48}


def test_division_by_zero():
    "testing the division by zero"
    response = client.get("/div/6/0")
    assert response.json() == "Unfortunately, Your rude Earth technology \
        does not allow dividing by zero!"


def test_db():
    "testing that last entries created by tests are in db"
    # getting last four entries to temp list
    cursor = mydb.results.find().sort([('_id', -1)]).limit(4)
    temp_list = []
    for item in cursor:
        temp_list.append(item)
    # testing entries to have correct values
    # multiplication
    assert temp_list[0]['operation'] == '6.0 * 8.0'
    assert temp_list[0]['result'] == 48
    # division
    assert temp_list[1]['operation'] == '6.0 / 3.0'
    assert temp_list[1]['result'] == 2
    # subtraction
    assert temp_list[2]['operation'] == '6.0 - 3.0'
    assert temp_list[2]['result'] == 3
    # addition
    assert temp_list[3]['operation'] == '2.0 + 2.0'
    assert temp_list[3]['result'] == 4
