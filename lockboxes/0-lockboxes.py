#!/usr/bin/python3


def canUnlockAll(boxes):
    # Keep track of which boxes we've seen and whether they're open or not
    seen = [False] * len(boxes)
    seen[0] = True
    open_boxes = [0]

    # Perform a depth-first search starting from box 0
    while open_boxes:
        box = open_boxes.pop()
        for key in boxes[box]:
            if key < len(boxes) and not seen[key]:
                seen[key] = True
                open_boxes.append(key)

    # If we've seen all the boxes, return True
    return all(seen)
