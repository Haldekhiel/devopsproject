def test_get_real_estates(client):
    response = client.get("/real_estates/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)