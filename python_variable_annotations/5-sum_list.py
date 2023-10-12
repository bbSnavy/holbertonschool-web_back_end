#!/usr/bin/env python3
""" python """
import typing


def sum_list(input_list: typing.List[float]) -> float:
    """ sum_list """
    result = 0.0
    for v in input_list:
        result += v
    return result
