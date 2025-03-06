# https://leetcode.com/problems/01-matrix/
# Difficulty: Medium
# Tags: bfs matrix

# Problem
# Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
# The distance between two cells sharing a common edge is 1.

# Solution
# Time O(m*n) and space O(m*n)
# First we traverse the matrix and add 0s to queue while setting 1s to -1 to show they are unvisited. Then we use bfs to move through cells and find unvisited nodes while updating distance. Thus we find the shortest distance for each node.


from collections import deque
from typing import List


def updateMatrix(mat: List[List[int]]) -> List[List[int]]:
    m = len(mat)
    n = len(mat[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    q = deque()

    for row in range(m):
        for col in range(n):
            if mat[row][col] == 0:
                q.append((row, col, 0))
            else:
                mat[row][col] = -1

    while q:
        curr_row, curr_col, dist = q.popleft()
        for dy, dx in directions:
            new_row, new_col = curr_row + dy, curr_col + dx
            if (
                0 <= new_row < m
                and 0 <= new_col < n
                and mat[new_row][new_col] == -1
            ):
                mat[new_row][new_col] = dist + 1
                q.append((new_row, new_col, dist + 1))

    return mat
