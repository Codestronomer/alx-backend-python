#!/usr/bin/env python3
"""
Defines a coroutine async_generator
"""
import asyncio
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Yields a float every second

    Yields:
        Generator[float]: float
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
