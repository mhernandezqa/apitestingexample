import requests
import json
import random
from data.test_data import TestData


def send_get_request(url):
    headers = {"Content-Type": "application/json"}
    response = requests.get(url, headers=headers)
    return response


def send_post_request(url, data):
    payload = json.dumps(data)
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, headers=headers, data=payload)
    return response


def send_delete_request(url):
    headers = {"Content-Type": "application/json",
               "Authorization": "Basic YWRtaW46cGFzc3dvcmQxMjM="}
    response = requests.delete(url, headers=headers)
    return response


def get_random_booking(url):
    response = send_get_request(url)
    data = json.loads(response.text)
    return random.choice(data)


class TestData:

    url = "https://restful-booker.herokuapp.com/booking"

    booking_data = {
    "firstname" : "Miguel",
    "lastname" : "Hernandez",
    "totalprice" : 5000,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2023-12-15",
        "checkout" : "2023-12-25"
    },
    "additionalneeds" : "Breakfast"
    }