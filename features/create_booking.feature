Feature: Create a booking
    Scenario: User creates a new booking
        Given The API is available
        When A valid POST request is sent to create a new booking
        Then The response should contain contain the newly created booking details
        And The created bookingid should be in the booking ids