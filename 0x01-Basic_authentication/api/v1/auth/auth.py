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
        if path is None:
            return True
        elif excluded_paths is None or excluded_paths == []:
            return True
        elif path in excluded_paths:
            return False
        else:
            for i in excluded_paths:
                if i.startswith(path):
                    return False
                if path.startswith(i):
                    return False
                if i[-1] == "*":
                    if path.startswith(i[:-1]):
                        return False
        return True

    def authorization_header(self, request=None) -> str:
        """handles the header"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """returns the current user"""
        return None
