#!/usr/bin/env python3

"""
Task Wait Random module

This module contains a function `task_wait_random` that creates and returns
an asyncio.Task for the `wait_random` coroutine with the specified max_delay.
"""

import asyncio
from typing import Task

wait_random = __import__('0-basic_async_syntax').wait_random

def task_wait_random(max_delay: int) -> Task[float]:
    """
    Create and return an asyncio.Task for the wait_random coroutine
    with the specified max_delay.

    Args:
        max_delay (int): Maximum delay in seconds.

    Returns:
        Task[float]: asyncio.Task object representing the execution
                     of the wait_random coroutine.

    Example:
        >>> task = task_wait_random(5)
        >>> isinstance(task, asyncio.Task)
        True
    """
    return asyncio.create_task(wait_random(max_delay))

# Testing the function
if __name__ == "__main__":
    import asyncio

    async def test(max_delay: int) -> float:
        task = task_wait_random(max_delay)
        await task
        print(task.__class__)

    asyncio.run(test(5))

