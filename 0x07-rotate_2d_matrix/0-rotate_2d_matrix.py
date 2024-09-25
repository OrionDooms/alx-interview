#!/usr/bin/python3
"""Rotate 2D Matrix"""
def reverse_Matrix(matrix):
    """Reversing the matrix"""
    for i in range(len(matrix)):
        matrix[i].reverse()

def rotate_2d_matrix(matrix):
    """Convert rows to columns by swapping the matrix[i][j] with matrix[j][i]"""
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            """Swapping matrix[i][j] and [j][i] """
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    reverse_Matrix(matrix)
