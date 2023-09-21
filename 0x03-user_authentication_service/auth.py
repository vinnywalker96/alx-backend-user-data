#!/usr/bin/env python3
"""Hash password"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """Hashed password

    Args:
        password: string to be hashed

    Returns:
        Hashed password
    """
    salt = bcrypt.gensalt()
    psswd = password.encode('utf-8')
    return bcrypt.hashpw(psswd, salt)
