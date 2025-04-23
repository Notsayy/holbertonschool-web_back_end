#!/usr/bin/env python3
"""
This module measures the average runtime of the wait_n coroutine
executed n times with a given maximum delay.
"""

import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for running wait_n(n, max_delay),
    and returns the average time per run.

    Args:
        n (int): Number of times to run wait_n.
        max_delay (int): Maximum delay for each wait_random call.

    Returns:
        float: The average time per coroutine execution.
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()
    total_time = end - start
    return total_time / n
