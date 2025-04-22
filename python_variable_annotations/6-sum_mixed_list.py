#!/usr/bin/env python3
"""
This module provides a function to calculate the sum of the list
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculates the sum of all elements in a list containing integers and floats

    Parameters:
        mxd_lst (List[Union[int, float]]): The list of numbers

    Returns:
        float: The total sum of the elements in `mxd_lst`.
    """
    return sum(mxd_lst)
