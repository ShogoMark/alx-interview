#!/usr/bin/python3

def rotate_2d_matrix(matrix):
    n = len(matrix)

    rotated_matrix = [[0] * n for _ in range(n)]

    for i in range(n):
        rotated_matrix[i][0] = matrix[n - 1][i]
        rotated_matrix[i][1] = matrix[n - 2][i]
        rotated_matrix[i][2] = matrix[n - 3][i]

    for i in range(n):
        for j in range(n):
            matrix[i][j] = rotated_matrix[i][j]
