#!/usr/bin/python3
"""
Test  - Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """Rotate the list of given numbers
    """
    n = len(matrix)  # define the matrix store this value in a variable

    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i] = matrix[i][::-1]
