from Utils.API_Helpers import APIClient

def test_login_api():
    client = APIClient()
    payload = {
    "email": "rbhosale@health.saisystems.com",
    "password": "Sai@12345"
}

    response = client.post("/verifyUser", data=payload)
    assert response.status_code == 200
    assert "token" in response.json()
