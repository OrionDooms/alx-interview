#!/usr/bin/python3
"""Making Change function"""


def ChangeHelper(coins, total, m):
    """ChangeHelper use recursion to handle larger coin values.
    The memo(Memoization) helps store already computed results and avoiding
    repeated calculated totals"""
    if total != 0:
        if total < 0:
            return -1
        """check memo is already memoized"""
        if total in m:
            return m[total]
        """Initialize the fewest_coins to infinity"""
        fewest_coins = float('inf')
        for coin in coins:
            if total >= coin:
                value = ChangeHelper(coins, total - coin, m)
                if value >= 0:
                    result = value + 1
                    fewest_coins = min(fewest_coins, result)
        """The current memo total"""
        if fewest_coins != float('inf'):
            m[total] = fewest_coins
        else:
            m[total] = -1
        return m[total]
    return 0


def makeChange(coins, total):
    """makeChange takes a pile of coins of different values and determine
    the fewest number of coins needed to meet a given amount total"""
    memo = {}
    return ChangeHelper(coins, total, memo)
