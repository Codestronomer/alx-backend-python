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
    delay_list = await asyncio.gather(*(wait_random(
        max_delay - 1
        ) for _ in range(n)))
    return list(delay_list)
