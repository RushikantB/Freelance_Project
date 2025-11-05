from Utils.API_Helpers import APIClient


def test_login_api():
    client = APIClient()
    payload = {
        "email": "",
        "password": ""
    }

    response = client.post("/verifyUser", data=payload)
    assert response.status_code == 200
    assert "token" in response.json()


def test_get_user_api():
    client = APIClient()
    response = client.get("/get_users")
    assert response.status_code == 200
    assert "token" in response.json()
