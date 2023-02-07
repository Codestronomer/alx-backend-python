#!/usr/bin/env python3
"""
Module measure runtime for the wait_n function
"""


import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int = 10) -> float:
    """
    Measures the total execution time for wait_n and returns the
    total time divided by arg n

    Args:
        n (int): number of times wait_random is called
        max_delay (int, optional): maximum amount of delay required for max n

    Return: (float) total_time/n
    """
    s = time.perf_counter()
    await wait_n(n, max_delay)
    total_time = time.perf_counter() - s
    return total_time/n
