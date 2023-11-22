

class TestData:

    base_url = "https://restful-booker.herokuapp.com/booking/"

    booking_data = {
        "firstname" : "John",
        "lastname" : "Doe",
        "totalprice" : 5000,
        "depositpaid" : True,
        "bookingdates" : {
            "checkin" : "2024-12-15",
            "checkout" : "2024-12-25"
        },
        "additionalneeds" : "Breakfast"
        }