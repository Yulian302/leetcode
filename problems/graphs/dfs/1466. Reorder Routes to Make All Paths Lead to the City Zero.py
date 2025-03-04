# https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/
# Difficulty: Medium
# Tags: graph dfs

# Problem
# There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

# Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.

# This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

# Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.

# It's guaranteed that each city can reach city 0 after reorder.

# Solution
# Time O(n) and space O(n)
# Given graph resembles a tree. We can start from root (0 node) and go deeper using dfs, while checking for connections that must be reversed. In order to do that we can create a set of all connections. And while moving from left to right, we can check if a connection from zero to other nodes exists (from left to right). If yes, then increment our answer.


from collections import defaultdict
from typing import List


def minReorder(n: int, connections: List[List[int]]) -> int:
    rodes = set()
    graph = defaultdict(list)
    for x, y in connections:
        graph[x].append(y)
        graph[y].append(x)
        rodes.add((x, y))

    def dfs(node):
        ans = 0
        for nei in graph[node]:
            if nei not in seen:
                if (node, nei) in rodes:
                    ans += 1
                seen.add(nei)
                ans += dfs(nei)
        return ans

    seen = {0}
    return dfs(0)
