#!/usr/bin/python3
"""A method that verifies if all boxes can be opened"""


def canUnlockAll(boxes):
    """Method that determines if all the boxes can be opened"""

    if type(boxes) != list or len(boxes) == 0:
        return False

    boxLength = len(boxes)

    freeKeys = [0]
    usedKeys = set()

    while freeKeys:
        openedBoxIndex = freeKeys.pop()
        usedKeys.add(openedBoxIndex)

        openedBox = boxes[openedBoxIndex]

        if type(openedBox) != list:
            return False

        for key in openedBox:
            if key < boxLength and key not in freeKeys and key not in usedKeys:
                freeKeys.append(key)
    return len(usedKeys) == boxLength
