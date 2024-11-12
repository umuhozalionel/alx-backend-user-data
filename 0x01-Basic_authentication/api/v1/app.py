#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from flask import Flask, jsonify
from flask_cors import CORS
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler """
    response = jsonify({"error": "Not found"})
    response.status_code = 404
    response.headers["Connection"] = "close"
    return response

@app.errorhandler(401)
def unauthorized(error) -> str:
    """ Unauthorized handler """
    response = jsonify({"error": "Unauthorized"})
    response.status_code = 401
    response.headers["Content-Length"] = str(len(response.get_data(as_text=True)))
    response.headers["Connection"] = "close"
    return response

@app.errorhandler(403)
def forbidden(error) -> str:
    """ Forbidden handler """
    response = jsonify({"error": "Forbidden"})
    response.status_code = 403
    response.headers["Content-Length"] = str(len(response.get_data(as_text=True)))
    response.headers["Connection"] = "close"
    return response

if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port, threaded=False, use_reloader=False)  # This forces HTTP/1.0 behavior
