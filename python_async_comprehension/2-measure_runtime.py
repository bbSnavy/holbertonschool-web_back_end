#!/usr/bin/env python3
""" measure runtime """
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ measure runtime """
    s = time.time()
    fn = async_comprehension
    l = [fn() for _ in range(4)]
    await asyncio.gather(*l)
    e = time.time()
    return e - s
