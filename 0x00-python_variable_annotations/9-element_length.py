#!/usr/bin/env python3

from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculate the length of each element in an iterable.

    Args:
        lst (Iterable[Sequence]): The iterable object containing sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples containing the original sequences
        and their respective lengths.
    """
    return [(i, len(i)) for i in lst]

if __name__ == "__main__":
    print(element_length.__annotations__)

