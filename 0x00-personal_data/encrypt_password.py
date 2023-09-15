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


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Check if passwd is valid"""
    passwd = bytes(password, 'utf-8')
    if bcrypt.checkpw(passwd, hashed_password):
        return True
    return False
