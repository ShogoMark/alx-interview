#!/usr/bin/python3

def pascal_triangle(n):
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
