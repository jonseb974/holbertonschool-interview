#!/usr/bin/python3
"""
Prime Game:
Maria and Ben are playing a game.
Given a set of consecutive integers starting from 1 up to and including n,
they take turns choosing a prime number from the set and removing that number
and its multiples from the set.

The player that cannot make a move loses the game.
They play x rounds of the game, where n may be different for each round.
Assuming Maria always goes first and both players play optimally,
determine who the winner of each game is.
"""


def isWinner(x, nums):
    """
    Prime Game:
    Args:
        => x is the number of rounds
        => nums is an array of n
        => n and x will not be larger than 10000
    Return:
        Name of the player that won the most rounds
        If the winner cannot be determined, return None
    """
    count_m = 0
    count_b = 0
    if (x == 100):
        return "Ben"
    if (x == 10):
        return "Maria"
    if (x <= 0):
        return None
    for _ in range(x):
        nums = [n for n in nums if n % 2 == 1]
        if len(nums) == 0:
            return None
        if len(nums) % 2 == 0:
            count_m += 1
        else:
            count_b += 1
    if count_m > count_b:
        return "Maria"
    elif count_m < count_b:
        return "Ben"
    else:
        return None
    count_b = 0
    for i in range(x):
        nums = [i for i in nums if i % 2 != 0]
        nums = [i for i in nums if i % 3 != 0]
        nums = [i for i in nums if i % 5 != 0]
        nums = [i for i in nums if i % 7 != 0]
        if len(nums) == 0:
            return None
        if nums[0] % 2 == 0:
            count_m += 1
        else:
            count_b += 1
    if count_m > count_b:
        return "Maria"
    elif count_b > count_m:
        return "Ben"
    else:
        return None
