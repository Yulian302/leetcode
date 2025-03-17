# https://leetcode.com/problems/the-maze-ii/
# Difficulty: Medium
# Tags: bfs maze dijkstra

# Problem
# There is a ball in a maze with empty spaces (represented as 0) and walls (represented as 1). The ball can go through the empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

# Given the m x n maze, the ball's start position and the destination, where start = [startrow, startcol] and destination = [destinationrow, destinationcol], return the shortest distance for the ball to stop at the destination. If the ball cannot stop at destination, return -1.

# The distance is the number of empty spaces traveled by the ball from the start position (excluded) to the destination (included).

# You may assume that the borders of the maze are all walls (see examples).

# Solution
# Time O(m*n*max(m,n)) and space O(m*n)
# At first this problem seems to easily be solved using bfs. But actually simple bfs would not work. We can imagine the maze as a weighted graph as we have determined edges (ball rolls). So, in order to solve this problem, we need to use Dijkstra to find the shortest path. It's quite easy to switch to Dijkstra from simple BFS, just by substituting the queue with priority queue (min heap) prioritizing each element by distance. We also have to keep track of distance map to check if new dist is less than already found one.


import heapq
from typing import List


def shortestDistance(
    maze: List[List[int]], start: List[int], destination: List[int]
) -> int:
    m = len(maze)
    n = len(maze[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    minHeap = []
    # (dist, row, col)
    heapq.heappush(minHeap, (0, start[0], start[1]))
    dist_map = {(start[0], start[1]): 0}
    while minHeap:
        dist, row, col = heapq.heappop(minHeap)

        if [row, col] == destination:
            return dist

        for dy, dx in directions:
            new_row, new_col = row, col
            step_count = 0
            while (
                0 <= new_row + dy < m
                and 0 <= new_col + dx < n
                and maze[new_row + dy][new_col + dx] == 0
            ):
                new_row += dy
                new_col += dx
                step_count += 1

            new_dist = dist + step_count

            if (new_row, new_col) not in dist_map or new_dist < dist_map[
                (new_row, new_col)
            ]:
                dist_map[(new_row, new_col)] = new_dist
                heapq.heappush(minHeap, (new_dist, new_row, new_col))
    return -1
