#!/usr/bin/env python3
""" python """
import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """ make_multiplier """
    return (lambda v: v * multiplier)
