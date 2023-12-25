# https://www.codewars.com/kata/63b84f54693cb10065687ae5/train/python
def create_box(m, n):
    matrix = [[0 for _ in range(m)] for _ in range(n)]
 
    for i in range(n):
        for j in range(m):
            distance_to_edge = 1 + min(i, n - 1 - i, j, m - 1 - j)
            matrix[i][j] = distance_to_edge

    return matrix
print(create_box(3, 3))