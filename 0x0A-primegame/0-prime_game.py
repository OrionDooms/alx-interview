#!/usr/bin/python3
"""Prime Game"""


def checkForPrime(n):
    """This function is to find the prime numbers, given number n and
    counting how many primes exist at each number"""
    if n < 2:
        return [0] * (n + 1)
    """prime_check is an array each index represents a if number is prime.
    All numbers are prime, set to True, except for 0 and 1, which are set to
    False"""
    prime_check = [True] * (n + 1)
    prime_check[0] = False
    prime_check[1] = False
    prime_count = [0] * (n + 1)
    a = 0

    for i in range(2, n + 1):
        if prime_check[i]:
            a += 1
            for j in range(i * i, n + 1, i):
                prime_check[j] = False
        prime_count[i] = a
    return prime_count


def isWinner(x, nums):
    """This function determines who wins between Maria and Ben."""
    if x > 0 and nums:
        max_n = max(nums)
        prime_count = checkForPrime(max_n)
        maria = 0
        ben = 0
        for n in nums:
            if prime_count[n] % 2 == 1:
                maria += 1
            else:
                ben += 1
        if maria > ben:
            return "Maria"
        elif ben > maria:
            return "Ben"
        else:
            return None
    return None
