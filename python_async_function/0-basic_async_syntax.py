#!/usr/bin/env python3
""" wait_random """
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ wait_random """
    v = random.uniform(0.0, float(max_delay))

    await asyncio.sleep(v)

    return v
