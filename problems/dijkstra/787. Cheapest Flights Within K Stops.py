# https://leetcode.com/problems/cheapest-flights-within-k-stops/
# Difficulty: Medium
# Tags: dijkstra graph min_heap

# Problem
# There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

# You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.

# Solution
# Time O(V+ElogV) and space O(V+E)
# We use dijkstra algorithm to find the cheapest flights from src to dest. But we need to keep track of the number of stops (k). So, our min heap internal logic is a bit different and has some additional if statements. Distances is an array of type [cost, stops], min heap is of type [cost, node, stops]. In this problem, dist = cost.

from cmath import inf
from collections import defaultdict
from heapq import heappop, heappush
from typing import List


def findCheapestPrice(n: int, flights, src: int, dst: int, k: int
                      ) -> int:
    graph = defaultdict(list)
    for x, y, dist in flights:
        graph[x].append([y, dist])

    distances = [[float("inf"), 0] for _ in range(n)]
    # [cost, stops]
    distances[src] = [0, 0]
    # (cost, node, stops)
    min_heap = [(0, src, 0)]
    while min_heap:
        curr_cost, node, stops = heappop(min_heap)

        if node == dst:
            return curr_cost

        if stops > k:
            continue

        for nei, cost in graph[node]:
            new_cost = curr_cost + cost
            if new_cost < distances[nei][0] or stops + 1 < distances[nei][1]:
                distances[nei] = [new_cost, stops + 1]
                heappush(min_heap, (new_cost, nei, stops + 1))
    return -1


# --- or ---
# Bellman-Ford algorithm
# Two arrays are used to keep track of prev distances and current distances. Edge relaxation is used to update with more optimal routes. This algorithm is good for finding shortest distance (or cheapest path) from source to destination with at most K edges.

class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        if src == dst:
            return 0

        prev = [inf] * n
        curr = [inf] * n
        prev[src] = 0

        for i in range(1, k + 2):
            curr[src] = 0

            for from_, to_, price in flights:
                if prev[from_] < inf:
                    curr[to_] = min(curr[to_], prev[from_] + price)

            prev = curr[:]

        return curr[dst] if curr[dst] != inf else -1
