#!/usr/bin/env python3

from typing import Tuple, List

def zoom_array(lst: Tuple[int], factor: int = 2) -> Tuple[int]:
    """
    Zoom in on an array by repeating each element a certain number of times.

    Args:
        lst (Tuple[int]): The input array.
        factor (int, optional): The zoom factor. Defaults to 2.

    Returns:
        Tuple[int]: The zoomed-in array.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return tuple(zoomed_in)


if __name__ == "__main__":
    array = (12, 72, 91)

    zoom_2x = zoom_array(array)

    zoom_3x = zoom_array(array, 3)

    print(zoom_array.__annotations__)

