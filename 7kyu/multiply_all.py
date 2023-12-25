def multiply_all(arr):
    def inner(n):
        return [x * n for x in arr]
    return inner