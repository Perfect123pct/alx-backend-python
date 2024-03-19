#!/usr/bin/env python3

"""
Measure Runtime Module
This module defines a coroutine called measure_runtime that executes async_comprehension four times in parallel using asyncio.gather and measures the total runtime.
"""

import asyncio
from time import perf_counter
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    """
    Measure Runtime Coroutine
    Executes async_comprehension four times in parallel using asyncio.gather and measures the total runtime.
    Returns:
        float: Total runtime in seconds.
    """
    start_time = perf_counter()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    end_time = perf_counter()
    return end_time - start_time

# For testing
async def main():
    return await measure_runtime()

if __name__ == "__main__":
    print(asyncio.run(main()))

