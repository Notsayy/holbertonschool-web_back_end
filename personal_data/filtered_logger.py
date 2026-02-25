#!/usr/bin/env python3
"""This module provides a function to filter information from log messages.
"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Obfuscate the values of specified fields in a log message.

    Args:
        fields: List of field names whose values should be obfuscated.
        redaction: String to replace the field values with.
        message: The log message containing the fields.
        separator: The character separating fields in the message.

    Returns:
        The log message with specified fields obfuscated.
    """
    return re.sub(
        r'(' + '|'.join(fields) + r')=[^' + separator + r']*',
        r'\1=' + redaction, message
    )
