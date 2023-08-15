#!/usr/bin/python3
"""a function that returns the number of operations"""

import math


def minOperations(n):
    """function that takes in a number n of H to copy"""

    total_op = 0
    copied_H = "H"

    highest_divisor = 1
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            highest_divisor = i
            break

    if highest_divisor == 1:
        return 0

    while len(copied_H) < n:
        copied_H += copied_H
        total_op += 1

    return total_op
