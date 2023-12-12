import requests
import pytest
from constants import BASE_URL, NAME, USER_ID, LONG_NAME, LONG_ID


@pytest.fixture
def sample_user():
    return {
        "name": NAME,
        "id": USER_ID
    }


@pytest.fixture
def sample_user_with_long_name():
    return {
        "name": LONG_NAME,
        "id": USER_ID
    }


@pytest.fixture
def sample_user_with_long_id():
    return {
        "name": NAME,
        "id": LONG_ID
    }


@pytest.fixture
def sample_user_without_name():
    return {
        "name": '',
        "id": USER_ID
    }


@pytest.fixture
def sample_user_without_id():
    return {
        "name": NAME,
        "id": ''
    }


@pytest.fixture
def sample_user_without_id_and_name():
    return {
        "name": '',
        "id": ''
    }


def get_user_by_id(user_id):
    response = requests.get(f"{BASE_URL}/{user_id}")
    try:
        assert response.status_code == 200
        assert response.json() == {"name": NAME, "id": str(user_id)}
        return True
    except AssertionError:
        return False


def get_user_name_by_id(user_id):
    response = requests.get(f"{BASE_URL}/{user_id}")
    try:
        return response.json()['name']
    except requests.exceptions.JSONDecodeError:
        return None


def add_user(payload):
    response = requests.post(BASE_URL, json=payload)
    return response


def find_user_in_user_list(user_list, user):
    for user_in_list in user_list:
        if user['id'] == user_in_list['id'] and user['name'] == user_in_list['name']:
            return True
    return False
