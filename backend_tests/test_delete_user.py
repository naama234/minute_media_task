import requests
from constants import BASE_URL, USER_ID
from conftest import add_user, sample_user, get_user_by_id


def test_delete_user(sample_user):
    add_user(sample_user)
    response = requests.delete(f"{BASE_URL}/{USER_ID}")
    assert response.status_code == 200
    assert get_user_by_id(USER_ID) == False
