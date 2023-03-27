def canUnlockAll(boxes):
    '''This method that determines if all the boxes can be opened.
       canUnlockAll Keeps track of which boxes we've seen
       and whether they're open or not.
    '''
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

    return all(seen)
