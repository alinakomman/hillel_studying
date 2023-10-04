import pytest
import requests


@pytest.fixture(scope="module")
def session():
    session = requests.session()
    yield session
    session.close()


first_test_data = [("Hju", "Fox", "lkiolkikkklll@yu.com", "ghjyu123456G", "ghjyu123456G")]
second_test_data = [("Hju", "Fox", "lkiolkikkklll@yu.com", "ghjyu123456G", "ghjyu123456GZ")]


@pytest.mark.parametrize("name, last_name, email, password, repeat_password", first_test_data)
def test_post_user(name, last_name, email, password, repeat_password, session):
    creds = {
        "name": name,
        "lastName": last_name,
        "email": email,
        "password": password,
        "repeatPassword": repeat_password
    }
    post_new_user = session.post(url="https://qauto2.forstudy.space/api/auth/signup", json=creds)
    assert post_new_user.status_code == 201


@pytest.mark.parametrize("name, last_name, email, password, repeat_password", first_test_data)
def test_signin_user(name, last_name, email, password, repeat_password, session):
    creds = {
        "name": name,
        "lastName": last_name,
        "email": email,
        "password": password,
        "repeatPassword": repeat_password
    }
    signin_user = session.post(url="https://qauto2.forstudy.space/api/auth/signin", json=creds)
    assert signin_user.status_code == 200


@pytest.mark.parametrize("name, last_name, email, password, repeat_password", first_test_data)
def test_check_with_correctdata(name, last_name, email, password, repeat_password, session):
    creds = {
        "name": name,
        "lastName": last_name,
        "email": email,
        "password": password,
        "repeatPassword": repeat_password
    }
    check_with_correct = session.get(url="https://qauto2.forstudy.space/api/users/current", json=creds)
    assert check_with_correct.status_code == 200


@pytest.fixture(scope="function")
def session_for_test_with_incorrectdata():
    session = requests.session()
    yield session
    session.close()


@pytest.mark.parametrize("name, last_name, email, password, repeat_password", second_test_data)
def test_check_with_incorrectdata(name, last_name, email, password, repeat_password, session_for_test_with_incorrectdata):
    creds = {
        "name": name,
        "lastName": last_name,
        "email": email,
        "password": password,
        "repeatPassword": repeat_password
    }
    check_with_incorrect = session_for_test_with_incorrectdata.get(url="https://qauto2.forstudy.space/api/users/current", json=creds)
    assert check_with_incorrect.status_code == 401
