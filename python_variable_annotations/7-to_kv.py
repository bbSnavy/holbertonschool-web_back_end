#!/usr/bin/env python3
""" python """
import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """ to_kv """
    return (k, v * v)
