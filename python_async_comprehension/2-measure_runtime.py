#!/usr/bin/env python3

"""
This module measures the total runtime of executing async_comprehension
four times in parallel using asyncio.gather.
"""

import asyncio
import time
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Executes async_comprehension four times
    in parallel and measures total runtime.

    Uses asyncio.gather to run multiple coroutines concurrently and calculates
    execution time using the event loop's internal clock for precision.

    Returns:
        float: Total runtime in seconds (approximately 10 seconds)
    """
    start_time = asyncio.get_event_loop().time()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    end_time = asyncio.get_event_loop().time()
    return end_time - start_time
