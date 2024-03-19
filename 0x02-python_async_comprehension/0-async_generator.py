#!/usr/bin/env python3

"""
Async Generator Module
This module defines a coroutine called async_generator that generates random numbers asynchronously.
"""

import asyncio
import random
from typing import AsyncGenerator

async def async_generator() -> AsyncGenerator[float, None]:
    """
    Async Generator Coroutine
    Generates random numbers asynchronously.
    Yields:
        float: Random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

# For testing
async def print_yielded_values():
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)

if __name__ == "__main__":
    asyncio.run(print_yielded_values())

