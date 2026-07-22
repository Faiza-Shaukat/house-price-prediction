"""
Basic tests for the House Price Predictor API.
Run with: pytest test_api.py
"""
from fastapi.testclient import TestClient
from api import app

client = TestClient(app)


def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()


def test_predict_endpoint():
    payload = {
        "area": 150,
        "bedrooms": 3,
        "age": 10,
        "proximity": 5.0
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "predicted_price" in data
    assert isinstance(data["predicted_price"], float)
    assert data["predicted_price"] > 0


def test_predict_invalid_input():
    payload = {
        "area": "not_a_number",
        "bedrooms": 3,
        "age": 10,
        "proximity": 5.0
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 422
