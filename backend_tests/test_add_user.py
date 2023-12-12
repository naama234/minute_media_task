import requests
from constants import BASE_URL


def test_add_user(sample_user):
    response = requests.post(BASE_URL, json=sample_user)
    assert response.status_code == 200
    assert response.json() == sample_user
