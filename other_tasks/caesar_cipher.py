# https://edube.org/learn/pe-2/lab-improving-the-caesar-cipher-3

def caesar_cipher(text: str, numerical_shift: int) -> str:
    """
    Encode the message using Caesar cipher.

    Returns:
        str: Encoded message.

    Raises:
        ValueError: If the shift value is not in the 1-25 range.
    """
    if numerical_shift < 1 or numerical_shift > 25:
        raise ValueError("A shift value is not between 1-25 range.")
    cipher = ''
    upper_a, upper_z, lower_a, lower_z = ord('A'), ord('Z'), ord('a'), ord('z')

    for char in text:
        if char.isalpha():
            code = ord(char) + numerical_shift
            if code > upper_z and char.isupper():
                code = upper_a + code-upper_z-1
            elif code > lower_z and char.islower():
                code = lower_a + code-lower_z-1
            cipher += chr(code)
        else:
            cipher += char

    return cipher

print(caesar_cipher("abcxyzABCxyz", 123))