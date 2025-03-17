# https://leetcode.com/problems/the-maze-iii/
# Difficulty: Hard
# Tags: bfs maze dijkstra

# Problem
# There is a ball in a maze with empty spaces (represented as 0) and walls (represented as 1). The ball can go through the empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction. There is also a hole in this maze. The ball will drop into the hole if it rolls onto the hole.

# Given the m x n maze, the ball's position ball and the hole's position hole, where ball = [ballrow, ballcol] and hole = [holerow, holecol], return a string instructions of all the instructions that the ball should follow to drop in the hole with the shortest distance possible. If there are multiple valid instructions, return the lexicographically minimum one. If the ball can't drop in the hole, return "impossible".

# If there is a way for the ball to drop in the hole, the answer instructions should contain the characters 'u' (i.e., up), 'd' (i.e., down), 'l' (i.e., left), and 'r' (i.e., right).

# The distance is the number of empty spaces traveled by the ball from the start position (excluded) to the destination (included).

# You may assume that the borders of the maze are all walls (see examples).


# Solution
# Time O(NlogN) and space O(N)
# At first this problem seems to easily be solved using bfs. But actually simple bfs would not work. We can imagine the maze as a weighted graph as we have determined edges (ball rolls). So, in order to solve this problem, we need to use Dijkstra to find the shortest path. It's quite easy to switch to Dijkstra from simple BFS, just by substituting the queue with priority queue (min heap) prioritizing each element by distance. We also have to keep track of distance map to check if new dist is less than already found one. Besides, we have to keep track of a path that a ball has passed. Below are two implementations: the switch from bfs to dijkstra and more concise dijkstra. We also have to break the tie for same distances by creating a new path lexicographically.


import heapq
from typing import List


def findShortestWay(
    maze: List[List[int]], ball: List[int], hole: List[int]
) -> str:
    m = len(maze)
    n = len(maze[0])

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    directions_verbose = {(0, 1): "r", (0, -1): "l", (1, 0): "d", (-1, 0): "u"}

    minHeap = []
    # (dist, row, col, path)
    heapq.heappush(minHeap, (0, ball[0], ball[1], ""))
    dist_map = {(ball[0], ball[1]): 0}
    path_map = {(ball[0], ball[1]): ""}

    while minHeap:
        dist, row, col, path = heapq.heappop(minHeap)

        if [row, col] == hole:
            return path

        for dy, dx in directions:
            new_row, new_col = row, col
            steps = 0
            while (
                0 <= new_row + dy < m
                and 0 <= new_col + dx < n
                and maze[new_row+dy][new_col+dx] == 0
            ):
                new_row += dy
                new_col += dx
                steps += 1
                if [new_row, new_col] == hole:
                    break
            new_dist = dist + steps
            new_path = path + directions_verbose[(dy, dx)]

            if (new_row, new_col) not in dist_map or new_dist < dist_map[
                (new_row, new_col)
            ]:
                dist_map[(new_row, new_col)] = new_dist
                path_map[(new_row, new_col)] = new_path
                heapq.heappush(minHeap, (new_dist, new_row, new_col, new_path))
            elif (
                new_dist == dist_map[(new_row, new_col)]
                and new_path < path_map[(new_row, new_col)]
            ):
                path_map[(new_row, new_col)] = new_path
                heapq.heappush(minHeap, (new_dist, new_row, new_col, new_path))

    return "impossible"

# --- or ---


def findShortestWay(maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
    def valid(row, col):
        return 0 <= row < m and 0 <= col < n and maze[row][col] == 0

    def get_neighbors(row, col):
        directions = [(0, -1, 'l'), (-1, 0, 'u'), (0, 1, 'r'), (1, 0, 'd')]
        neighbors = []

        for dy, dx, direction in directions:
            curr_row = row
            curr_col = col
            dist = 0

            while valid(curr_row + dy, curr_col + dx):
                curr_row += dy
                curr_col += dx
                dist += 1
                if [curr_row, curr_col] == hole:
                    break

            neighbors.append((curr_row, curr_col, dist, direction))

        return neighbors

    m = len(maze)
    n = len(maze[0])
    # (dist, path, row, col)
    heap = [(0, "", ball[0], ball[1])]
    seen = set()

    while heap:
        curr_dist, path, row, col = heapq.heappop(heap)

        if (row, col) in seen:
            continue

        if [row, col] == hole:
            return path

        seen.add((row, col))

        for next_row, next_col, dist, direction in get_neighbors(row, col):
            heapq.heappush(heap, (curr_dist + dist, path +
                                  direction, next_row, next_col))

    return "impossible"
