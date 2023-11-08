#!/usr/bin/env python3
""" measure runtime """
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ measure runtime """
    s = time.time()
    fn = async_comprehension
    await asyncio.gather(fn(), fn(), fn(), fn())
    e = time.time()
    return e - s
