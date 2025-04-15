# https://leetcode.com/problems/connecting-cities-with-minimum-cost/
# Difficulty: Medium
# Tags: graph mst kraskals prims

# Problem
# There are n cities labeled from 1 to n. You are given the integer n and an array connections where connections[i] = [xi, yi, costi] indicates that the cost of connecting city xi and city yi (bidirectional connection) is costi.

# Return the minimum cost to connect all the n cities such that there is at least one path between each pair of cities. If it is impossible to connect all the n cities, return -1,

# The cost is the sum of the connections' costs used.

# Solution
# Time O(M*logN),where M is the number of edges -> O(M) as logN never exceeds 5 and space O(N): parents + weights
# This problem is the Minimum Spanning Tree problem. It can be solved using Kraskal's algorithm. We sort connections based on weight in ascending order. Then going one by one, we try to add edges with the least weight if they don't create a cycle (can be done efficiently using disjoint set).

from typing import List


class DisjointSet:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.rank = [1] * n

    # find root of a node
    def find(self, node):
        while node != self.root[node]:
            self.root[node] = self.root[self.root[node]]
            node = self.root[node]
        return node

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY:
            return

        if self.rank[rootX] > self.rank[rootY]:
            self.root[rootY] = rootX
            self.rank[rootX] += 1
        else:
            self.root[rootX] = rootY
            if self.rank[rootX] == self.rank[rootY]:
                self.rank[rootY] += 1

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        ds = DisjointSet(n)
        edges = 0
        totalCost = 0
        connections.sort(key=lambda x: x[2])
        for x, y, w in connections:
            if not ds.is_connected(x - 1, y - 1):
                ds.union(x - 1, y - 1)
                edges += 1
                totalCost += w
        return totalCost if edges == n - 1 else -1
