# https://leetcode.com/problems/minimum-knight-moves/
# Difficulty: Medium
# Tags: bfs minimum chess

# Problem
# In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].

# A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.

# Solution
# Time O((max(∣x∣,∣y∣))^2) and space O((max(∣x∣,∣y∣))^2)
# We use standard bfs approach to search for solutions, but we have to add an outer loop in a queue in order to visit all the children at the time and explore other moves. Simply speaking, it imitates the signal going in all possible directions from starting point. That's the way of finding the least number of moves to the solution which always exists.

from collections import deque


def minKnightMoves(x: int, y: int) -> int:

    directions = [
        (-1, -2),
        (-2, -1),
        (-2, 1),
        (-1, 2),
        (1, -2),
        (2, -1),
        (2, 1),
        (1, 2),
    ]

    # (row, col)
    q = deque([(0, 0)])
    seen = {(0, 0)}
    steps = 0
    while q:
        for i in range(len(q)):
            row, col = q.popleft()
            if [row, col] == [x, y]:
                return steps
            for dy, dx in directions:
                new_row, new_col = row + dy, col + dx
                if (new_row, new_col) not in seen:
                    seen.add((new_row, new_col))
                    q.append((new_row, new_col))
        steps += 1
    return steps
