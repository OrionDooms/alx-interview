#!/usr/bin/python3
"""There are locked boxes. Each box is numbered sequentially from 0 to n - 1
and each box may contain keys to the other boxes."""


def canUnlockAll(boxes):
    size = len(boxes)
    test_list = [False] * size
    test_list[0] = True

    def firstSearch(box):
        """Search through all items in the current list"""
        for x in boxes[box]:
            if x < size and not test_list[x]:
                test_list[x] = True
                firstSearch(x)

    firstSearch(0)
    """Return True if all boxes are opened, else False"""
    return all(test_list)
