#!/usr/bin/env python3
""" measure_runtime """
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines')


async def measure_time(n: int, max_delay: int) -> float:
    """ measure_time """
    s = time.time()

    await wait_n(n, max_delay)

    e = time.time()

    return e - s
