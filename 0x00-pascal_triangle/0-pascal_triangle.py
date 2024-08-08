#!/usr/bin/python3
"""
The script to Pascal's Triangle.
"""

'''Pascal's Triangle - Returns a lists of integers.
n will be always an integer.
Returns an empty list if n = 0.'''


def pascal_triangle(n):
    triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            row.append(Xfactorial(i) // (Xfactorial(j) * Xfactorial(i - j)))
        triangle.append(row)
    return triangle


"""
Factural is a multiplication operation of natural numbers.
n! = n * (n - 1) * (n - 2)
"""


def Xfactorial(n):
    result = 1
    """ Multiply all numbers from 1 to n"""
    for i in range(2, n + 1):
        result *= i
    return result
