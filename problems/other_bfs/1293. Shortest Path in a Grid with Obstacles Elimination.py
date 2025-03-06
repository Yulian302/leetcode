# https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/
# Difficulty: Hard
# Tags: bfs grid shortest_path obstacles

# Problem
# You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle). You can move up, down, left, or right from and to an empty cell in one step.

# Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1) given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.

# Solution
# Time O(m*n*k) and space O(m*n*k) as we need to explore the total number of unique states
# We need to use bfs for this problem to find the shortest path. We start from (0,0) and end at (m-1,n-1), meanwhile incrementing number of steps taken. While making decision what cell to take at each bfs iteration, we need to check the boundaries of a new cell and if it has an obstacle. Then if it does, we destroy the obstacle if the remaining k allows us to do that. We propagate our k across other cells. Of course we also need to keep track of visited nodes using a set in this format: (row,col,remaining_k). Remaining k for each cell is crucial as we can have another state for this cell with different k.

from collections import deque
from typing import List


def shortestPath(grid: List[List[int]], k: int) -> int:
    m = len(grid)
    n = len(grid[0])
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    if m == 1 and n == 1:
        return 0

    def is_valid_cell(row, col):
        return 0 <= row < m and 0 <= col < n

    # (row,col,remaining_k)
    q = deque([(0, 0, k)])
    steps = 0
    visited = {(0, 0, k)}
    while q:
        for _ in range(len(q)):
            row, col, remaining_k = q.popleft()

            for dy, dx in directions:
                new_row, new_col = row + dy, col + dx
                if is_valid_cell(new_row, new_col):
                    new_k = remaining_k - grid[new_row][new_col]

                    if new_row == m - 1 and new_col == n - 1:
                        return steps + 1

                    if new_k >= 0 and (new_row, new_col, new_k) not in visited:
                        visited.add((new_row, new_col, new_k))
                        q.append((new_row, new_col, new_k))
        steps += 1
    return -1
