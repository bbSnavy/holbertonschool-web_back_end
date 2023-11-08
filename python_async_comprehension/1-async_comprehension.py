#!/usr/bin/env python3
""" async comprehension """
import typing

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
    """ async comprehension """
    result = []

    async for v in async_generator:
        result.append(v)

    return result
