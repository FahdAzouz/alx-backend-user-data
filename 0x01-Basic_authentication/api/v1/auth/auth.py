#!/usr/bin/env python3
"""auhtentication module"""

from flask import request
from typing import (
    List,
    TypeVar
)


class Auth:
    '''class handling authentication'''

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """returns False """
        return False

    def authorization_header(self, request=None) -> str:
        """handles the header"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """returns the current user"""
        return None
