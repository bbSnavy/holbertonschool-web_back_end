#!/usr/bin/env python3
import asyncio
import random
""" python """


async def wait_random(max_delay: int = 10):
    """ wait_random """
    v = random.uniform(0.0, float(max_delay))

    await asyncio.sleep(v)

    return v
