#!/usr/bin/env python3
"""
This module provides a function to execute multiple task_wait_random
coroutines concurrently and return their results in completion order.
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Execute multiple task_wait_random coroutines concurrently and collect
    results in the order they complete.

    Args:
        n (int): Number of concurrent executions to spawn.
        max_delay (int): Maximum delay value for each task_wait_random call.

    Returns:
        List[float]: List of delay values sorted by completion order,
        which corresponds to ascending delay durations.
    """
    async_tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []
    for completed in asyncio.as_completed(async_tasks):
        delay = await completed
        delays.append(delay)
    return delays
