#!/usr/bin/python3
"""Island Perimeter"""


def island_perimeter(grid):
    """island_perimeter(grid) returns the perimeter of the island
    The island grid is a list of list of integers, 0 is the water,
    and 1 is the land"""
    result = 0
    if type(grid) == list:
        row = len(grid)
        col = len(grid[0])
        """loop through each cell in the grid"""
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    """check the top, bottom, left side and right side"""
                    if i == 0:
                        result += 1
                    if grid[i - 1][j] == 0:
                        result += 1

                    if i == row - 1:
                        result += 1
                    if grid[i + 1][j] == 0:
                        result += 1

                    if j == 0:
                        result += 1
                    if grid[i][j - 1] == 0:
                        result += 1

                    if j == col - 1:
                        result += 1
                    if grid[i][j + 1] == 0:
                        result += 1

    return result
