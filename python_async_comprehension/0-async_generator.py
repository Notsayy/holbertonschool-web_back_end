#!/usr/bin/env python3

"""
This module contains an asynchronous generator function that yields
10 random floating-point numbers between 0 and 10, waiting 1 second
asynchronously between each yield.
"""

import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous generator that yields 10 random floats.

    Each time, it waits asynchronously for 1 second,
    then yields a random floating-point number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
