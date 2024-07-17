#!/usr/bin/env python3
"""authentification module"""
from bcrypt import hashpw
import bcrypt


def _hash_password(password: str) -> bytes:
    '''
    returns a salted hash of the input password,
    hashed with bcrypt.hashpw.
    '''
    hashed = hashpw(password.encode("utf-8"), bcrypt.gensalt())
    return hashed
