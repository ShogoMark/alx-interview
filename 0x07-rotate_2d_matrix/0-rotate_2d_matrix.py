#!/usr/bin/python3
""" Defines the rotate_2d_matrix function """


def rotate_2d_matrix(matrix):
    """ Rotates a 2D matrix 90 degrees clockwise """
    len_matrix = len(matrix)

    # Step 1: Transpose the matrix
    for i in range(len_matrix):
        for j in range(i, len_matrix):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for i in range(len_matrix):
        matrix[i].reverse()
