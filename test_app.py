import pytest
from app import app

@pytest.fixture
def test_client():
    app.config["TESTING"] = True
    client = app.test_client()
    yield client


# Test index endpoint
def test_index(test_client):
    response = test_client.get("/")
    data = response.get_json()
    assert response.status_code == 200
    assert data["message"] == "Welcome To My Drinks API"

# Test drinks endpoint
def test_drinks(test_client):
    response = test_client.get("/drinks")
    data = response.get_json()
    assert response.status_code == 200
    assert isinstance(data, dict)
    assert list(data.keys()) ==["drinks"]

# Test description endpoint
def test_get_description_valid(test_client):
    response = test_client.get("/description", json={"requested_drink": "Grape"})
    data = response.get_json()
    assert response.status_code == 200
    assert data["description"] == "Delicious grape fruit drink"

def test_get_description_unavailable(test_client):
    response = test_client.get("/description", json={"requested_drink": "Pear"})
    data = response.get_json()
    assert response.status_code == 404
    assert data["error"] == "The drink you've requested is not available at this time."

def test_get_description_no_input(test_client):
    response = test_client.get("/description", json={})
    data = response.get_json()
    assert response.status_code == 400
    assert data["error"] == "Provide drink to check description"
