# https://leetcode.com/problems/the-maze/
# Difficulty: Medium
# Tags: bfs maze

# Problem
# There is a ball in a maze with empty spaces (represented as 0) and walls (represented as 1). The ball can go through the empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

# Given the m x n maze, the ball's start position and the destination, where start = [startrow, startcol] and destination = [destinationrow, destinationcol], return true if the ball can stop at the destination, otherwise return false.

# You may assume that the borders of the maze are all walls (see examples).

# Solution
# Time O(mn(m+n)) and space O(m*n)
# We use bfs for this problem. It's a typical bfs problem for finding out if it's possible to get to `destination` from `start`. The curveball in this problem is only the way to move the ball in a certain direction. We have to check the bounds and move it in a loop until wall is reached.

from collections import deque
from typing import List


def hasPath(
    maze: List[List[int]], start: List[int], destination: List[int]
) -> bool:
    m = len(maze)
    n = len(maze[0])

    if m == 1 and n == 1:
        return start[0] == destination[0] and start[1] == destination[1]

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    q = deque([start])
    seen = {(start[0], start[1])}
    while q:
        row, col = q.popleft()

        if [row, col] == destination:
            return True

        for dy, dx in directions:
            new_row, new_col = row, col
            while (
                0 <= new_row + dy < m
                and 0 <= new_col + dx < n
                and maze[new_row + dy][new_col + dx] == 0
            ):
                new_row += dy
                new_col += dx

            if (new_row, new_col) not in seen:
                seen.add((new_row, new_col))
                q.append((new_row, new_col))

    return False
