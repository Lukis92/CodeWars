"""Utility functions for operations on collections."""

from collections import Counter
from typing import Sequence


def common(a: Sequence[int], b: Sequence[int], c: Sequence[int]) -> int:
    """Return the sum of elements present in all three sequences.

    Each element is counted as many times as it appears in all three
    sequences. For example, if ``2`` appears twice in each sequence,
    ``2`` will contribute ``4`` to the final sum.

    Args:
        a: First sequence of integers.
        b: Second sequence of integers.
        c: Third sequence of integers.

    Returns:
        The sum of common elements among ``a``, ``b`` and ``c``.
    """

    total = 0
    b_counts, c_counts = Counter(b), Counter(c)

    for value in a:
        if b_counts[value] > 0 and c_counts[value] > 0:
            total += value
            b_counts[value] -= 1
            c_counts[value] -= 1

    return total
