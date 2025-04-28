#!/usr/bin/env python3

"""
This module provides an asynchronous comprehension function that collects
10 random floating-point numbers generated asynchronously.
"""

import asyncio
import random
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random floats from an asynchronous generator into a list.

    Asynchronously iterates over the async_generator, appending each yielded
    random float to a list, and returns the list after all values are collected

    Returns:
        List[float]: A list containing 10 random floating-point
        numbers between 0 and 10.
    """
    random_numbers = []
    async for i in async_generator():
        random_numbers.append(i)
    return random_numbers
