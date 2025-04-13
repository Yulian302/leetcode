# https://leetcode.com/problems/min-cost-to-connect-all-points/
# Difficulty: Medium
# Tags: graph mst kraskals

# Problem
# You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

# The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

# Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

# Solution
# Time O(N^2*logN) and space O(N)
# This problem is the Minimum Spanning Tree problem. It can be solved using Kraskal's algorithm. First we generate all possible points distances and each point index (for distinction). This forms all possible edges between points. [Kraskals algo] We sort them in ascending order, iterate from lowest weighted edge to largest and accept those that don't form a cycle (we can easily check for cycles using Disjoint Set Data Structure). If forms, just skip it. Then we return result only when the number of edges equals to the number of nodes - 1. [E == N-1]!

from typing import List


class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]

    # find parent
    def find(self, node):
        while node != self.parent[node]:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)

        # cycle detection
        if root1 == root2:
            return False

        if self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
            self.rank[root1] += 1
        else:
            self.parent[root1] = root2
            if self.rank[root1] == self.rank[root2]:
                self.rank[root2] += 1

        return True


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []

        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                distance = abs(x1 - x2) + abs(y1 - y2)
                edges.append((distance, i, j))  # (cost, node1, node2)

        edges.sort()

        ds = DisjointSet(n)
        total_cost = 0
        edges_used = 0

        for distance, i, j in edges:
            if ds.union(i, j):
                total_cost += distance
                edges_used += 1
                if edges_used == n - 1:
                    break

        return total_cost
