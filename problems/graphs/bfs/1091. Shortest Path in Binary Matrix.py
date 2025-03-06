# https://leetcode.com/problems/shortest-path-in-binary-matrix/
# Difficulty: Medium
# Tags: graph bfs

# Problem
# Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

# A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

#     All the visited cells of the path are 0.
#     All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).

# The length of a clear path is the number of visited cells of this path.

# Solution
# Time O(n^2) and space O(n^2)
# We use bfs to travel over 0s and determine the shortest path. The way the length is incremented in a bfs approach works to find the shortest path possible from starting position to ending position.

from collections import deque
from typing import List


def shortestPathBinaryMatrix(grid: List[List[int]]) -> int:
    n = len(grid)
    if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
        return -1
    directions = [
        (-1, 0),
        (-1, 1),
        (0, 1),
        (1, 1),
        (1, 0),
        (1, -1),
        (0, -1),
        (-1, -1),
    ]
    # (row,col,length)
    q = deque([(0, 0, 1)])
    grid[0][0] = 1
    while q:
        row, col, length = q.popleft()
        if row == n - 1 and col == n - 1:
            return length

        for dy, dx in directions:
            new_row, new_col = row + dy, col + dx
            if (
                0 <= new_row < n
                and 0 <= new_col < n
                and grid[new_row][new_col] == 0
            ):
                grid[new_row][new_col] = 1
                q.append((new_row, new_col, length + 1))
    return -1
