# https://www.codewars.com/kata/564871e795df155582000013/train/python
def fill_gaps(timesheet):
    n = len(timesheet)
    arr = timesheet[:]
    i = 0

    while i < n:
        if arr[i] is None and i != 0:
            start = i
            # Find the end of the None sequence
            while i < n and arr[i] is None:
                i += 1

            # check if we are not at the end and if surrounding values are the same
            if i < n and arr[start-1] == arr[i]:
                for j in range(start, i):
                    arr[j] = arr[start - 1]
        else:
            i += 1
    return arr


print(fill_gaps([1,None,1]))#, [1,1,1], "Replace None values surrounded by matching values")
# print(fill_gaps([1,None,None,None,1]))#, [1,1,1,1,1], "There may be multiple Nones")
# print(fill_gaps([1,None,1,2,None,2]))#, [1,1,1,2,2,2], "There may be multiple replacements required")
# print(fill_gaps([1,None,2,None,2,None,1]))#, [1,None,2,2,2,None,1], "No nesting.")
# print(fill_gaps([1,None,2]))#, [1,None,2], "No replacement if ends don't match")
# print(fill_gaps([None,1,None]))#, [None,1,None], "No replacement if ends don't match off the ends of the array")
# print(fill_gaps(['codewars', None, None, 'codewars', 'real work', None, None, 'real work']))#, ["codewars", "codewars", "codewars", "codewars", "real work", "real work", "real work", "real work"], "Works with strings too")

