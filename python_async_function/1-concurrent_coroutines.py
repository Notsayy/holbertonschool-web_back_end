#!/usr/bin/env python3
"""
Module for running multiple asynchronous wait_random coroutines and
returning their results in order of completion.
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random coroutines concurrently and collect their results
    in order of completion.

    Args:
        n (int): Number of times to run wait_random.
        max_delay (int): Maximum delay for each wait_random call.

    Returns:
    List[float]: List of delays, sorted in ascending order by
    completion time.
    """
    async_tasks = [wait_random(max_delay) for _ in range(n)]
    delays = []
    for completed in asyncio.as_completed(async_tasks):
        delay = await completed
        delays.append(delay)
    return delays
