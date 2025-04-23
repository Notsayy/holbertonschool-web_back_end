#!/usr/bin/env python3
"""
This module provides a function to create an asyncio.Task
for the wait_random coroutine with a given maximum delay.
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Returns an asyncio.Task for the wait_random coroutine
    with the specified max_delay.

    Args:
        max_delay (int): The maximum delay for wait_random.

    Returns:
        asyncio.Task: The created asyncio Task.
    """
    return asyncio.create_task(wait_random(max_delay))
