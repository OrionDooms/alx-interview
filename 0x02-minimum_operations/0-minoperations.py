#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """Given a number n, this method calculates the number of operations
    needed to result in exactly number H characters in the file."""
    if n == 1:
        return 0
    x = n + 1
    for i in range(2, x):
        if n % i == 0:
            return i + minOperations(n // i)
    return 0
