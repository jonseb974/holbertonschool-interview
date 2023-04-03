#!/usr/bin/python3
"""
0-minoperations.py
"""


def minOperations(n):
    """
    This method that calculates the fewest number of operations
    needed to result in exactly n H characters in the file.
    """
    if n < 1 or not isinstance(n, int):
        return 0
    if n == 1:
        return 0
    operations = 0
    i = 2
    while i <= n:
        while n % i == 0:
            operations += i
            n /= i
        i += 1
    return operations
