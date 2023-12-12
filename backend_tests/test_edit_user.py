import requests
import pytest
from constants import BASE_URL, USER_ID, UPDATED_NAME, INVALID_USER_ID
from conftest import add_user, sample_user, get_user_by_id

def test_edit_user(sample_user):
    add_user(sample_user)
    payload = {"name": UPDATED_NAME, "id": USER_ID}
    response = requests.put(f"{BASE_URL}/{USER_ID}", json=payload)
    assert response.status_code == 200
    assert response.json() == payload
    assert get_user_by_id(USER_ID) == False


def test_edit_unexisting_user():
    payload = {"name": UPDATED_NAME, "id": INVALID_USER_ID}
    response = requests.put(f"{BASE_URL}/{INVALID_USER_ID}", json=payload)
    assert response.status_code == 404