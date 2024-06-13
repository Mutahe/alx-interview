#!/usr/bin/python3
""" A method that calculates the fewest number of 
operations needed to result in exactly n H characters in the file
"""


def minOperations(n):
    """
    Method for compute the minimum number
    of operations for task Copy All and Paste

    Args:
        n: input value
        value_list: List to save the operations
    Return: the sum of the operations
    """
    if n < 2:
        return 0
    value_list = []
    k = 1
    while n != 1:
        k += 1
        if n % k == 0:
            while n % k == 0:
                n /= k
                value_list.append(k)
    return sum(value_list)