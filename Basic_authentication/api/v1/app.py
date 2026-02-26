#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request, Response
from flask_cors import (CORS, cross_origin)
from typing import Tuple
import os


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

auth = None
if getenv('AUTH_TYPE') == 'auth':
    from api.v1.auth.auth import Auth
    auth = Auth()


@app.before_request
def before_request() -> None:
    """Filter each request before it is handled by a route."""
    if auth is None:
        return
    excluded = ['/api/v1/status/', '/api/v1/unauthorized/', '/api/v1/forbidden/']
    if not auth.require_auth(request.path, excluded):
        return
    if auth.authorization_header(request) is None:
        abort(401)
    if auth.current_user(request) is None:
        abort(403)


@app.errorhandler(404)
def not_found(error) -> Tuple[Response, int]:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error) -> Tuple[Response, int]:
    """ Unauthorized handler
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> Tuple[Response, int]:
    """ Forbidden handler
    """
    return jsonify({"error": "Forbidden"}), 403


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = int(getenv("API_PORT", "5000"))
    app.run(host=host, port=port)
