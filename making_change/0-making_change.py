#!/usr/bin/python3
"""
makeChange function determines the fewest number of coins needed
to meet a given amount
"""


def makeChange(coins, total):
    """
    Prototype: def makeChange(coins, total):
    Args:
      coins: list of values of coins in your possession
        (the value of a coin will always be an int > 0)
        (you can assume you have an infinite supply of each coin)
      total: amount of money you want to make change for
    Return:
      if total is <= 0: return 0
      if total cannot be met: return -1
      if total can be met: return the minimum number of coins needed
        to meet total.
    """
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        if total >= coin:
            count += total // coin
            total %= coin
    if total == 0:
        return count
    if total <= 0:
        return 0
    return -1
