from Utils.API_Helpers import APIClient
from Utils.schema_validator import validate_json_schema
import json
import uuid
import pytest


@pytest.mark.api
def test_get_user_api():
    client = APIClient(use_auth=True)

    # Check for correct id before executing the script
    response = client.get("/public/v2/posts/257567")
    assert response.status_code == 200

    data = response.json()
    schema_path = "/Users/rushikantbhosale/Documents/Rushikant/Automation/Freelance_Framework/Schemas/get_user_schemas.json"
    validate_json_schema(data, schema_path)
    print(data)


@pytest.mark.api
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

    schema_path = "/Users/rushikantbhosale/Documents/Rushikant/Automation/Freelance_Framework/Schemas/post_user_schemas.json"
    validate_json_schema(data, schema_path)
    print(data)


@pytest.mark.api
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


@pytest.mark.api
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
