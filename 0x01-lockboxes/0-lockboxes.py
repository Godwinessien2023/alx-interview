#!/usr/bin/python3
from collections import deque

def canUnlockAll(boxes):
    n = len(boxes)
    if n == 0:
        return True
    
    # Set to keep track of visited boxes
    visited = set()
    visited.add(0)  # Start with the first box unlocked
    
    # Queue for BFS
    queue = deque([0])
    
    while queue:
        current_box = queue.popleft()
        
        # Check keys in the current box
        for key in boxes[current_box]:
            if key < n and key not in visited:
                visited.add(key)
                queue.append(key)
    
    # If all boxes are visited, return True
    return len(visited) == n
