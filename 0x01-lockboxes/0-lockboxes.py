#!/usr/bin/python3

from collections import deque

def canUnlockAll(boxes):
    # Initialize a set to keep track of visited boxes
    visited = set()
    # Initialize a queue to perform BFS
    queue = deque([0])  # Start with the first box
    visited.add(0)  # Mark the first box as visited

    while queue:
        current_box = queue.popleft()  # Get the next box from the queue
        # Check all keys in the current box
        for key in boxes[current_box]:
            # If the key opens a new box and it hasn't been visited yet
            if key < len(boxes) and key not in visited:
                # Mark the box as visited
                visited.add(key)
                # Add the newly opened box to the queue for further exploration
                queue.append(key)

    # If all boxes have been visited, return True
    return len(visited) == len(boxes)
