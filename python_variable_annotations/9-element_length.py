#!/usr/bin/env python3
"""
This module provides a function to compute the length of each element
in an iterable of sequences.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(
    lst: Iterable[Sequence]
) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples containing each sequence and its length from
    the given iterable.

    Parameters:
        lst (Iterable[Sequence]): An iterable containing sequence elements
            (e.g., strings, lists, tuples).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples, each containing a
            sequence from `lst` and its length.
    """
    return [(i, len(i)) for i in lst]
