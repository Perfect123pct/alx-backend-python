#!/usr/bin/env python3

"""
Async IO Basics module

This module contains an asynchronous coroutine `wait_random`
that waits for a random delay between 0 and max_delay seconds
and eventually returns it.
"""

import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay
    between 0 and max_delay seconds (inclusive) and returns it.

    Args:
        max_delay (int): Maximum delay in seconds (default 10).

    Returns:
        float: Random delay between 0 and max_delay seconds.

    Example:
        >>> import asyncio
        >>> from 0-basic_async_syntax import wait_random
        >>> asyncio.run(wait_random())
        9.034261504534394
        >>> asyncio.run(wait_random(5))
        1.6216525464615306
        >>> asyncio.run(wait_random(15))
        10.634589756751769
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

# Testing the coroutine
if __name__ == "__main__":
    print(asyncio.run(wait_random()))
    print(asyncio.run(wait_random(5)))
    print(asyncio.run(wait_random(15)))

