#!/usr/bin/python3
"""
Interview question on minimum operation
"""


def minOperations(n):
    """Takes in n and determine the fewest number of operations it can make"""

    if n <= 0:
        return 0
    operations = 0
    i = 2
    while i <= n:
        while n % i == 0:
            operations += i
            n /= i
        i += 1

    return operations
