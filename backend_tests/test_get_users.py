import pytest
import requests
from conftest import NAME, USER_ID, BASE_URL, add_user, find_user_in_user_list, sample_user


def test_get_users(sample_user):
    add_user(sample_user)
    response = requests.get(f"{BASE_URL}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert find_user_in_user_list(response.json(), sample_user) == True

