#!/usr/bin/env python3
"""
filtered_logger module.

This module provides utilities for filtering and obfuscating sensitive
information (such as PII) from log messages using regular expressions.
"""

import re
import logging
from typing import List, Tuple


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


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Filters values in incoming log records using filter_datum """
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.getMessage(), self.SEPARATOR)
        return super().format(record)

PII_FIELDS: Tuple[str, ...] = ("name", "email", "phone", "ssn", "password")


def get_logger() -> logging.Logger:
    """Returns a logging.Logger configured for user data"""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(list(PII_FIELDS)))
    logger.addHandler(handler)
    return logger