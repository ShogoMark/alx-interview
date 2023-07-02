#!/usr/bin/python3

"""
    Creates a function that returns a list of lists of integers
    representing a Pascal's triangle for any given integer of n
"""


def pascal_triangle(n):
    """
        A function that creates a list of lists of integers representing
        the Pascal's triangle of n.
    """
    res = []

    if n > 0:
        for row in range(n):
            if row == 0:
                res.append([1])
            else:
                prev_row = res[row - 1]
                current_row = [1]

                for i in range(1, row):
                    current_row.append(prev_row[i - 1] + prev_row[i])

                current_row.append(1)
                res.append(current_row)
        return res
    else:
        return []
