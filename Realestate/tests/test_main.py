import pytest
from app.main import app, get_real_estate, create_real_estate, RealEstate

def test_get_real_estates(client):
    response = client.get("/real_estates/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
