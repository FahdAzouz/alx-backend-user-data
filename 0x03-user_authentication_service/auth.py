#!/usr/bin/env python3
"""authentification module"""
from bcrypt import hashpw
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid
from typing import Union


def _hash_password(password: str) -> bytes:
    '''
    returns a salted hash of the input password,
    hashed with bcrypt.hashpw.
    '''
    hashed = hashpw(password.encode("utf-8"), bcrypt.gensalt())
    return hashed


def _generate_uuid() -> str:
    '''return string representation of uuid'''
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """Initializes a new Auth instance.
        """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Adds a new user to the database.
        """
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))
        raise ValueError("User {} already exists".format(email))

    def valid_login(self, email: str, password: str) -> bool:
        """validate the login"""
        user = None
        try:
            user = self._db.find_user_by(email=email)
            if user is not None:
                return bcrypt.checkpw(
                    password.encode("utf-8"),
                    user.hashed_password,
                )
        except NoResultFound:
            return False
        return False

    def create_session(self, email: str) -> str:
        """
        method find the user corresponding to the email,
        generate a new UUID and store it in the database
        as the user’s session_id, then return the session ID.
        """
        try:
            user = self._db.find_user_by(email=email)
            if user is not None:
                id = _generate_uuid()
                self._db.update_user(user.id, session_id=id)
                return id
        except NoResultFound:
            return None
        return None

    def get_user_from_session_id(self, session_id: str) -> Union[User, None]:
        '''Retrieves a user based on a given session ID.
        '''
        user = None
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None
        return user

    def destroy_session(self, user_id: int) -> None:
        '''destroys session'''
        if user_id is None:
            return None
        self._db.update_user(user_id, session_id=None)
