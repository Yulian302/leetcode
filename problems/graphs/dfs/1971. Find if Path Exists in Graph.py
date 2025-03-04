# https://leetcode.com/problems/find-if-path-exists-in-graph/
# Difficulty: Easy (Medium)
# Tags: graph dfs

# Problem
# There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

# You want to determine if there is a valid path that exists from vertex source to vertex destination.

# Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.


# Solution
# Time O(V+E) and space O(V), because we can have a different number of edges, which is less that number of vertices
# We use dfs to react the destination starting from source. If it is possible, we return True. Otherwise, False.


from collections import defaultdict
from typing import List


def validPath(n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    if source == destination:
        return True

    graph = defaultdict(list)
    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)

    seen = set()

    def dfs(node):
        if node == destination:
            return True

        seen.add(node)
        for nei in graph[node]:
            if nei not in seen:
                if dfs(nei):
                    return True
        return False

    return dfs(source)
