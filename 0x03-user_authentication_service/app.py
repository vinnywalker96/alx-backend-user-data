#!/usr/bin/env python3
"""Basic flask app"""
from flask import (
        Flask,
        jsonify,
        request
        )
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
