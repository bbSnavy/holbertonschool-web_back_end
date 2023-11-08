#!/usr/bin/env python3
""" tasks """
import asyncio
import typing

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> typing.List[float]:
    """ task_wait_n """
    return [
        await result
        for result
        in asyncio.as_completed([
            task_wait_random(max_delay)
            for _
            in range(n)
        ])
    ]
