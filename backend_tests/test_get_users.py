import pytest
import requests
from conftest import  NAME, USER_ID, BASE_URL, add_user

def test_get_users():
    add_user(NAME, USER_ID)
    response = requests.get(f"{BASE_URL}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
