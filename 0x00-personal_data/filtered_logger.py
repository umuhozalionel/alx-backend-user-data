#!/usr/bin/env python3
"""
Module for filtering sensitive data in log messages
"""

import re
from typing import List


def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """
    Obfuscates log messages by replacing values of specified fields with
    a redaction string.

    Args:
        fields (List[str]): List of strings representing all fields to
        obfuscate.
        redaction (str): String representing by what the field will be
        obfuscated.
        message (str): String representing the log line.
        separator (str): String representing by which character is separating
        all fields in the log line.

    Returns:
        str: Obfuscated log message.
    """
    for field in fields:
        message = re.sub(
            f"{field}=[^{separator}]*",
            f"{field}={redaction}",
            message
        )
    return message
