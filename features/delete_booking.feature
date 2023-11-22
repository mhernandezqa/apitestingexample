Feature: Delete a booking
    Scenario: User deletes a booking
        Given The API is available
        And The booking to delete exists
        When A valid DELETE request is sent to create a booking
        Then The deleted bookingid should not be in the booking ids