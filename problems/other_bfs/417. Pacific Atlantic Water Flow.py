# https://leetcode.com/problems/pacific-atlantic-water-flow/
# Difficulty: Medium
# Tags: bfs reverse_bfs ocean

# Problem
# There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

# The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

# The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

# Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.


# Solution
# Time O(m*n) and space O(m*n)
# This problem can be solved using a reverse BFS approach. We start from the oceans to find those nodes that cen be reached. So, we add both atlantic and pacific ocean starting points to initial queue. We also have to keep track of seen nodes for both oceans (queues). Then we use bfs on both queues exploring only the cells that are in bounds and that are more than or equal to current cell (imitate that rain can be flown from i+1 cell to i). In the end, we return the intersection for both sets of visited cells for both oceans. It gives us the cells from which rain can be flown to both of the oceans.

from collections import deque
from typing import List


def pacificAtlantic(heights: List[List[int]]) -> List[List[int]]:

    if not heights:
        return []

    m = len(heights)
    n = len(heights[0])

    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    pacific_seen = set()
    atlantic_seen = set()

    def bfs(starts, seen):
        q = deque(starts)
        while q:
            row, col = q.popleft()
            seen.add((row, col))
            for dy, dx in directions:
                new_row, new_col = row + dy, col + dx
                if (
                    0 <= new_row < m
                    and 0 <= new_col < n
                    and heights[new_row][new_col] >= heights[row][col]
                    and (new_row, new_col) not in seen
                ):
                    q.append((new_row, new_col))

    # start from both oceans
    pacific_starts = [(0, j) for j in range(n)] + [(i, 0) for i in range(m)]
    atlantic_starts = [(m - 1, j) for j in range(n)] + [
        (i, n - 1) for i in range(m)
    ]

    bfs(pacific_starts, pacific_seen)
    bfs(atlantic_starts, atlantic_seen)

    return list(pacific_seen & atlantic_seen)
