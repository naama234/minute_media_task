import requests
import pytest
from constants import BASE_URL, INVALID_USER_ID
from conftest import get_user_by_id


def test_get_user(sample_user):
    add_response = requests.post(BASE_URL, json=sample_user)
    user_id = add_response.json()["id"]
    assert get_user_by_id(user_id) == True


def test_get_not_existing_user():
    response = requests.get(f"{BASE_URL}/{INVALID_USER_ID}")
    assert response.status_code == 404
