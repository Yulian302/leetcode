# https://leetcode.com/problems/transpose-matrix/
# Difficulty: Easy
# Tags: math matrix transpose

# Problem
# Given a 2D integer array matrix, return the transpose of matrix.

# The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

# Solution
# Time O(m*n) and space O(m*n) or Time O(n^2) and space O(1) for square matrix
# We just swap the rows and columns for a mxn matrix. But for nxn matrix, we can use a better approach: for i in 0..n, for j in i..n.


from typing import List


def transpose(matrix: List[List[int]]) -> List[List[int]]:
    m = len(matrix)
    n = len(matrix[0])
    res = [[0] * m for _ in range(n)]
    for i in range(m):
        for j in range(n):
            res[j][i] = matrix[i][j]
    return res

# --- or ---

# for square matrix


def transposeSquareMatrix(matrix: List[List[int]]) -> List[List[int]]:
    m = len(matrix)
    n = len(matrix[0])
    for i in range(m):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix
