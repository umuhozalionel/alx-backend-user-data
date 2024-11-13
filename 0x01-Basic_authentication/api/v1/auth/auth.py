# api/v1/auth/auth.py

from flask import request
from typing import List, TypeVar

class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        if path is None:
            return True
        if excluded_paths is None or not excluded_paths:
            return True
        
        if not path.endswith('/'):
            path += '/'

        excluded_paths = [p if p.endswith('/') else p + '/' for p in excluded_paths]

        if path in excluded_paths:
            return False

        return True

    def authorization_header(self, request=None) -> str:
        if request is None:
            return None
        if 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        return None
