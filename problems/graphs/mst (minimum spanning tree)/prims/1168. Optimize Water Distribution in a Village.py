# https://leetcode.com/problems/optimize-water-distribution-in-a-village/
# Difficulty: Hard
# Tags: graph mst virtual_node

# Problem
# There are n houses in a village. We want to supply water for all the houses by building wells and laying pipes.

# For each house i, we can either build a well inside it directly with cost wells[i - 1] (note the -1 due to 0-indexing), or pipe in water from another well to it. The costs to lay pipes between houses are given by the array pipes where each pipes[j] = [house1j, house2j, costj] represents the cost to connect house1j and house2j together using a pipe. Connections are bidirectional, and there could be multiple valid connections between the same two houses with different costs.

# Return the minimum total cost to supply water to all houses.

# Solution
# Time O((N+M)*log(N+M)) and space O(N+M)
# This problem is the Minimum Spanning Tree problem. It can be solved using Prim's algorithm. But first we need to understand why. We create a virtual 0 node that represents a well. Then we add connections from this well to other houses. The minimum spanning tree will form an optimal water distribution system for the houses (as it's a subgraph in a graph that connects all vertices with N-1 edges, where N is the number of vertices in the most efficient way (minimum total edges cost)).

import heapq
from typing import List


class Solution:
    def minCostToSupplyWater(
        self, n: int, wells: List[int], pipes: List[List[int]]
    ) -> int:
        # {key: value} -> key: int (node), value: [int] (nodes)
        graph = {i: [] for i in range(n + 1)}
        for node1, node2, cost in pipes:
            graph[node1].append((node2, cost))
            graph[node2].append((node1, cost))

        # adding well (virtual node 0)
        for house in range(1, n + 1):
            graph[0].append((house, wells[house - 1]))

        # find minimum spanning tree (Prim's)

        totalCost = 0
        min_heap = []
        startNode = 0
        visited = [False] * (n + 1)
        heapq.heappush(min_heap, (0, startNode))

        while min_heap:
            cost, node = heapq.heappop(min_heap)

            if visited[node]:
                continue

            visited[node] = True
            totalCost += cost
            for nei, weight in graph[node]:
                if not visited[nei]:
                    heapq.heappush(min_heap, (weight, nei))

        return totalCost
