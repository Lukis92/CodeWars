# https://edube.org/learn/pe-2/lab-anagrams-3
def anagram_check(text_1: str, text_2: str) -> str:
    """
    Check if provided texts are anagrames.

    Args:
        text_1 (str): First text.
        text_2 (str): Second text to compare.

    Returns:
        (str): 'Anagrams' if both texts are anagram of each other, otherwise 'Not anagrams'.
    """

    return "Anagrams" if sorted(text_1.lower()) == sorted(text_2.lower()) else "Not anagrams"

print(anagram_check("Listen", "Silent"))
print(anagram_check("modern", "norman"))