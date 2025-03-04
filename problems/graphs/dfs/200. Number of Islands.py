# https://leetcode.com/problems/number-of-islands/
# Difficulty: Medium
# Tags: graph dfs

# Problem
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Solution
# O(M*N) as we traverse across entire matrix updating seen elements to avoid repetetive visits, and space O(M*N)
# We iterate over entire matrix and as soon as the element is 1, we add it to seen, update counter and use dfs recursive function to add all other 1s near this one. This way we can efficiently find a number of islands. PS: We should also implement a function to check if next calculated row and col are within bounds.

from typing import List


def numIslands(grid: List[List[str]]) -> int:
    m = len(grid)
    n = len(grid[0])

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    seen = set()
    ans = 0

    def is_valid(row, col):
        return 0 <= row < m and 0 <= col < n and grid[row][col] == "1"

    def dfs(row, col):
        stack = [(row, col)]
        while stack:
            row, col = stack.pop()
            for dy, dx in directions:
                new_row, new_col = row + dy, col + dx
                if is_valid(new_row, new_col) and (new_row, new_col) not in seen:
                    seen.add((new_row, new_col))
                    stack.append((new_row, new_col))

    for row in range(m):
        for col in range(n):
            if grid[row][col] == "1" and (row, col) not in seen:
                ans += 1
                seen.add((row, col))
                dfs(row, col)
    return ans
