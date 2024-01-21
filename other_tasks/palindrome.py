# https://edube.org/learn/pe-2/lab-palindromes-4
def is_palindrome(text: str) -> bool:
    """
    Check if the passed text is a palindrome, ignoring spaces and
    case sensitivity.

    Args:
        text (str): Text to check if it's a palindrome.

    Returns:
        bool: True if it's a palindrome, otherwise False.
    """
    processed_text = text.replace(" ", "").upper()

    if processed_text == processed_text[::-1]:
        return "It's a palindrome"
    return "It's not a palindrome"

print(is_palindrome("Ten animals I slam in a net"))
print(is_palindrome("Eleven animals I slam in a net"))