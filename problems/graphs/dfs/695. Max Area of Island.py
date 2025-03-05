# https://leetcode.com/problems/max-area-of-island/
# Difficulty: Medium
# Tags: graph dfs

# Problem
# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

# The area of an island is the number of cells with a value 1 in the island.

# Return the maximum area of an island in grid. If there is no island, return 0.

# Solution
# Time O(M*N) where m is the number of rows, n is the number of cols; space O(M*N). It is O(M*N) as dfs moves through 1s only once!
# We use dfs to move over islands and calculate the area for each island while updating the max area. Recursive function in this case returns the area of an island. We need to move to all directions and check if the land is valid.

from typing import List


def maxAreaOfIsland(grid: List[List[int]]) -> int:

    m = len(grid)
    n = len(grid[0])
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def is_valid_land(row, col):
        return 0 <= row < m and 0 <= col < n

    def dfs(row, col):
        if not is_valid_land(row, col) or grid[row][col] == 0:
            return 0
        grid[row][col] = 0
        area = 1
        for dy, dx in directions:
            new_row, new_col = row + dy, col + dx
            area += dfs(new_row, new_col)
        return area

    max_area = 0
    for row in range(m):
        for col in range(n):
            if grid[row][col] == 1:
                max_area = max(max_area, dfs(row, col))
    return max_area
