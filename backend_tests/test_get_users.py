import requests
from conftest import BASE_URL, add_user, find_user_in_user_list


def test_get_users(sample_user):
    add_user(sample_user)
    response = requests.get(f"{BASE_URL}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert find_user_in_user_list(response.json(), sample_user) == True

