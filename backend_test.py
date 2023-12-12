import requests

base_url = "http://localhost:5000/users"


def test_add_user():
    payload = {"name": "John Doe", "id": "123"}
    response = requests.post(f"{base_url}", json=payload)
    assert response.status_code == 200
    assert response.json() == payload


def test_get_user():
    payload = {"name": "John Doe", "id": "123"}
    response_create_user = requests.post(f"{base_url}", json=payload)
    user_id = "123"
    response_get_user = requests.get(f"{base_url}/{user_id}")
    assert response_get_user.status_code == 200
    assert response_get_user.json() == payload


def test_get_not_existing_user():
    user_id = "invalid_id"
    response = requests.get(f"{base_url}/{user_id}")
    assert response.status_code == 404


def test_get_users():
    response = requests.get(f"{base_url}")
    assert response.status_code == 200


def test_edit_user():
    user_id = "123"
    payload = {"name": "Updated Name", "id": user_id}
    response = requests.put(f"{base_url}/{user_id}", json=payload)
    assert response.status_code == 200
    assert response.json() == payload


def test_delete_user():
    user_id = "123"
    response = requests.delete(f"{base_url}/{user_id}")
    assert response.status_code == 200
