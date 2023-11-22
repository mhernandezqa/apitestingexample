import pytest
from pytest_bdd import scenario, given, when, then
import json
from utils.actions import *
from data.test_data import TestData


URL = TestData().base_url


class BookingHelper:
    booking_request = {}
    booking_response = {}
    booking_ids = []


@pytest.fixture
def test_data():
    test_data = TestData()
    return test_data


@pytest.fixture
def application():
    helper = BookingHelper()
    return helper


@scenario('../features/create_booking.feature','User creates a new booking')
def test_create_booking():
    pass


@given('The API is available')
def api_available(application):

    response = send_get_request(url=URL)
    assert response.status_code == 200
    

@when('A valid POST request is sent to create a new booking')
def valid_post_request(application, test_data):
    
    data = test_data.booking_data
    application.post_booking_request = data
    response = send_post_request(url=URL, data=data)
    application.booking_response = json.loads(response.text)
    assert response.status_code == 200


@then('The response should contain contain the newly created booking details')
def booking_created_succesfully(application):
    success = True
    messages = []
    for key, value in application.booking_request.items():
        response_value = application.booking_response['booking'][f'{key}']
        if value == response_value:
            success = True
        else:
            success = False
            messages.append(f"the {key} value: {value} in the request is not equal to the value in the response: {response_value}")
    assert success, messages


@then('The created bookingid should be in the booking ids')
def booking_in_booking_ids(application):
    response = send_get_request(url=URL)
    application.booking_ids = json.loads(response.text)
    print(type(application.booking_ids))
    assert any(booking["bookingid"] == application.booking_response["bookingid"] for booking in application.booking_ids)