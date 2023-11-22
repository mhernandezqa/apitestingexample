import pytest
from pytest_bdd import scenario, given, when, then
import json
from utils.actions import *
from data.test_data import TestData


URL = TestData().base_url


class DeleteBookingHelper:
    booking = {}
    booking_response = {}
    booking_ids = []


@pytest.fixture
def test_data():
    test_data = TestData()
    return test_data


@pytest.fixture
def application():
    helper = DeleteBookingHelper()
    return helper


@scenario('../features/delete_booking.feature','User deletes a booking')
def test_delete_booking():
    pass


@given('The API is available')
def api_available():

    response = send_get_request(url=URL)
    assert response.status_code == 200


@given('The booking to delete exists')
def booking_exists(application):
    booking = get_random_booking(url=URL)
    application.booking = booking
    assert booking


@when('A valid DELETE request is sent to create a booking')
def valid_delete_request(application):
    url = URL + str(application.booking["bookingid"])
    print(url)
    response = send_delete_request(url=url)
    assert response.status_code == 201


@then('The deleted bookingid should not be in the booking ids')
def booking_id_deleted(application):
    url = URL + str(application.booking["bookingid"])
    print(url)
    response = send_get_request(url=url)
    assert response.status_code == 404