# api/v1/auth/auth.py

from flask import request
from typing import List, TypeVar

class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Determine if authentication is required """
        return False

    def authorization_header(self, request=None) -> str:
        """ Get the authorization header from the request """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Get the current user """
        return None
