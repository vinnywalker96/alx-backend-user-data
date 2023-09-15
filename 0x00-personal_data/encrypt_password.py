#!/usr/bin/env python3
"""Encypting Password"""
import bcrypt


def hash_password(password: str) -> bytes:
    """hash_password

    Args:
        password:str
    Returns bytes password
    """
    passwd = bytes(password, 'utf-8')
    hashed = bcrypt.hashpw(passwd, bcrypt.gensalt())
    return hashed
