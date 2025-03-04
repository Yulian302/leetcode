# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
# Difficulty: Medium
# Tags: graph dfs

# Problem
# You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

# Return the number of connected components in the graph.

# Solution
# Time O(V+E) and space O(V+E)
# This problem is similar to 200. Number of Provinces. We start from initial node (0), keep track of seen and update our answer of visited times. We also use dfs to go through all connected nodes. Therefore, using this method we can easily count number of connected components or provinces.

from collections import defaultdict
from typing import List


def countComponents(n: int, edges: List[List[int]]) -> int:
    if n == 1:
        return 1

    graph = defaultdict(list)
    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)

    seen = set()
    ans = 0

    def dfs(node):
        for nei in graph[node]:
            if nei not in seen:
                seen.add(nei)
                dfs(nei)

    for i in range(n):
        if i not in seen:
            seen.add(i)
            ans += 1
            dfs(i)
    return ans
