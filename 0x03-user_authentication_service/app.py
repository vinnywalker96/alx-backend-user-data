#!/usr/bin/env python3
"""Basic flask app"""
from flask import (
        Flask,
        jsonify,
        request,
        abort
        )
from sqlalchemy.orm.exc import NoResultFound
from auth import Auth
from db import DB

app = Flask(__name__)
AUTH = Auth()
Db = DB()


@app.route("/")
def home():
    """Basic flask app"""
    return jsonify({"message": "Bienvenue"})


@app.route("/users/", methods=["POST"], strict_slashes=False)
def register_user():
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        user = AUTH.register_user(email, password)
    except ValueError:
        return jsonify(
                {"message": "email already registered"}
                ), 400
    return jsonify({"email": f"{email}", "message": "user created"})


@app.route("/sessions/", methods=["POST"], strict_slashes=False)
def login():
    """Authenticate User"""
    email = request.form.get("email")
    password = request.form.get("password")
    user_login = AUTH.valid_login(email, password)
    if not user_login:
        abort(401)
        session = AUTH.create_session(email)
        DB.commit()
    return jsonify({"email": email,"message": "logged in"})
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
