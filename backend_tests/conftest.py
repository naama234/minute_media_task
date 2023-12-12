import requests
import pytest
from constants import BASE_URL, NAME, USER_ID

@pytest.fixture
def sample_user():
    return {
        "name": NAME,
        "id": USER_ID
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
