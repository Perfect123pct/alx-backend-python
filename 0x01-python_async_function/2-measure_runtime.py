#!/usr/bin/env python3

"""
Measure Runtime module

This module contains a function `measure_time` that measures the total execution
time for the `wait_n` coroutine and returns the average time per iteration.
"""

import asyncio
import time
from typing import Callable

wait_n = __import__('1-concurrent_coroutines').wait_n

def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for the wait_n coroutine and returns
    the average time per iteration.

    Args:
        n (int): Number of times to spawn the coroutine.
        max_delay (int): Maximum delay in seconds for each coroutine.

    Returns:
        float: Average time per iteration.

    Example:
        >>> measure_time(5, 9)
        1.759705400466919
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n

# Testing the function
if __name__ == "__main__":
    n = 5
    max_delay = 9
    print(measure_time(n, max_delay))

