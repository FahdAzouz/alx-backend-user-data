#!/usr/bin/env python3
"""
Defines a hash_password function to return a hashed password
"""
import bcrypt
from bcrypt import hashpw


def hash_password(password: str) -> bytes:
    """
    Returns a hashed password
    Args:
        password (str): password to be hashed
    """
    b = password.encode()
    hashed = hashpw(b, bcrypt.gensalt())
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    '''
    Returns if password match the hash
    '''
    return bcrypt.checkpw(password.encode(), hashed_password)
