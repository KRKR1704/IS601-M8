# Author: Roopesh Kumar Reddy Kaipa
# Date: 10/27/2025
import pytest  # Import the pytest framework for writing and running tests
from fastapi.testclient import TestClient  # Import TestClient for simulating API requests
from main import app  # Import the FastAPI app instance from your main application file

@pytest.fixture
def client():
    """
    Pytest Fixture to create a TestClient for the FastAPI application.

    This fixture initializes a TestClient instance that can be used to simulate
    requests to the FastAPI application without running a live server. The client
    is yielded to the test functions and properly closed after the tests complete.

    Benefits:
    - Speeds up testing by avoiding the overhead of running a server.
    - Allows for testing API endpoints in isolation.
    """
    with TestClient(app) as client:
        yield client

def test_add_api(client):
    """
    Test the Addition API Endpoint.

    This test verifies that the `/add` endpoint correctly adds two numbers provided
    in the JSON payload and returns the expected result.

    Steps:
    1. Send a POST request to the `/add` endpoint with JSON data `{'a': 10, 'b': 5}`.
    2. Assert that the response status code is `200 OK`.
    3. Assert that the JSON response contains the correct result (`15`).
    """
    response = client.post('/add', json={'a': 10, 'b': 5})
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    assert response.json()['result'] == 15, f"Expected result 15, got {response.json()['result']}"

def test_subtract_api(client):
    """
    Test the Subtraction API Endpoint.

    This test verifies that the `/subtract` endpoint correctly subtracts the second number
    from the first number provided in the JSON payload and returns the expected result.

    Steps:
    1. Send a POST request to the `/subtract` endpoint with JSON data `{'a': 10, 'b': 5}`.
    2. Assert that the response status code is `200 OK`.
    3. Assert that the JSON response contains the correct result (`5`).
    """
    response = client.post('/subtract', json={'a': 10, 'b': 5})
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    assert response.json()['result'] == 5, f"Expected result 5, got {response.json()['result']}"

def test_multiply_api(client):
    """
    Test the Multiplication API Endpoint.

    This test verifies that the `/multiply` endpoint correctly multiplies two numbers
    provided in the JSON payload and returns the expected result.

    Steps:
    1. Send a POST request to the `/multiply` endpoint with JSON data `{'a': 10, 'b': 5}`.
    2. Assert that the response status code is `200 OK`.
    3. Assert that the JSON response contains the correct result (`50`).
    """
    response = client.post('/multiply', json={'a': 10, 'b': 5})
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    assert response.json()['result'] == 50, f"Expected result 50, got {response.json()['result']}"

def test_divide_api(client):
    """
    Test the Division API Endpoint.

    This test verifies that the `/divide` endpoint correctly divides the first number
    by the second number provided in the JSON payload and returns the expected result.

    Steps:
    1. Send a POST request to the `/divide` endpoint with JSON data `{'a': 10, 'b': 2}`.
    2. Assert that the response status code is `200 OK`.
    3. Assert that the JSON response contains the correct result (`5`).
    """
    response = client.post('/divide', json={'a': 10, 'b': 2})
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    assert response.json()['result'] == 5, f"Expected result 5, got {response.json()['result']}"

def test_divide_by_zero_api(client):
    """
    Test the Division by Zero API Endpoint.

    This test verifies that the `/divide` endpoint correctly handles division by zero
    by returning an appropriate error message and status code.

    Steps:
    1. Send a POST request to the `/divide` endpoint with JSON data `{'a': 10, 'b': 0}`.
    2. Assert that the response status code is `400 Bad Request`.
    3. Assert that the JSON response contains an 'error' field with the message "Cannot divide by zero!".
    """
    response = client.post('/divide', json={'a': 10, 'b': 0})
    assert response.status_code == 400, f"Expected status code 400, got {response.status_code}"
    assert 'error' in response.json(), "Response JSON does not contain 'error' field"
    assert "Cannot divide by zero!" in response.json()['error'], \
        f"Expected error message 'Cannot divide by zero!', got '{response.json()['error']}'"


def test_power_api(client):
    """
    Test the Power API Endpoint.

    This test verifies that the `/power` endpoint correctly raises a to the power of b
    and returns the expected result.
    """
    response = client.post('/power', json={'a': 2, 'b': 10})
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    assert response.json()['result'] == 1024.0, f"Expected result 1024.0, got {response.json()['result']}"

    response = client.post('/power', json={'a': 16, 'b': 0.5})
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    assert response.json()['result'] == 4.0, f"Expected result 4.0, got {response.json()['result']}"

    response = client.post('/power', json={'a': -1, 'b': 0.5})
    assert response.status_code == 400, f"Expected status code 400 for invalid power, got {response.status_code}"
