#!/usr/bin/python3
"""Island Perimeter"""


def island_perimeter(grid):
    """island_perimeter(grid) returns the perimeter of the island
    The island grid is a list of list of integers, 0 is the water,
    and 1 is the land"""
    if type(grid) != list:
        return 0
    row = len(grid)
    col = len(grid[0])
    if (row <= 1 or row > 100 or col <= 1 or col > 100):
        return 0
    result = 0
    """loop through each cell in the grid"""
    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1:
                """check the top, bottom, left side and right side"""
                if grid[i - 1][j] == 0 or i == 0:
                    result += 1

                if grid[i + 1][j] == 0 or i == row - 1:
                    result += 1

                if grid[i][j - 1] == 0 or j == 0:
                    result += 1

                if grid[i][j + 1] == 0 or j == col - 1:
                    result += 1
    return result
