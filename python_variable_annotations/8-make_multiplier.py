#!/usr/bin/env python3
"""
This module provides a function to create a multiplier function
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies its input by a specified multiplier.

    Parameters:
        multiplier (float): The value to multiply by.

    Returns:
        A function that takes a float and returns input x multiplier
    """
    def multiplier_function(x: float) -> float:
        return x * multiplier
    return multiplier_function
