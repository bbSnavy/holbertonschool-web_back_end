#!/usr/bin/env python3
""" simple pagination """
import csv
import math
import typing

from typing import List


def index_range(page: int, page_size: int) -> typing.Tuple[int]:
    """ index range """
    return ((page - 1) * page_size, page * page_size)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> typing.List[typing.List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ get page """
        assert type(page) is int
        assert type(page_size) is int
        assert page > 0
        assert page_size > 0

        data = self.dataset()
        page = index_range(page, page_size)
        if page[1] >= len(data):
            return []

        return data[page[0]: page[1]]
