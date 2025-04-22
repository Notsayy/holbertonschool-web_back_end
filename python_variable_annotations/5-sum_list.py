#!/usr/bin/env python3
"""
This module provides a function to calculate the sum of a list of numbers.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculates the sum of all elements in a list of floating-point numbers.

    Parameters:
        input_list (List[float]): The list of numbers to sum.

    Returns:
        float: The total sum of the elements in `input_list`.
    """
    return sum(input_list)
