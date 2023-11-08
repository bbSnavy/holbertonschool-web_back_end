#!/usr/bin/env python3
""" async generator """
import asyncio
import random
import typing


async def async_generator() -> typing.Generator[float, None, None]:
    """ async generator """
    for _ in range(10):
        await asyncio.sleep(1)

        value = random.randint(0, 10)

        yield value
