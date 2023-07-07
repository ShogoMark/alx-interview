#!/usr/bin/python3
"""A method that verifies if all boxes can be opened"""


def canUnlockAll(boxes):
    """Method that determines if all the boxes can be opened"""
    matches = []

    for i in range(len(boxes)):
        current_box = boxes[i]

        for j in range(len(current_box)):
            current_item = current_box[j]

            for k in range(i + 1, len(boxes)):
                other_box = boxes[k]

                for other_boxes in range(len(other_box)):
                    other_item = other_box[other_boxes]

                    if current_item == other_box:
                        matches.append(True)
                        break
                else:
                    continue
                break
            else:
                continue
            break
    
    return all(matches)
