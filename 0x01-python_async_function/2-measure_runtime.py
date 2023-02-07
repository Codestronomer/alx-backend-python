#!/usr/bin/env python3
"""
Module measure runtime for the wait_n function
"""
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n and returns the
    total time divided by arg n

    Args:
        n (int): number of times wait_random is called
        max_delay (int, optional): maximum amount of delay required for max n

    Return: (float) total_time/n
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elasped_time = time.perf_counter() - start
    return elasped_time / n
