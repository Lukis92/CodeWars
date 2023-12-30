# https://www.codewars.com/kata/57fb0f3f9610ced69000023c/train/python
def remove(inp):
    while True:
        new_s = ""
        i = 0

        while i < len(inp):
            # Find the next different character
            j = i + 1
            while j < len(inp) and inp[j] == inp[i]:
                j += 1

            # Add the sequence if its length is even or it's a single character
            if (j - i) % 2 == 0 or j - i == 1:
                new_s += inp[i:j]

            i = j

        # Break the loop if no changes were made
        if new_s == inp:
            break

        inp = new_s

    return inp
