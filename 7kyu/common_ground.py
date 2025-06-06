"""Find common words between two strings in the order they appear in the second."""

from typing import List


def common_ground(s1: str, s2: str) -> str:
    """Return unique common words from ``s2`` that also appear in ``s1``.

    If there are no common words, ``"death"`` is returned.

    Args:
        s1: First string of words.
        s2: Second string of words.

    Returns:
        A string containing words that are present in both inputs, ordered
        by their appearance in ``s2``. Duplicates are removed while
        preserving order.
    """

    words1 = set(s1.split())
    result: List[str] = []
    seen = set()

    for word in s2.split():
        if word in words1 and word not in seen:
            result.append(word)
            seen.add(word)

    return " ".join(result) if result else "death"
