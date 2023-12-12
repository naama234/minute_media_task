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
        "name": LONG_NAME,
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


def add_user(payload):
    return requests.post(f"{BASE_URL}", json=payload)
