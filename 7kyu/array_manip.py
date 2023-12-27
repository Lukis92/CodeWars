# https://www.codewars.com/kata/58d5e6c114286c8594000027/train/python
def array_manip(array):
    result = []
    for i, _ in enumerate(array):
        least_greater = float('inf')
        for j in range(i+1, len(array)):
            if array[j] > array[i] and array[j] < least_greater:
                least_greater = array[j]
        result.append(least_greater if least_greater != float('inf') else -1)

    return result

print(array_manip([8, 58, 71, 18, 31, 32, 63, 92, 43, 3, 91, 93, 25, 80, 28]))#, [18, 63, 80, 25, 32, 43, 80, 93, 80, 25, 93, -1, 28, -1, -1])
print(array_manip([ 2, 4, 18, 16, 7, 3, 9, 13, 18, 10 ]))#, [3, 7, -1, 18, 9, 9, 10, 18, -1, -1])
#[18, 58, 71, 8, 31, 32, 63, 92, 43, 3, 91, 93, 25, 80, 28]
#[18, 63, 71, 8, 31, 32, 58, 92, 43, 3, 91, 93, 25, 80, 28]
#