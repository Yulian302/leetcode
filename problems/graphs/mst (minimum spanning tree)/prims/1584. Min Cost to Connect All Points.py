# https://leetcode.com/problems/min-cost-to-connect-all-points/
# Difficulty: Medium
# Tags: graph mst prims

# Problem
# You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

# The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

# Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

# Solution
# Time O(N^2*logN) and space O(N)
# This problem is the Minimum Spanning Tree problem. It can be solved using Prim's algorithm. We initialize a set (or an array when number of nodes is predefined) of visited nodes and set arbitrary start node to True. Starting from that node, we add it's neighbours to min heap, which focuses on edges' weights and keeps a minimum edge. Then we repeat that process until min heap is not empty and number of edges is not equal to N-1.

from collections import defaultdict
import heapq
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        graph = defaultdict(list)

        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                distance = abs(x1 - x2) + abs(y1 - y2)
                graph[i].append((j, distance))
                graph[j].append((i, distance))

        edges = 0
        totalCost = 0
        visited = [False]*n
        start_node = 0
        # let start node be 0
        visited[start_node] = True
        # (weight, start_node, neighbor)
        min_heap = []
        for nei, weight in graph[start_node]:
            heapq.heappush(min_heap, (weight, nei))

        while min_heap and edges < n-1:
            weight, node = heapq.heappop(min_heap)

            if visited[node]:
                continue

            visited[node] = True
            edges += 1
            totalCost += weight

            for nei, w in graph[node]:
                if not visited[nei]:
                    heapq.heappush(min_heap, (w, nei))

        return totalCost
