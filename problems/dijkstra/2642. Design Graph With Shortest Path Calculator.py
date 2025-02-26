# https://leetcode.com/problems/design-graph-with-shortest-path-calculator/
# Difficulty: Hard
# Tags: dijkstra graph min_heap

# Problem
# There is a directed weighted graph that consists of n nodes numbered from 0 to n - 1. The edges of the graph are initially represented by the given array edges where edges[i] = [fromi, toi, edgeCosti] meaning that there is an edge from fromi to toi with the cost edgeCosti.

# Implement the Graph class:

#     Graph(int n, int[][] edges) initializes the object with n nodes and the given edges.
#     addEdge(int[] edge) adds an edge to the list of edges where edge = [from, to, edgeCost]. It is guaranteed that there is no edge between the two nodes before adding this one.
#     int shortestPath(int node1, int node2) returns the minimum cost of a path from node1 to node2. If no path exists, return -1. The cost of a path is the sum of the costs of the edges in the path.

# Solution
# Time O(ElogN) and space O(N+E)
# We use dijkstra algorithm for this problem in order to find the shortest path from node1 to node2. If it doesn't exist, we return -1.

from collections import defaultdict
from heapq import heappop, heappush


class Graph:

    def __init__(self, n: int, edges: list[list[int]]):
        self.graph = defaultdict(list)
        self.n = n
        for u, v, w in edges:
            self.graph[u].append([v, w])

    def addEdge(self, edge: list[int]) -> None:
        u, v, w = edge
        if [v, w] not in self.graph[u]:
            self.graph[u].append([v, w])

    def shortestPath(self, node1: int, node2: int) -> int:
        distances = [float("inf")] * self.n
        distances[node1] = 0
        min_heap = [(0, node1)]
        while min_heap:
            dist, node = heappop(min_heap)
            if dist > distances[node]:
                continue
            for nei, weight in self.graph[node]:
                new_dist = dist + weight
                if new_dist < distances[nei]:
                    distances[nei] = new_dist
                    heappush(min_heap, (new_dist, nei))
        return distances[node2] if distances[node2] != float("inf") else -1


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
