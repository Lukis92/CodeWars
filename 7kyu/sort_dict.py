"""Helpers for working with dictionaries."""

from typing import Dict, List, Tuple


def sort_dict(d: Dict) -> List[Tuple]:
    """Return dictionary items sorted by value in descending order.

    Args:
        d: Dictionary whose items should be sorted.

    Returns:
        A list of ``(key, value)`` tuples sorted by ``value`` from highest to
        lowest.
    """

    return sorted(d.items(), key=lambda item: item[1], reverse=True)
