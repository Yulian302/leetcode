# https://leetcode.com/problems/set-matrix-zeroes/
# Difficulty: Medium
# Tags: matrix array

# Problem
# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

# You must do it in place.

# Solution
# Most efficient: Time O(mn) and space O(1)
# One way to solve it is to iterate the matrix -> and set row and col elems to 0 and storing them in set to avoid additional processing: Time O(mn(m+n)) and space O(mn). Another way would be to iterate the matrix and for 0 elements add curr row and curr col to corresponding sets. Then iterate matrix again and set to 0 if curr row is in rows or curr col is in cols. Time O(mn) and space O(m+n). The most efficient way in terms of space complexity will be to iterate the matrix and only set the beginning of row and col to 0 if 0 element is spotted. Then iterate again skipping first row and col -> set elements to 0 if curr row or curr col have 0 at the beginning. Then we just have to process first row and first col additionaly. Space O(1).

from typing import List


class Solution(object):
    def setZeroes(self, matrix: List[List[int]]) -> None:
        is_col = False
        R = len(matrix)
        C = len(matrix[0])
        for i in range(R):
            if matrix[i][0] == 0:
                is_col = True
            for j in range(1, C):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for i in range(1, R):
            for j in range(1, C):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for j in range(C):
                matrix[0][j] = 0

        if is_col:
            for i in range(R):
                matrix[i][0] = 0
