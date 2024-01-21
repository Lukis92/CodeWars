# https://edube.org/learn/pe-2/lab-find-a-word-3
def find_a_word(str_1: str, str_2: str) -> bool:
    """
    Checks whether all characters from the first string are hidden
    inside the second string.

    Args:
    str_1 (str): The string containing the characters to find.
    str_2 (str): The string to search in.

    Returns:
    bool: True if all characters from the first string are present in the second string.
    """
    return set(str_1).issubset(str_2)

print(find_a_word("donor", "Nabucodonosor"))
print(find_a_word("donut", "Nabucodonosor"))