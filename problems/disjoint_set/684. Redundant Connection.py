# https://leetcode.com/problems/redundant-connection/
# Difficulty: Medium
# Tags: disjoint_set graph

# Problem
# In this problem, a tree is an undirected graph that is connected and has no cycles.

# You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

# Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

# Solution
# Time O(N*Alpha(N)) and space O(N)
# We can use a disjoint set data structure to efficiently solve this problem. In our DS we use a ranking system to balance our formed tree and path compression for more efficient root search. Moreover, we keep track of redundant edges. For a disjoint set, the redundant edge is the one where we have same root elements before doing union operation. In the end, we return the last found redundant edge.

from typing import List


class DisjointSet:
    def __init__(self, n):
        self.root = list(range(n))
        self.rank = [1] * n
        self.redundant = []

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x-1)
        rootY = self.find(y-1)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootY] > self.rank[rootX]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
        else:
            self.redundant.append([x, y])


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        elems = set()
        for x, y in edges:
            elems.add(x)
            elems.add(y)

        ds = DisjointSet(len(elems))
        for x, y in edges:
            ds.union(x, y)

        return ds.redundant[-1]
