import requests
from constants import BASE_URL


def test_add_user(sample_user):
    response = requests.post(BASE_URL, json=sample_user)
    assert response.status_code == 200
    assert response.json() == sample_user


def test_add_user_with_long_name(sample_user_with_long_name):
    response = requests.post(BASE_URL, json=sample_user_with_long_name)
    assert response.status_code == 200
    assert response.json() == sample_user_with_long_name


def test_add_user_with_long_id(sample_user_with_long_id):
    response = requests.post(BASE_URL, json=sample_user_with_long_id)
    assert response.status_code == 200
    assert response.json() == sample_user_with_long_id


def test_add_user_with_empty_name(sample_user_without_name):
    response = requests.post(BASE_URL, json=sample_user_without_name)
    assert response.status_code == 400


def test_add_user_with_empty_id(sample_user_without_id):
    response = requests.post(BASE_URL, json=sample_user_without_id)
    assert response.status_code == 400


def test_add_user_with_empty_id_and_empty_name(sample_user_without_id_and_name):
    response = requests.post(BASE_URL, json=sample_user_without_id_and_name)
    assert response.status_code == 400
    assert response.json() == sample_user_without_id_and_name


def test_add_us_with_same_id(sample_user):
    first_response = requests.post(BASE_URL, json=sample_user)
    second_response = requests.post(BASE_URL, json=sample_user)
    assert second_response.status_code == 400
