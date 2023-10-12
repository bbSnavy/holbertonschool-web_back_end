#!/usr/bin/env python3
""" python """
from typing import Iterable
from typing import Sequence
from typing import List
from typing import Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ element_length """
    return [(i, len(i)) for i in lst]
