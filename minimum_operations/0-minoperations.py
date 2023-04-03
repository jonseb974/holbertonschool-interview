#!/usr/bin/python3
"""
0-minoperations.py
"""


def minOperations(n):
    """
    This method that calculates the fewest number of operations
    needed to result in exactly n H characters in the file.
    """
    if n == 1:
        return 0
    dp = [float('inf')] * (n+1)
    dp[1] = 0
    for i in range(2, n+1):
        for j in range(1, i):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + (i//j))
    if dp[n] == float('inf'):
        return 0
    return dp[n]

