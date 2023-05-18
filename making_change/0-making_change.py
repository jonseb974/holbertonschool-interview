#!/usr/bin/python3
"""
Module: 0-making_change.py
"""

from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """
    Determines the fewest number of coins needed to meet a given total amount.

    Args:
        coins (List[int]): A list of coin values in your possession.
        total (int): The total amount to be achieved.

    Returns:
        int: The fewest number of coins needed to meet the total amount.
             If the total is 0 or less, returns 0.
             If the total cannot be met by any number of coins you have,
             returns -1.

    Raises:
        None.
    """

    if total <= 0:
        return 0

    # Create a list to store the fewest number of coins needed for each total
    # amount
    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0

    # Iterate through all possible amounts from 1 to the given total
    for amount in range(1, total + 1):
        # Check each coin to see if it can be used to make change for
        # the current amount
        for coin in coins:
            if coin <= amount:
                # Calculate the number of coins needed for the current amount
                num_coins = min_coins[amount - coin] + 1
                if num_coins < min_coins[amount]:
                    min_coins[amount] = num_coins

    # If the minimum number of coins for the total amount is still infinity,
    # it means it cannot be met
    if min_coins[total] == float('inf'):
        return -1
    else:
        return min_coins[total]
