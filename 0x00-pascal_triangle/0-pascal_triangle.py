#!/usr/bin/python3
"""
The script to Pascal's Triangle.
"""


def pascal_triangle(n):
    """
    Pascal's Triangle - Returns a lists of integers.
    n will be always an integer.
    Returns an empty list if n = 0.
    """
    triangle = []
    if n <= 0:
        return triangle
    for i in range(n):

        """ start each row with 1s """
        row = [1] * (i + 1)

        """ Update the values in between """
        for j in range(1, i):
            tempA = triangle[i - 1][j - 1]
            tempB = triangle[i - 1][j]
            row[j] = tempA + tempB

        triangle.append(row)
    return triangle
