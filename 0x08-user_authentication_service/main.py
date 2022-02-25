#!/usr/bin/env python3
"""Integration test module for Flask app"""
from auth import Auth
import requests


AUTH = Auth()


def register_user(email: str, password: str) -> None:
    """Test register user route"""
    payload = {'email': email, 'password': password}
    r = requests.post('http://127.0.0.1:5000/users', data=payload)
    assert r.status_code == 200
    assert r.json() == {'email': email, "message": "user created"}


def log_in_wrong_password(email: str, password: str) -> None:
    """Test login with wrong password"""
    payload = {'email': email, 'password': password}
    r = requests.post('http://127.0.0.1:5000/sessions', data=payload)
    assert r.status_code == 401, f"staus code:{r.status_code}"


def log_in(email: str, password: str) -> str:
    """Test login with correct password"""
    payload = {'email': email, 'password': password}
    r = requests.post('http://127.0.0.1:5000/sessions', data=payload)
    assert r.status_code == 200
    assert r.json() == {'email': email, "message": "logged in"}

    return r.cookies.get('session_id')


def profile_unlogged() -> None:
    """Test /profile route with invalid input"""
    r = requests.get('http://127.0.0.1:5000/profile')
    assert r.status_code == 403


def profile_logged(session_id: str) -> None:
    """Test /profile route with valid input"""
    cookies = {'session_id': session_id}
    r = requests.get('http://127.0.0.1:5000/profile', cookies=cookies)
    user = AUTH.get_user_from_session_id(session_id)
    assert r.status_code == 200
    assert r.json() == {'email': user.email}


def log_out(session_id: str) -> None:
    """Test /sessions route DELETE method"""
    cookies = {'session_id': session_id}
    r = requests.delete('http://127.0.0.1:5000/sessions', cookies=cookies)
    assert r.status_code == 200
    assert r.json() == {"message": "Bienvenue"}


def reset_password_token(email: str) -> str:
    """Test /reset_password POST method, creates a password"""
    payload = {'email': email}
    r = requests.post('http://127.0.0.1:5000/reset_password', data=payload)
    user = AUTH._db.find_user_by(email=email)
    assert r.status_code == 200
    assert r.json() == {'email': email, "reset_token": user.reset_token}

    return user.reset_token


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """Test /reset_password PUT method, update a password"""
    payload = {"email": email, "reset_token": reset_token,
               "new_password": new_password}
    r = request.put('http://127.0.0.1:5000/reset_password', data=payload)
    assert r.status_code == 200
    assert r.json() == {'email': email, "message": "Password updated"}


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    print(reset_token)
    '''
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
    '''
