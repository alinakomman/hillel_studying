import pytest
import requests


first_test_data = [("Hju", "Fox", "awershjdf1hjo234iuy@yu.com", "ghjyu123456G", "ghjyu123456G")]
second_test_data = [("Hju", "Fox", "awershjdf1hjo234iuy@yu.com", "ghjyu123456G", "ghjyu123456GZ")]


@pytest.mark.parametrize("name, last_name, email, password, repeat_password", first_test_data)
def test_post_user(name, last_name, email, password, repeat_password):
    creds = {
        "name": name,
        "lastName": last_name,
        "email": email,
        "password": password,
        "repeatPassword": repeat_password
    }
    session = requests.session()
    post_new_user = session.post(url="https://qauto2.forstudy.space/api/auth/signup", json=creds)
    assert post_new_user.status_code == 201


@pytest.mark.parametrize("name, last_name, email, password, repeat_password", first_test_data)
def test_singin_user(name, last_name, email, password, repeat_password):
    creds = {
        "name": name,
        "lastName": last_name,
        "email": email,
        "password": password,
        "repeatPassword": repeat_password
    }
    session = requests.session()
    signin_user = session.post(url="https://qauto2.forstudy.space/api/auth/signin", json=creds)
    assert signin_user.status_code == 200


@pytest.mark.parametrize("name, last_name, email, password, repeat_password", first_test_data)
def test_check_with_correctdata(name, last_name, email, password, repeat_password):
    creds = {
        "name": name,
        "lastName": last_name,
        "email": email,
        "password": password,
        "repeatPassword": repeat_password
    }
    session = requests.session()
    check_with_correct = session.get(url="https://qauto2.forstudy.space/api/users/current", json=creds)
    assert check_with_correct.status_code == 200


@pytest.mark.parametrize("name, last_name, email, password, repeat_password", second_test_data)
def test_check_with_incorrectdata(name, last_name, email, password, repeat_password):
    creds = {
        "name": name,
        "lastName": last_name,
        "email": email,
        "password": password,
        "repeatPassword": repeat_password
    }
    session = requests.session()
    check_with_incorrect = session.get(url="https://qauto2.forstudy.space/api/users/current", json=creds)
    assert check_with_incorrect.status_code == 401
