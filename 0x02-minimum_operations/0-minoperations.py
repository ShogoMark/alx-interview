#!/usr/bin/python3
"""a function that returns the number of operations"""

import math


def minOperations(n):
    total_op = 0
    copied_H = "H"

    highest_divisor = 1
    for i in range(2, int(math.sqrt(n)) + 1): 
        if n % i == 0:
            highest_divisor = i

    while len(copied_H) <= highest_divisor:
        copied_H += copied_H
        total_op += 1

    while len(copied_H) < n:
        copied_H += copied_H
        total_op += 1

    return total_op
