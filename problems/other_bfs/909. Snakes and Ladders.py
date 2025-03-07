# https://leetcode.com/problems/snakes-and-ladders/
# Difficulty: Medium
# Tags: bfs matrix Boustrophedon style

# Problem
# You are given an n x n integer matrix board where the cells are labeled from 1 to n2 in a Boustrophedon style starting from the bottom left of the board (i.e. board[n - 1][0]) and alternating direction each row.

# You start on square 1 of the board. In each move, starting from square curr, do the following:

#     Choose a destination square next with a label in the range [curr + 1, min(curr + 6, n2)].
#         This choice simulates the result of a standard 6-sided die roll: i.e., there are always at most 6 destinations, regardless of the size of the board.
#     If next has a snake or ladder, you must move to the destination of that snake or ladder. Otherwise, you move to next.
#     The game ends when you reach the square n2.

# A board square on row r and column c has a snake or ladder if board[r][c] != -1. The destination of that snake or ladder is board[r][c]. Squares 1 and n2 are not the starting points of any snake or ladder.

# Note that you only take a snake or ladder at most once per dice roll. If the destination to a snake or ladder is the start of another snake or ladder, you do not follow the subsequent snake or ladder.

#     For example, suppose the board is [[-1,4],[-1,3]], and on the first move, your destination square is 2. You follow the ladder to square 3, but do not follow the subsequent ladder to 4.

# Return the least number of dice rolls required to reach the square n2. If it is not possible to reach the square, return -1.

# Solution
# Time O(n^2) and space O(n^2)
# We use bfs for this problem to find the least number of dice rolls to reach from start to end. We add pos to queue instead of coordinates to avoid unnessesary convertion, and, surely, number of rolls. In seen set we only need pos (one state). The most tricky and complex part is to come up with convertion of Boustrophedon number into a row,col coordinate. Personally, I had to look it up... Any other part is quite similar to other bfs problems for optimal search.


from collections import deque
from typing import List


def snakesAndLadders(board: List[List[int]]) -> int:
    n = len(board)
    # (row, col)

    def position_to_coordinates(curr, n):
        row = n - 1 - (curr - 1) // n
        col = (curr - 1) % n

        if (n - 1 - row) % 2 == 1:
            col = n - 1 - col
        return row, col

    # (pos, rolls)
    q = deque([(1, 0)])
    # (pos)
    seen = {1}
    while q:
        for _ in range(len(q)):
            pos, rolls = q.popleft()

            if pos == n * n:
                return rolls

            for next_pos in range(pos + 1, min(pos + 7, n * n + 1)):
                row, col = position_to_coordinates(next_pos, n)
                if board[row][col] != -1:
                    next_pos = board[row][col]

                if next_pos not in seen:
                    seen.add(next_pos)
                    q.append((next_pos, rolls + 1))
    return -1
