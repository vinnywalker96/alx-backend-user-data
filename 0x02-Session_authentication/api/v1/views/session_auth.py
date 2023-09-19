#!/usr/bin/env python3
"""
handles all routes for the Session authentication
"""
from api.v1.views import app_views
from flask import jsonify
from models.user import user
from api.v1.app import auth
from api.v1.auth import 

@app_views.route('/auth_session/login', methods=[
    'POST'], strict_slashed=False)
def session_authentication():
    email, password = request.form.get()
    if email is None:
        return jsonify({ "error": "email missing" }), 400
    if password is None:
        return jsonify({ "error": "password missing" }), 400
    user = User.search({'email': email})
    if user is None:
        return jsonify({ "error": "no user found for this email" }), 404
    for u in users:
        if not u.is_valid_password(password):
            return jsonify({ "error": "wrong password" }), 401
    cookie = auth.session_cookie(request)
    user_id = auth.user_id_for_session_id(cookie)
    auth.create_session(user_id)
    user = User.get(user_id)
    return jsonify(user.to_json())
    



