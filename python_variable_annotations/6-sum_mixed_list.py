#!/usr/bin/env python3
""" python """
import typing


def sum_mixed_list(input_list: typing.List[typing.Union[int, float]]) -> float:
    """ sum_mixed_list """
    result = 0.0
    for v in input_list:
        result += v
    return result
