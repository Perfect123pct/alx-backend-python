#!/usr/bin/env python3
"""
Module for computing the floor of a float.
"""

import math


def floor(n: float) -> int:
    """
    Return the floor of the given float.

    Args:
        n (float): The input float.

    Returns:
        int: The floor of the input float.
    """
    return math.floor(n)


if __name__ == "__main__":
    import math

    ans = floor(3.14)

    print(ans == math.floor(3.14))
    print(floor.__annotations__)
    print("floor(3.14) returns {}, which is a {}".format(ans, type(ans)))

