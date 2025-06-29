import requests

BASE_URL = "http://localhost:5000/api"

def test_login_success():
    res = requests.post(f"{BASE_URL}/login", json={
        "email": "test@example.com",
        "password": "test123"
    })
    assert res.status_code == 200
    assert "token" in res.json()

def test_login_fail():
    res = requests.post(f"{BASE_URL}/login", json={
        "email": "wrong@example.com",
        "password": "wrongpass"
    })
    assert res.status_code in [400, 401]
