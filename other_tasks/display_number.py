# https://edube.org/learn/pe-2/lab-a-led-display-3
class DigitPatterns:
    """
    Class to store and manage digit patterns.
    """
    patterns = {
    '0': ('###', '# #', '# #', '# #', '###'),
    '1': ('  #', '  #', '  #', '  #', '  #'),
    '2': ('###', '  #', '###', '#  ', '###'),
    '3': ('###', '  #', '###', '  #', '###'),
    '4': ('# #', '# #', '###', '  #', '  #'),
    '5': ('###', '#  ', '###', '  #', '###'),
    '6': ('###', '#  ', '###', '# #', '###'),
    '7': ('###', '  #', '  #', '  #', '  #'),
    '8': ('###', '# #', '###', '# #', '###'),
    '9': ('###', '# #', '###', '  #', '###'),
    '.': ('   ', '   ', '   ', '   ', '  #'),
    }

    @classmethod
    def get_pattern(cls, digit):
        """
        Returns the pattern for the given digit.
        """
        return cls.patterns.get(digit, ('?', '?', '?', '?', '?'))


def display_number(number: int) -> None:
    """
    Displays the number in a large digit pattern.
    """
    digits = [DigitPatterns.get_pattern(digit) for digit in str(number)]

    for i in range(5):
        line = " ".join([segment[i] for segment in digits])
        print(line)

display_number(16)