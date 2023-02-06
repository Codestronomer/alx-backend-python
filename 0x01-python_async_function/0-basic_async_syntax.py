#!/usr/bin/env python3
# 0-basic_async_syntax.py


"""
module contains an asynchronous coroutine that takes in an
integer argument max_delay that waits for a random
delay between 0 and max_delay seconds and returns it.
"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> int:
    """
    Coroutine takes an argument and returns a random number
    in the range of the argument
    Args: max_delay (int)
    Return: int
    """
    delay = random.uniform(0, max_delay)
    asyncio.sleep(delay)
    return delay
