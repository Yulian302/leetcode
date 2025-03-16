# https://leetcode.com/problems/rotting-oranges/
# Difficulty: Medium
# Tags: bfs matrix

# Problem
# You are given an m x n grid where each cell can have one of three values:

#     0 representing an empty cell,
#     1 representing a fresh orange, or
#     2 representing a rotten orange.

# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

# Solution
# Time O(m*n) and space O(m*n)
# A little modified BFS problem, because we should start at multiply points at once. So, first we traverse the matrix, count the number of fresh oranges to early return when all of them are rotten; and add rotten oranges to queue. Then we use queue to do bfs from all rotten oranges and rot fresh oranges that are on the way. Directions of rotting are not diagonal. We can return early as the number of fresh oranges is zero.

from collections import deque
from typing import List


def orangesRotting(grid: List[List[int]]) -> int:

    m = len(grid)
    n = len(grid[0])
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    fresh = 0
    # (row,col)
    q = deque()
    for row in range(m):
        for col in range(n):
            if grid[row][col] == 2:
                q.append((row, col))
            elif grid[row][col] == 1:
                fresh += 1
    minutes = 0
    while q and fresh > 0:
        n_nodes = len(q)
        for _ in range(n_nodes):
            row, col = q.popleft()
            for dy, dx in directions:
                new_row, new_col = row + dy, col + dx
                if (
                    0 <= new_row < m
                    and 0 <= new_col < n
                    and grid[new_row][new_col] == 1
                ):
                    grid[new_row][new_col] = 2
                    fresh -= 1
                    q.append((new_row, new_col))
        minutes += 1
    return minutes if fresh == 0 else -1
