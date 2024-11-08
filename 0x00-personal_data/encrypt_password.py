#!/usr/bin/env python3
"""
Module for hashing and validating passwords
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hashes a password using bcrypt.

    Args:
        password (str): The password to hash.

    Returns:
        bytes: The hashed password as a byte string.
    """
    # Generate a salt
    salt = bcrypt.gensalt()

    # Hash the password with the generated salt
    hashed_password = bcrypt.hashpw(password.encode(), salt)

    return hashed_password


def is_valid(
    hashed_password: bytes, password: str
) -> bool:
    """
    Validates that the provided password matches the hashed password.

    Args:
        hashed_password (bytes): The hashed password.
        password (str): The plain text password.

    Returns:
        bool: True if the password matches the hashed password,
        False otherwise.
    """
    return bcrypt.checkpw(
        password.encode(),
        hashed_password
    )
