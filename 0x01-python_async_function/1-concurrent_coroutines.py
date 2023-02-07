#!/usr/bin/env python3
"""
Module imports wait_random coroutines
and performs a couple of operations on it
"""


import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    runs wait_random a number of times specified with the specified
    of delay

    args:
        n (int): number of times wait_random is called
        max_delay (int): args for wait_random

    return:
        (List): A list of floats returned by every call to wait_random
    """
    delay_tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await task for task in asyncio.as_completed(delay_tasks)]
