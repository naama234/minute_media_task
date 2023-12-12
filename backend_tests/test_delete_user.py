import requests
from constants import BASE_URL, USER_ID, INVALID_USER_ID
from conftest import add_user, get_user_by_id, find_user_in_user_list, sample_user_with_long_id


def test_delete_user(sample_user):
    add_user(sample_user)
    response = requests.delete(f"{BASE_URL}/{USER_ID}")
    assert response.status_code == 200
    assert find_user_in_user_list(response.json(), sample_user) == False
    assert get_user_by_id(USER_ID) == False


def test_delete_unexisting_user():
    response = requests.delete(f"{BASE_URL}/{INVALID_USER_ID}")
    assert response.status_code == 500


def test_delete_with_long_id(sample_user_with_long_id):
    add_user(sample_user_with_long_id)
    response = requests.delete(f"{BASE_URL}/{USER_ID}")
    assert response.status_code == 200
    assert find_user_in_user_list(response.json(), sample_user_with_long_id) == False
    assert get_user_by_id(USER_ID) == False
