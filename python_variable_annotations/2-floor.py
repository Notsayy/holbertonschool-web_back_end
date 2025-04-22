#!/usr/bin/env python3

"""
This module provides a function to compute the floor of a floating-point number
"""

import math


def floor(n: float) -> int:
    """
    Returns the largest integer less than or equal to the floating-point number

    Parameters:
        n (float): The number to apply the floor function to.

    Returns:
        int: The floor of `n`.
    """
    return math.floor(n)
