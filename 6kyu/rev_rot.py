# https://www.codewars.com/kata/56b5afb4ed1f6d5fb0000991/train/python
def rev_rot(strng, sz):
    if sz <= 0 or sz > len(strng) or not strng:
        return ""

    def process_chunk(chunk):
        sum_cubes = sum(int(digit)**3 for digit in chunk)
        return chunk[::-1] if sum_cubes % 2 == 0 else chunk[1:] + chunk[0]

    chunks = [strng[i:i+sz] for i in range(0, len(strng) - sz + 1, sz)]
    return ''.join(process_chunk(chunk) for chunk in chunks)

rev_rot("66443875", 4)


