#!/usr/bin/python3
"""Island Perimeter"""


def island_perimeter(grid):
    """island_perimeter(grid) returns the perimeter of the island
    The island grid is a list of list of integers, 0 is the water,
    and 1 is the land"""
    result = 0
    if type(grid) == list:
        rows = len(grid)
        cols = len(grid[0])
        """loop through each cell in the grid"""
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    result += 4
                    """check the top, bottom, left side and right side"""
                    if (grid[row + 1][col] == 1 and row < rows - 1):
                        result -= 2
                    if (grid[row][col + 1] == 1 and col < cols - 1):
                        result -= 2
    return result
