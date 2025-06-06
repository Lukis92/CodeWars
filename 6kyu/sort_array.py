"""Sort only the odd numbers in a list while preserving even positions."""

from typing import List


def sort_array(source_array: List[int]) -> List[int]:
    """Return a list with odd numbers sorted in ascending order.

    The positions of even numbers remain unchanged.

    Args:
        source_array: List of integers containing both odd and even numbers.

    Returns:
        A new list where all odd numbers are sorted but even numbers are
        in their original positions.
    """

    odds = sorted([num for num in source_array if num % 2])
    odd_iter = iter(odds)
    return [next(odd_iter) if num % 2 else num for num in source_array]
