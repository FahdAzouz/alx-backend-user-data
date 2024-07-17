#!/usr/bin/env python3
"""authentification module"""
from bcrypt import hashpw
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    '''
    returns a salted hash of the input password,
    hashed with bcrypt.hashpw.
    '''
    hashed = hashpw(password.encode("utf-8"), bcrypt.gensalt())
    return hashed


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """register a user in the database"""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return self._db.add_user(email, self._hash_password(password))
        raise ValueError("User {} already exists".format(email))
