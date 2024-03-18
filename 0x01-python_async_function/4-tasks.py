#!/usr/bin/env python3

"""
Tasks module

This module contains a function `task_wait_n` that spawns `task_wait_random` coroutine `n` times
with the specified max_delay and returns the list of all the delays.
"""

import asyncio
from typing import List, Task

task_wait_random = __import__('3-tasks').task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that spawns `task_wait_random` coroutine `n` times
    with the specified max_delay and returns the list of all the delays.

    Args:
        n (int): Number of times to spawn the coroutine.
        max_delay (int): Maximum delay in seconds for each coroutine.

    Returns:
        List[float]: List of all the delays in ascending order.

    Example:
        >>> import asyncio
        >>> from 4-tasks import task_wait_n
        >>> print(asyncio.run(task_wait_n(5, 6)))
        [0.2261658205652346, 1.1942770588220557, 1.8410422186086628, 2.1457353803430523, 4.002505454641153]
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return await asyncio.gather(*tasks)

# Testing the coroutine
if __name__ == "__main__":
    import asyncio

    n = 5
    max_delay = 6
    print(asyncio.run(task_wait_n(n, max_delay)))

