#!/usr/bin/python3
"""function that calculate perimeter of island"""

def island_perimeter(grid):
    """function take in grid of area"""
    
    land = 0

    for i in range(0, len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                land += 1

    perimeter = land * 4

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                # check left neighbor
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2 # subtract 2 for the shared edge

                # check top neighbor
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2 # subtract 2 for the shared edge

    return perimeter
