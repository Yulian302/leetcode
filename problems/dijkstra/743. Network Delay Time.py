# https://leetcode.com/problems/network-delay-time/
# Difficulty: Medium
# Tags: dijkstra graph

# Problem
# You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

# We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

# Solution
# Time O(nlogn) and space O(n)
# Better to look at the image provided. We use dijkstra algorithm to find all the shortest paths from start node to other nodes. It will show us the travel time of a signal from its starting node to other nodes. And the minimum time required to travel to all the nodes will be the biggest distance.

from collections import defaultdict
from math import inf
from heapq import heappop, heappush


def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
    graph = defaultdict(list)
    for u, v, val in times:
        graph[u - 1].append([v - 1, val])

    distances = [inf] * n
    distances[k - 1] = 0
    heap = [(0, k - 1)]
    while heap:
        curr_dist, node = heappop(heap)
        if curr_dist > distances[node]:
            continue

        for nei, weight in graph[node]:
            dist = curr_dist + weight
            if dist < distances[nei]:
                distances[nei] = dist
                heappush(heap, (dist, nei))
    ans = max(distances)
    return ans if ans < inf else -1
