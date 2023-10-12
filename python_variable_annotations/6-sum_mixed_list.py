#!/usr/bin/env python3
""" python """


def sum_mixed_list(input_list: list[float | int]) -> float:
    """ sum_mixed_list """
    result = 0.0
    for v in input_list:
        result += v
    return result
