#!/usr/bin/env python3
"""
Basic Flask app
"""
from auth import Auth
from flask import abort, Flask, jsonify, redirect, request, url_for
from sqlalchemy.orm.exc import NoResultFound


app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'])
def index():
    """ GET /
    Return:
    - jsonifiy {"message": "Bienvenue"}
    """
    return jsonify(message="Bienvenue")


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    """ POST /users/
    Return:
        - Register user and return jsonified info or
        - 400 if user email in db
    """
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        AUTH.register_user(email, password)
        return jsonify(email=email, message="user created")
    except ValueError:
        return jsonify(message="email already registered"), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """ POST /sessions/
    Create new session, store session ID as cookie, key is session_id on the\
            response
    Return:
        - JSON payload of the form
        - 401 if login information is incorrect
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        response = jsonify(email=email, message="logged in")
        response.set_cookie('session_id', session_id)
        return response
    else:
        abort(401)


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """Logout and delete current session"""
    session_id = request.cookies.get('session_id')
    if session_id is None:
        abort(403)

    user = AUTH.get_user_from_session_id(session_id)
    if user:
        AUTH.destroy_session(user.id)
        return redirect(url_for('index'))
    else:
        abort(403)


@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile():
    """ GET /profile
    Find user if exists
    Return:
        - Status code 200
        - payload {"email": "<user email>"}
        - 403 if user does not exist or session_id invalid
    """
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        return jsonify(email=user.email), 200
    else:
        abort(403)


@app.route('/reset_password', methods=['POST'], strict_slashes=False)
def get_reset_password_token():
    """ POST /reset_password
    Generates a token
    Return:
        - Status code 200
        - payload {"email": "<user email>", "reset_token": "<reset token>"}
        - 403 if email not registered
    """
    email = request.form.get('email')
    if email:
        try:
            token = AUTH.get_reset_password_token(email)
            return jsonify(email=email, reset_token=token), 200
        except ValueError:
            abort(403)


@app.route('/reset_password', methods=['PUT'], strict_slashes=False)
def update_password():
    """ PUT /reset_password
    Update the password
    Return:
        - Status code 200
        - Payload {"email": "<user email>", "message": "Password updated"}
        - 403 if token is invalid
    """
    email = request.form.get('email')
    reset_token = request.form.get('reset_token')
    password = request.form.get('new_password')
    try:
        AUTH.update_password(reset_token, password)
        return jsonify(email=email, message="Password updated"), 200
    except Exception:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)