#!/usr/bin/env python3

"""
Concurrent Coroutines module

This module contains an asynchronous coroutine `wait_n`
that spawns `wait_random` coroutine `n` times with the specified max_delay.
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that spawns `wait_random` coroutine `n` times
    with the specified max_delay and returns the list of all the delays.

    Args:
        n (int): Number of times to spawn the coroutine.
        max_delay (int): Maximum delay in seconds for each coroutine.

    Returns:
        List[float]: List of all the delays in ascending order.

    Example:
        >>> import asyncio
        >>> from 1-concurrent_coroutines import wait_n
        >>> print(asyncio.run(wait_n(5, 5)))
        [0.9693881173832269, 1.0264573845731002, 1.7992690129519855, 3.641373003434587, 4.500011569340617]
        >>> print(asyncio.run(wait_n(10, 7)))
        [0.07256214141415429, 1.518551245602588, 3.355762808432721, 3.7032593997182923, 3.7796178143655546, 4.744537840582318, 5.50781365463315, 5.758942587637626, 6.109707751654879, 6.831351588271327]
        >>> print(asyncio.run(wait_n(10, 0)))
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    """
    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return sorted(delays)

# Testing the coroutine
if __name__ == "__main__":
    import asyncio
    print(asyncio.run(wait_n(5, 5)))
    print(asyncio.run(wait_n(10, 7)))
    print(asyncio.run(wait_n(10, 0)))

