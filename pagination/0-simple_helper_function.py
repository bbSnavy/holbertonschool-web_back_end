#!/usr/bin/env python3
""" simple helper function """
import typing


def index_range(page: int, page_size: int) -> typing.Tuple[int]:
    """ index range """
    return ((page - 1) * page_size, page * page_size)
