import requests

BASE_URL = "http://localhost:5000"


def test_home_page():
    """Test if the home page loads successfully."""
    response = requests.get(BASE_URL)
    assert response.status_code == 200, "Home page did not load successfully"
    assert (
        "<title>Calculator App</title>" in response.text
    ), "Calculator app title is missing"


def test_addition():
    """Test addition functionality."""
    payload = {"num1": 5, "num2": 3, "operation": "add"}
    response = requests.post(f"{BASE_URL}/calculate", data=payload)
    assert response.status_code == 200, "Failed to calculate addition"
    assert "Result: 8" in response.text, "Addition result is incorrect"


def test_subtraction():
    """Test subtraction functionality."""
    payload = {"num1": 5, "num2": 3, "operation": "subtract"}
    response = requests.post(f"{BASE_URL}/calculate", data=payload)
    assert response.status_code == 200, "Failed to calculate subtraction"
    assert "Result: 2" in response.text, "Subtraction result is incorrect"


def test_division_by_zero():
    """Test division by zero."""
    payload = {"num1": 5, "num2": 0, "operation": "divide"}
    response = requests.post(f"{BASE_URL}/calculate", data=payload)
    assert response.status_code == 200, "Failed to handle division by zero"
    assert (
        "Error: Division by zero" in response.text
    ), "Division by zero error message is incorrect"


if __name__ == "__main__":
    print("Running tests...")
    test_home_page()
    test_addition()
    test_subtraction()
    test_division_by_zero()
    print("All tests passed!")
