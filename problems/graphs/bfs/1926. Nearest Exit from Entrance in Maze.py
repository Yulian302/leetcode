# https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/
# Difficulty: Medium
# Tags: graph bfs

# Problem
# You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') and walls (represented as '+'). You are also given the entrance of the maze, where entrance = [entrancerow, entrancecol] denotes the row and column of the cell you are initially standing at.

# In one step, you can move one cell up, down, left, or right. You cannot step into a cell with a wall, and you cannot step outside the maze. Your goal is to find the nearest exit from the entrance. An exit is defined as an empty cell that is at the border of the maze. The entrance does not count as an exit.

# Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists.

# Solution
# Time O(m*n) and space O(m*n)
# Standard bfs problem to find shortest path. We start moving from entrance cell until the exit is reached. We have to keep track of steps taken, so our queue is the following tuple: (node, steps). Visited nodes are tracked like this: (row, col). No additional state is needed.

from collections import deque
from typing import List


def nearestExit(maze: List[List[str]], entrance: List[int]) -> int:
    m = len(maze)
    n = len(maze[0])

    if m == 1 and n == 1:
        return -1

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def inbounds(row, col):
        return 0 <= row < m and 0 <= col < n

    def is_exit(row, col):
        return (row == 0 or row == m - 1 or col == 0 or col == n - 1) and (
            row,
            col,
        ) != (entrance[0], entrance[1])

    # (row,col,steps)
    q = deque([(entrance[0], entrance[1], 0)])
    # (row,col)
    seen = {(entrance[0], entrance[1])}
    while q:
        for _ in range(len(q)):
            row, col, steps = q.popleft()

            for dy, dx in directions:
                new_row, new_col = row + dy, col + dx
                if (
                    (new_row, new_col) not in seen
                    and inbounds(new_row, new_col)
                    and maze[new_row][new_col] != "+"
                ):
                    seen.add((new_row, new_col))
                    if is_exit(new_row, new_col):
                        return steps + 1
                    q.append((new_row, new_col, steps + 1))
    return -1
