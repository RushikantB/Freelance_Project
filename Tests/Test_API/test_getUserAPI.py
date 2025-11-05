from Utils.API_Helpers import APIClient
import json
import uuid


def test_get_user_api():
    client = APIClient(use_auth=True)
    response = client.get("/public/v2/posts/254014")
    assert response.status_code == 200

    data = response.json()
    assert "id" in data  # validate that user list exists
    assert "title" in data
    assert "body" in data
    assert "user_id" in data
    assert isinstance(data, dict)
    print(data)


def test_post_user_api():
    client = APIClient(use_auth=True)
    unique_id = str(uuid.uuid4())[:8]
    name = f"Rushi_{unique_id}"
    email = f"testmail_{unique_id}@test.com"
    payload = {
        "name": name,
        "email": email,
        "gender": "male",
        "status": "active"
    }
    response = client.post("/public/v2/users", data=payload)
    assert response.status_code == 201
    data = response.json()
    assert "name" in data
    assert "email" in data
    assert "gender" in data
    assert "status" in data

    assert isinstance(data, dict)
    print(data)


def test_put_user_api():
    client = APIClient(use_auth=True)
    payload = {
        "post_id": 254331,
        "name": "Suraj M B",
        "email": "hibsdsrtrwtds@test.com",
        "body": "dsfdmadsfsdfcsdfsfdsfle"
    }
    response = client.put("/public/v2/comments/172967", data=payload)
    assert response.status_code == 200
    data = response.json()
    assert "post_id" in data
    assert "email" in data
    assert "name" in data
    assert "body" in data

    assert isinstance(data, dict)
    print(data)


def test_delete_user_api():
    client = APIClient(use_auth=True)
    response = client.delete("/public/v2/todos/92622")
    assert response.status_code in [200, 204]
    '''
    data = response.json()
    assert "user_id" in data
    assert "title" in data
    assert "due on" in data
    assert isinstance(data, dict)
    '''
