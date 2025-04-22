#!/usr/bin/env python3
"""
This module provides a function to create a tuple and the square of a number.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple containing a string and the square of a number as a float.

    Parameters:
        k (str): The string to include in the tuple.
        v (Union[int, float]): The number to be squared.

    Returns:
        A tuple where the first element is `k` and the square of `v`
    """
    return (k, float(v ** 2))
