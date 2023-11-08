#!/usr/bin/env python3
""" wait_n """
import asyncio
import typing

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    return [
        await result
        for result
        in asyncio.as_completed([
            asyncio.create_task(wait_random(max_delay))
            for _
            in range(n)
        ])
    ]
