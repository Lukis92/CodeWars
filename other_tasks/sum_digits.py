# https://edube.org/learn/pe-2/lab-the-digit-of-life-3
def sum_digits(number: int) -> int:
    """
    Repeatedly sum the digits of a number until the sum is a single digit.

    Args:
        number (int): The number to sum the digits of.

    Returns:
        int: The resulting single-digit sum.
    """
    result = number

    while result >= 10:
        result = sum(int(digit) for digit in str(result))

    return result

print(sum_digits(19991229))
print(sum_digits(20000101))