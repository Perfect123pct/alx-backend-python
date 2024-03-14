#!/usr/bin/env python3

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a function that multiplies a float by a given multiplier.

    Args:
        multiplier (float): The multiplier value.

    Returns:
        Callable[[float], float]: A function that takes a float as input
        and returns the result of multiplying it by the multiplier.
    """
    def multiplier_function(number: float) -> float:
        return number * multiplier

    return multiplier_function

if __name__ == "__main__":
    make_multiplier.__annotations__
    fun = make_multiplier(2.22)
    print("{}".format(fun(2.22)))

