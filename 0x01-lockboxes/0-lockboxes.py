def canUnlockAll(boxes):
    size = len(boxes)
    test_list = [False] * size
    test_list[0] = True

    def firstSearch(box):
        for x in boxes[box]:
           if x < size and not test_list[x]:
               test_list[x] = True
               firstSearch(x)

    firstSearch(0)
    return all(test_list)
