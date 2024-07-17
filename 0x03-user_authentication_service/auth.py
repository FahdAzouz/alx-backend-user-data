#!/usr/bin/env python3
"""authentification module"""
from typing import Bytes
from bcrypt import hashpw
import bcrypt


def _hash_password(password: str) -> Bytes:
    '''returns a salted hash of the input password, hashed with bcrypt.hashpw.'''
    hashed = hashpw(password.encode("utf-8"), bcrypt.gensalt())
    return hashed
