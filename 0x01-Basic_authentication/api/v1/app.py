# api/v1/app.py

from flask import Flask, request, abort
from flask_cors import CORS
from os import getenv

app = Flask(__name__)
CORS(app)

auth = None

# Based on the environment variable AUTH_TYPE, load the appropriate auth class
auth_type = getenv('AUTH_TYPE')

if auth_type == 'auth':
    from api.v1.auth.auth import Auth
    auth = Auth()

@app.before_request
def before_request():
    if auth is None:
        return
    if request.path not in ['/api/v1/status/', '/api/v1/unauthorized/', '/api/v1/forbidden/']:
        if not auth.require_auth(request.path, ['/api/v1/status/', '/api/v1/unauthorized/', '/api/v1/forbidden/']):
            return
        if auth.authorization_header(request) is None:
            abort(401, description="Unauthorized")
        if auth.current_user(request) is None:
            abort(403, description="Forbidden")

@app.route('/api/v1/status/', methods=['GET'])
def status():
    return {"status": "OK"}

@app.route('/api/v1/unauthorized/', methods=['GET'])
def unauthorized():
    abort(401, description="Unauthorized")

@app.route('/api/v1/forbidden/', methods=['GET'])
def forbidden():
    abort(403, description="Forbidden")

if __name__ == "__main__":
    app.run(host=getenv('API_HOST', '0.0.0.0'), port=int(getenv('API_PORT', 5000)))
