#!/usr/bin/env python3

"""
Async Comprehension Module
This module defines a coroutine called async_comprehension that collects 10 random numbers using async comprehensions.
"""

import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator

async def async_comprehension() -> List[float]:
    """
    Async Comprehension Coroutine
    Collects 10 random numbers using async comprehensions.
    Returns:
        List[float]: List of 10 random numbers.
    """
    return [i async for i in async_generator()]

# For testing
async def main():
    print(await async_comprehension())

if __name__ == "__main__":
    asyncio.run(main())

