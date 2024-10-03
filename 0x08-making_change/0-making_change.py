#!/usr/bin/python3
"""Making Change function"""


def makeChange(coins, total):
    """makeChange takes a pile of coins of different values and determine
    the fewest number of coins needed to meet a given amount total"""
    if total != 0:
        if total < 0:
            return -1
        fewest_coins = float('inf')
        for coin in coins:
            if amount - coin >= 0:
                value = MinCoins(coins, amount - coin)
                if value >= 0:
                    result = value + 1
                    fewest_coins = min(fewest_coins, result)
        if fewest_coins != flaot('inf'):
            return fewest_coins
        else:
            return -1
    return 0
