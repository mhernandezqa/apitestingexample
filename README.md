# Booking REST API Testing Example

This project provides a simple yet comprehensive demonstration of how to perform testing on a RESTful booking API using Python, pytest, and pytest-bdd.

You can find more about the restful-booker project and its API documentation here:

https://restful-booker.herokuapp.com/apidoc/

## Getting Started

To get started with this example, follow these steps:

### Prerequisites

Make sure you have the following prerequisites installed:

- Python (3.x recommended)
- pytest (`pip install pytest`)
- pytest-bdd (`pip install pytest-bdd`)

### Installation

1. Clone the repository:

   ```
   git clone https://github.com/mhernandezqa/apitestingexample.git
   ```

2. Install dependencies:

```
   pip install -r requirements.txt
```

### Project Structure

```

apitestingexample/
│
├── data/
│   ├── __init__.py
│   ├── test_data.py
│   └── ...
│
├── features/
│   ├── __init__.py
│   ├── create_booking.feature
│   ├── delete_booking.feature
│   └── ...
│
├── tests/
│   ├── __init__.py
│   ├── test_create_booking.py
│   ├── test_delete_booking.py
│   └── ...
│
├── utils/
│   ├── __init__.py
│   ├── actions.py
│   └── ...
│
├── ...
└── requirements.txt

```

* test_data.py: Defines test data and base URL for the API.
* features/: Contains BDD feature files for scenarios.
* tests/test_create_booking.py: Implements test scenarios for creating bookings.
* tests/test_delete_booking.py: Implements test scenarios for deleting bookings.
* utils/actions.py: Provides utility functions for sending GET, POST, and DELETE requests, as well as getting random booking data.
* data/test_data.py: Defines default test data for bookings.

### Running Tests

You can run the tests by executing the following commands:

```

pytest tests/

```