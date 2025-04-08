# https://leetcode.com/problems/sudoku-solver/
# Difficulty: Hard
# Tags: backtracking sudoku

# Problem
# Write a program to solve a Sudoku puzzle by filling the empty cells.

# A sudoku solution must satisfy all of the following rules:

#     Each of the digits 1-9 must occur exactly once in each row.
#     Each of the digits 1-9 must occur exactly once in each column.
#     Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.

# The '.' character indicates empty cells.

# Solution
# Time O((9!)^9) and space O(81)
# We use backtracking for this problem. It eliminates redundant (wrong) candidates. But first we go over a board and write down existing numbers to the rows, cols and boxes sets. These sets are important, they will help us check if a particular number exists in any in constant time. We also keep track of empty cells to avoid unnessary search in the future. Then we use backtracking to place the number if it can be placed and continue that process until no possible solution is found. Then we backtrack (remove latest number) and try again. We do this recursively until our empty cells array is empty (we reached the end).

from typing import List


class Solution:
    def place_number(self, board, row, col, number):
        self.row[row].add(board[row][col])
        self.col[col].add(board[row][col])
        self.box[(row // 3) * 3 + (col // 3)].add(board[row][col])

    def populate_board(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    self.place_number(board, i, j, board[i][j])
                else:
                    self.empty.append((i, j))

    def solve(self, board, index):
        if index == len(self.empty):
            return True
        i, j = self.empty[index]

        for c in "123456789":
            if self.isSafe(i, j, c):
                board[i][j] = c
                self.row[i].add(c)
                self.col[j].add(c)
                self.box[(i // 3) * 3 + (j // 3)].add(c)
                if self.solve(board, index + 1):
                    return True
                board[i][j] = "."
                self.row[i].remove(c)
                self.col[j].remove(c)
                self.box[(i // 3) * 3 + (j // 3)].remove(c)
        return False

    def isSafe(self, i, j, c):
        if (
            c in self.row[i]
            or c in self.col[j]
            or c in self.box[(i // 3) * 3 + (j // 3)]
        ):
            return False
        return True

    def solveSudoku(self, board: List[List[str]]) -> None:
        n = 3
        N = n * n
        self.row = [set() for _ in range(N)]
        self.col = [set() for _ in range(N)]
        self.box = [set() for _ in range(N)]
        self.empty = []
        self.populate_board(board)
        self.solve(board, 0)
